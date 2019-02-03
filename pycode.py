"""
Doggy doggy doo
"""

import os  # Used for file search
import io  # Used to load images into memory

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

import cv2  # Used to capture a video stream
import uuid  # Used to make unique file names


# Gets api credentials for Google Play Platform
def api_cred():
    # Sets environment for API call
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "X"


# Returns a file from a file path, and filename
def get_image_file(file_path: object, file_name: object) -> object:
    my_file = os.path.join(os.path.dirname(file_path), file_name)
    # Loads the image into memory
    with io.open(my_file, 'rb') as image_file:
        content = image_file.read()
    return types.Image(content=content)


# Returns a path to an image with a unique name
def get_unique_image_path(file_path):
    return file_path + uuid.uuid4().hex + ".png"


# Returns the path to an image captured from the camera
def get_image_camera(file_path):
    vid_stream = cv2.VideoCapture(0)
    if not vid_stream.isOpened():
        print("Error: Failed to open video stream")

    count = 0
    while vid_stream.isOpened():
        ret, frame = vid_stream.read()
        count += 1
        if count == 10 and ret:
            file_path = get_unique_image_path(file_path)
            # save frame as PNG file
            cv2.imwrite(file_path, frame)
            # Frees resources
            vid_stream.release()
            cv2.destroyAllWindows()
            # Loads the image into memory
            with io.open(file_path, 'rb') as image_file:
                content = image_file.read()
            return types.Image(content=content)


def print_info(dog_treat):
    # add deadly categories here
    av = "Avocados can cause vomiting or diarrhea in large quantities. The pit of the avocado can cause death."
    al = "Alcohol can cause vomiting or diarrhea in large quantities, even death."
    alm = "Dogs can choke on almonds if not chewed completely."
    am = "Apple seeds release cyanide when chewed, which is poisonous to dogs."
    b = "Small bones can be deadly to dogs, since bone fragments can harm their digestive system."
    cin = "Inhaling cinnamon can cause respiratory problems in dogs."
    co = "Theobromine and methylxanthines found in chocolate can cause heart problems and/or other dangerous effects."
    f = "Salmon, if uncooked, may have parasites which can lead to death in some dogs."
    g = "Grape products are deadly to dogs."
    m = "Marijuana can cause death in your pet."
    o = "Oxalates can cause vomiting, diarrhea, weakness, tremors, and bloody urine."
    p = "Peach and plum pits contain cyanide which is poisonous to pets."
    s = "Salt produces excessive thirst and urination in pets, and can even cause sodium ion poisoning."
    "Causes diarrhea, vomiting, tremors, and seizures."
    v = "Onions, Chives, or Garlic can cause gastrointestinal irritation and could lead to red blood cell damage."
    x = "Xylithol causes insulin release which can cause liver failure."
    y = "Yeast can cause the animal’s stomach to bloat which can cause life threatening situations."

    # Deadly ingredients and derivatives in dictionary as key and the category variable above as value
    deadly = {"grapes": g, "grape": g, "raisin": g, "raisins": g, "wine": g,
              "artificial sweetener": x, "gum": x, "chewing gum": x,
              "avocado": av, "avocados": av,
              "alcohol": al, "beer": al,
              "almond": alm, "almonds": alm,
              "apple": am, "apples": am, "apple seeds": am,
              "bone": b, "bones": b, "chicken bone": b, "chicken bones": b, "fish bone": b, "fish bones": b,
              "cinnamon": cin,
              "chocolate": co, "coffee": co, "caffeine": co,
              "salmon": f, "fish": f,
              "marijuana": m, "cannabis": m, "hemp": m,
              "tomato leaves": o,
              "peaches": p, "peach": p, "plum": p, "plums": p, "pit": p, "pits": p,
              "onion": v, "onions": v, "garlic": v, "chive": v, "chives": v,
              "salt": s, "sodium chloride": s, "salty": s,
              "yeast": y, "bread": y, "dough": y}

    # Unhealthy categories
    an = "Raw meat can contain bacteria which can cause harm to the pet."
    c = "Citrus can give dogs an upset stomach."
    d = "Some animals are lactose intolerant."
    e = "Raw eggs contain avidin, which decreases the absorption of biotin which can cause skin problems."
    n = "Some nuts can can cause pancreatitis, vomiting, or diarrhea but is not toxic to dogs."
    coco = "Coconuts are not deadly but can upset a dog's stomach."

    # Unhealthy ingredients and derivatives in dictionary as key and the category variable above as value
    unhealthy = {"oranges": c, "orange": c, "lime": c, "limes": c, "lemons": c, "lemon": c,
                 "raw meat": an,
                 "coconut": coco, "coconuts": coco,
                 "dairy": d, "milk": d,
                 "raw eggs": e,
                 "nuts": n, "walnuts": n, "macadamia nuts": n, "pecans": n, "macadamia nut": n, "nut": n, "walnut": n,
                 "nut": n, }

    food_info = set()

    # logic for testing

    for treat in dog_treat:
        if treat in deadly:
            food_info.add(deadly.get(treat))
        elif treat in unhealthy:
            food_info.add(unhealthy.get(treat))
    food = ""
    for ele in food_info:
        food += ele + '<br>'
    return food


# Main Function
def main():
    api_cred()  # Secures API credentials
    client = vision.ImageAnnotatorClient()  # New client instance
    # Performs text detection on the image file
    file_path = "X"
    response = client.text_detection(image=get_image_camera(file_path))  # Gets img)
    # get_image_file(file_path, ___f_names___[0])
    texts = response.text_annotations

    output = []  # Stores strings of output
    for text in texts:  # For each text input
        desc = ''.join(filter(str.isalpha, text.description)).lower()  # Ensures it is alphabetic, then lower()s it
        if len(desc) > 1:  # Only appends strings of size 2 or more
            output.append(desc)

    # for ele in output:  # Prints it just to display values
    #     print(ele)
    return print_info(output)


main()  # Calls main function
