import sqlite3
import os

# Create data directory if not exists
os.makedirs('data', exist_ok=True)
os.makedirs('downloads', exist_ok=True)

db_path = os.path.join('data', 'outreach.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Table 1: Campaign Metrics (Track 1,000 reach goal & budget)
cursor.execute('''
CREATE TABLE IF NOT EXISTS campaign_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    campaign_name TEXT NOT NULL,
    target_engagements INTEGER DEFAULT 1000,
    current_engagements INTEGER DEFAULT 420,
    budget_allocated REAL DEFAULT 1000.00,
    budget_spent REAL DEFAULT 450.00,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Table 2: Material & Info Kit Requests (From web forms)
cursor.execute('''
CREATE TABLE IF NOT EXISTS material_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    contact_info TEXT NOT NULL,
    street_address TEXT,
    city_location TEXT NOT NULL,
    request_type TEXT NOT NULL,
    comments TEXT,
    status TEXT DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Table 3: Download Library Items
cursor.execute('''
CREATE TABLE IF NOT EXISTS resource_library (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    filename TEXT NOT NULL,
    category TEXT NOT NULL,
    download_count INTEGER DEFAULT 0,
    file_size_kb INTEGER DEFAULT 250,
    description TEXT
)
''')

# Seed Initial Campaign Data if empty
cursor.execute("SELECT COUNT(*) FROM campaign_metrics")
if cursor.fetchone()[0] == 0:
    cursor.execute('''
    INSERT INTO campaign_metrics (campaign_name, target_engagements, current_engagements, budget_allocated, budget_spent)
    VALUES ('Mid-Michigan Phase 1 Outreach', 1000, 420, 1000.00, 450.00)
    ''')

# Seed Resource Library Metadata if empty
cursor.execute("SELECT COUNT(*) FROM resource_library")
if cursor.fetchone()[0] == 0:
    resources = [
        ('12-Tribes Scriptural Poster', '12_tribes_scriptural_chart.html', 'Chart', 142, 380, 'Full reference chart of the 12 tribes and scripture breakdown.'),
        ('Deuteronomy 28 Prophecy Study Guide', 'deuteronomy_28_prophecy_guide.html', 'Booklet', 218, 520, '16-page study guide covering scriptural prophecies.'),
        ('Guia de Estudio en Espanol', 'guia_estudio_espanol.html', 'Bilingual', 95, 410, 'Folleto educativo traducido al espanol.'),
        ('Prison Ministry Resource Pack', 'prison_ministry_resource_pack.html', 'Ministry', 64, 490, 'Rehabilitation and moral mentorship study pack.')
    ]
    cursor.executemany('''
    INSERT INTO resource_library (title, filename, category, download_count, file_size_kb, description)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', resources)

# Seed Sample Community Requests
cursor.execute("SELECT COUNT(*) FROM material_requests")
if cursor.fetchone()[0] == 0:
    sample_requests = [
        ('Marcus Johnson', 'marcus.j@example.com', '123 E. 5th Ave', 'Flint', 'Free Physical Info & Study Kit', 'Please mail the printed pamphlet to my home.', 'Fulfilled'),
        ('Elena Rodriguez', 'elena.r@example.com', '456 Saginaw St', 'Flint', 'Spanish Study Booklet', 'Interesada en los folletos en espanol.', 'Pending'),
        ('David Smith', 'dsmith@example.com', '789 Washington Ave', 'Saginaw', 'Virtual Bible Class Zoom Link', 'Looking forward to the Tuesday evening class.', 'Pending')
    ]
    cursor.executemany('''
    INSERT INTO material_requests (full_name, contact_info, street_address, city_location, request_type, comments, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', sample_requests)

conn.commit()
conn.close()
print("Database 'data/outreach.db' created and seeded successfully.")
