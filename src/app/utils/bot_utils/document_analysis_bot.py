from utils.scripts_utils import screenshot
from utils.ocr_utils.capture import *

def check_document()-> dict:

    img = screenshot.region_screenshot(screenshot.calculate_region(950,475,1189,516),"nameDoc.png")

    name = image_to_string(img).replace("\n","")

    img = screenshot.region_screenshot(screenshot.calculate_region(940,708,1079,749),"experienceDoc.png")

    experience = (image_to_string(img).replace("\n","")).split()
    experience = int(experience[0])

    img = screenshot.region_screenshot(screenshot.calculate_region(948,547,1121,588),"idDoc.png")

    member_id = image_to_string(img).replace("\n","")

    img = screenshot.region_screenshot(screenshot.calculate_region(943,623,1146,660),"phoneDoc.png")

    phone = image_to_string(img).replace("\n","")

    return {"name":name,"experience":experience,"phone": phone,"member_id":member_id}