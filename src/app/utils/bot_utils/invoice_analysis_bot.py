from ...utils.scripts_utils import screenshot,mouse
from ...utils.ocr_utils.capture import *

def check_Facture() -> dict:

    img = screenshot.region_screenshot(screenshot.calculate_region(656,316,767,357),"nameFacture.png")

    name = image_to_string(img).replace("\n","")

    img = screenshot.region_screenshot(screenshot.calculate_region(996,972,1248,991),"priceFacture.png")

    price = int(image_to_string(img).replace(".",""))

    img = screenshot.region_screenshot(screenshot.calculate_region(657,399,874,417),"emailFacture.png")

    email = image_to_string(img).replace("\n","")

    img = screenshot.region_screenshot(screenshot.calculate_region(653,265,749,290),"dateFacture.png")

    date = image_to_string(img).replace("\n","")

    return  {"name": name,"price": price,"email": email,"date": date }