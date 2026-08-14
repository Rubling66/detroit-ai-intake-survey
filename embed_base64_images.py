import base64
import os

base_dir = r"c:\Users\Admin\Desktop\detroit_ai_intake_survey"

def get_base64_img(rel_path):
    full_path = os.path.join(base_dir, rel_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode('utf-8')
            ext = os.path.splitext(full_path)[1].lower().replace('.', '')
            if ext == 'jfif' or ext == 'jpg' or ext == 'jpeg':
                mime = 'image/jpeg'
            elif ext == 'png':
                mime = 'image/png'
            else:
                mime = 'image/jpeg'
            return f"data:{mime};base64,{encoded}"
    return ""

logo_b64 = get_base64_img("assets/logo.jfif")
tribes_b64 = get_base64_img("assets/tribes_chart.jpg")
community_b64 = get_base64_img("assets/community_graphic.jpg")

print(f"Logo Base64 length: {len(logo_b64)}")
print(f"Tribes Base64 length: {len(tribes_b64)}")
print(f"Community Base64 length: {len(community_b64)}")
