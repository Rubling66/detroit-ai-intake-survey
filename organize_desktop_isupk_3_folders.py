import os
import shutil

base_desktop = r"C:\Users\Admin\Desktop\ISUPK"
os.makedirs(base_desktop, exist_ok=True)

# 3 Subfolders
folder1 = os.path.join(base_desktop, "01_PRINTABLE_PAMPHLETS_AND_FLYERS")
folder2 = os.path.join(base_desktop, "02_MEETING_CARDS_AND_FACILITATOR_GUIDES")
folder3 = os.path.join(base_desktop, "03_EDUCATIONAL_STUDY_PACKS_AND_SPECS")

for f in [folder1, folder2, folder3]:
    os.makedirs(f, exist_ok=True)

# Copy base images to all 3 folders so all standalone HTML files render graphics offline
base_images = ["logo.jfif", "tribes_chart.jpg", "community_graphic.jpg"]
src_base = r"c:\Users\Admin\Desktop\detroit_ai_intake_survey\assets"

for img in base_images:
    src_img = os.path.join(src_base, img)
    if not os.path.exists(src_img):
        src_img = os.path.join(base_desktop, img)
    if os.path.exists(src_img):
        for f in [base_desktop, folder1, folder2, folder3]:
            shutil.copy(src_img, os.path.join(f, img))

# Mapping files to 3 folders
folder1_files = [
    ("flyers/trifold_heritage.html", "01_Trifold_Heritage_and_Scripture.html"),
    ("flyers/trifold_spanish.html", "02_Trifold_Spanish_Educativo.html"),
    ("flyers/trifold_community.html", "03_Trifold_Community_Aid_and_ReEntry.html"),
    ("flyers/flyer_flint_popup.html", "04_Flyer_Flint_PopUp_Table.html"),
    ("flyers/flyer_virtual_bible_study.html", "05_Flyer_Virtual_Bible_Study.html"),
    ("flyers/flyer_spanish_outreach.html", "06_Flyer_Spanish_Outreach.html"),
    ("flyers/flyer_community_aid_drive.html", "07_Flyer_Community_Aid_Drive.html")
]

folder2_files = [
    ("flyers/meeting_close_card.html", "01_Meeting_Close_Decision_Card_2Up.html"),
    ("flyers/meeting_close_guide.html", "02_Meeting_Facilitator_Close_Guide.html")
]

folder3_files = [
    ("downloads/12_tribes_scriptural_chart.html", "01_StudyChart_12_Tribes_Poster.html"),
    ("downloads/deuteronomy_28_prophecy_guide.html", "02_StudyGuide_Deuteronomy_28_Prophecy.html"),
    ("downloads/guia_estudio_espanol.html", "03_StudyGuide_Spanish_Guia_Familia.html"),
    ("downloads/prison_ministry_resource_pack.html", "04_StudyGuide_Prison_Ministry_Pack.html")
]

src_project = r"c:\Users\Admin\Desktop\detroit_ai_intake_survey"

def copy_and_adjust(file_list, target_folder):
    for src_rel, dest_name in file_list:
        full_src = os.path.join(src_project, src_rel)
        full_dest = os.path.join(target_folder, dest_name)
        if os.path.exists(full_src):
            with open(full_src, 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.replace('../assets/logo.jfif', 'logo.jfif')
            content = content.replace('../assets/tribes_chart.jpg', 'tribes_chart.jpg')
            content = content.replace('../assets/community_graphic.jpg', 'community_graphic.jpg')
            content = content.replace('assets/logo.jfif', 'logo.jfif')
            content = content.replace('assets/tribes_chart.jpg', 'tribes_chart.jpg')
            content = content.replace('assets/community_graphic.jpg', 'community_graphic.jpg')
            with open(full_dest, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Deposited in {os.path.basename(target_folder)}: {dest_name}")

copy_and_adjust(folder1_files, folder1)
copy_and_adjust(folder2_files, folder2)
copy_and_adjust(folder3_files, folder3)

# Master Spec HTML in root and folder3
specs_src = os.path.join(base_desktop, "00_PRINT_CATALOG_AND_GRAPHIC_SPECS.html")
if os.path.exists(specs_src):
    shutil.copy(specs_src, os.path.join(folder3, "00_PRINT_CATALOG_AND_GRAPHIC_SPECS.html"))

print("Successfully organized ISUPK Desktop folder into 3 professional subfolders.")
