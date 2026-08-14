import http.server
import socketserver
import json
import sqlite3
import urllib.parse
import os

PORT = 8080
DB_PATH = os.path.join('data', 'outreach.db')

class OutreachAPIHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        # API Route: Fetch Campaign Progress Metrics
        if parsed_path.path == '/api/progress':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT target_engagements, current_engagements, budget_allocated, budget_spent FROM campaign_metrics ORDER BY id DESC LIMIT 1")
            row = cursor.fetchone()
            conn.close()
            
            if row:
                response = {
                    "target_engagements": row[0],
                    "current_engagements": row[1],
                    "budget_allocated": row[2],
                    "budget_spent": row[3],
                    "percentage": round((row[1] / row[0]) * 100, 1)
                }
            else:
                response = {"target_engagements": 1000, "current_engagements": 420, "percentage": 42.0}
                
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return
            
        # API Route: Fetch List of Requests (Admin view)
        elif parsed_path.path == '/api/requests':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT id, full_name, contact_info, city_location, request_type, status, created_at FROM material_requests ORDER BY id DESC")
            rows = cursor.fetchall()
            conn.close()
            
            requests_list = []
            for r in rows:
                requests_list.append({
                    "id": r[0],
                    "full_name": r[1],
                    "contact_info": r[2],
                    "city_location": r[3],
                    "request_type": r[4],
                    "status": r[5],
                    "created_at": r[6]
                })
                
            self.wfile.write(json.dumps(requests_list).encode('utf-8'))
            return

        # Default static file serving
        return super().do_GET()

    def do_POST(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        # API Route: Receive New Request Form Submission
        if parsed_path.path == '/api/request':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            
            try:
                data = json.loads(body)
            except Exception:
                # Fallback for form-encoded data
                data = urllib.parse.parse_qs(body)
                data = {k: v[0] for k, v in data.items()}
                
            full_name = data.get('fullName', data.get('full_name', 'Anonymous'))
            contact_info = data.get('contactEmail', data.get('contact_info', 'N/A'))
            street_address = data.get('streetAddress', data.get('street_address', ''))
            city_location = data.get('cityLocation', data.get('city_location', 'Flint'))
            request_type = data.get('interestType', data.get('request_type', 'General Info'))
            comments = data.get('commentsMessage', data.get('comments', ''))
            
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO material_requests (full_name, contact_info, street_address, city_location, request_type, comments)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (full_name, contact_info, street_address, city_location, request_type, comments))
            
            # Increment engagement metric
            cursor.execute("UPDATE campaign_metrics SET current_engagements = current_engagements + 1 WHERE id = 1")
            conn.commit()
            
            # Fetch updated engagements count
            cursor.execute("SELECT current_engagements, target_engagements FROM campaign_metrics WHERE id = 1")
            updated = cursor.fetchone()
            conn.close()
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            res = {
                "success": True,
                "message": f"Thank you, {full_name}! Your request for '{request_type}' has been recorded.",
                "new_engagements": updated[0] if updated else 421
            }
            self.wfile.write(json.dumps(res).encode('utf-8'))
            return

        self.send_error(404, "Endpoint not found")

if __name__ == '__main__':
    # Ensure DB exists
    if not os.path.exists(DB_PATH):
        import init_db
    
    with socketserver.TCPServer(("", PORT), OutreachAPIHandler) as httpd:
        print(f"Backend Server & REST API running at http://localhost:{PORT}")
        httpd.serve_forever()
