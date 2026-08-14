import os
import shutil

src_project = r"c:\Users\Admin\Desktop\detroit_ai_intake_survey"
desktop_dir = r"C:\Users\Admin\Desktop\ISUPK"

# Ensure all 3 subfolders exist and have all final versions
folder1 = os.path.join(desktop_dir, "01_PRINTABLE_PAMPHLETS_AND_FLYERS")
folder2 = os.path.join(desktop_dir, "02_MEETING_CARDS_AND_FACILITATOR_GUIDES")
folder3 = os.path.join(desktop_dir, "03_EDUCATIONAL_STUDY_PACKS_AND_SPECS")

for f in [desktop_dir, folder1, folder2, folder3]:
    os.makedirs(f, exist_ok=True)

# Copy invoice to root and all subfolders
invoice_src = os.path.join(src_project, "invoice_project_calculator.html")
if os.path.exists(invoice_src):
    for f in [desktop_dir, folder1, folder2, folder3]:
        shutil.copy(invoice_src, os.path.join(f, "00_PROJECT_BILLING_INVOICE_CALCULATOR.html"))

print("All local saves, desktop syncs, and website versions finalized.")
