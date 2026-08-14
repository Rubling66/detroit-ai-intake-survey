import os
import shutil

dest_dir = r"C:\Users\Admin\Desktop\ISUPK"
os.makedirs(dest_dir, exist_ok=True)

# Copy logo if not already present in ISUPK folder
src_logo = r"C:\Users\Admin\Desktop\ISUPK\OIP.jfif"
dest_logo = os.path.join(dest_dir, "logo.jfif")
if os.path.exists(src_logo) and src_logo != dest_logo:
    shutil.copy(src_logo, dest_logo)

# Source directory containing compiled materials
src_base = r"c:\Users\Admin\Desktop\detroit_ai_intake_survey"

# File Mappings: (source_rel_path, dest_filename)
files_to_copy = [
    ("flyers/trifold_heritage.html", "01_Trifold_Heritage_and_Scripture.html"),
    ("flyers/trifold_spanish.html", "02_Trifold_Spanish_Educativo.html"),
    ("flyers/trifold_community.html", "03_Trifold_Community_Aid_and_ReEntry.html"),
    ("flyers/flyer_flint_popup.html", "04_Flyer_Flint_PopUp_Table.html"),
    ("flyers/flyer_virtual_bible_study.html", "05_Flyer_Virtual_Bible_Study.html"),
    ("flyers/flyer_spanish_outreach.html", "06_Flyer_Spanish_Outreach.html"),
    ("flyers/flyer_community_aid_drive.html", "07_Flyer_Community_Aid_Drive.html"),
    ("flyers/meeting_close_card.html", "08_Meeting_Close_Decision_Card_2Up.html"),
    ("flyers/meeting_close_guide.html", "09_Meeting_Facilitator_Close_Guide.html"),
    ("downloads/12_tribes_scriptural_chart.html", "10_StudyChart_12_Tribes_Poster.html"),
    ("downloads/deuteronomy_28_prophecy_guide.html", "11_StudyGuide_Deuteronomy_28_Prophecy.html"),
    ("downloads/guia_estudio_espanol.html", "12_StudyGuide_Spanish_Guia_Familia.html"),
    ("downloads/prison_ministry_resource_pack.html", "13_StudyGuide_Prison_Ministry_Pack.html")
]

for src_rel, dest_name in files_to_copy:
    full_src = os.path.join(src_base, src_rel)
    full_dest = os.path.join(dest_dir, dest_name)
    
    if os.path.exists(full_src):
        with open(full_src, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Adjust logo image relative paths to load 'logo.jfif' directly from Desktop\ISUPK folder
        content = content.replace('../assets/logo.jfif', 'logo.jfif')
        content = content.replace('assets/logo.jfif', 'logo.jfif')
        content = content.replace('OIP.jfif', 'logo.jfif')
        
        with open(full_dest, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Copied & Path-Adjusted: {dest_name}")
    else:
        print(f"Warning: Source not found {full_src}")

print("All standalone print files successfully deposited in Desktop\\ISUPK.")
