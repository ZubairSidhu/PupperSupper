import os  # Used for file search
import io  # Used to load images into memory
 
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import storage
import base64
 
# Gets api credentials for Google Play Platform
def api_cred():
  print('api_cred')
    # Sets environment for API call
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/DogFitness-3e9c56e7ef8c.json"
 
 
def get_image_uri(uri):
    image = vision.types.Image()
    image.source.image_uri = uri
    #print('get_image_uri')
    #print(image)
    return image

def send_base64(string):
    image = vision.types.Image()
    image.content = string.encode()
    #image.source.image_uri = uri
    #print('get_image_uri')
    #print(image)
    return image
 
 
def print_info(dog_treat):
    # add deadly categories here
    av = "Avocados can cause vomiting or diarrhea in large quantities. The pit of the avocado can cause death."
    al = "Alcohol can cause vomiting or diarrhea in large quantities, even death."
    alm = "Dogs can choke on almonds if not chewed completely."
    am = "Apple seeds contain cyanide which is poisonous to dogs."
    b = "Bones can be deadly to dogs since bone fragments can harm their digestive system."
    cin = "Inhaling cinnamon can cause respiratory problems in dogs."
    co = "Theobromine and methylxanthines can cause heart problems and/or other dangerous effects."
    f = "Salmon if uncooked may have parasites which can lead to death in some pets."
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
 
    for food in food_info:
        print(food)
 
  
def upload_blob(data, content_type, destination_blob_name):
    """Uploads a file to the bucket."""

    print(data[:22])
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('dogfitness-vcm')
    blob = bucket.blob(destination_blob_name)

    decoded = base64.b64decode(data[22:])

    blob.upload_from_string(decoded, content_type=content_type)


# Main Function
def main(img_uri):
    api_cred()  # Secures API credentials

    print('Uploading Blob')
    upload_blob(img_uri, 'image/png', 'yee-haw.png')

    client = vision.ImageAnnotatorClient()  # New client instance
    # Performs text detection on the image file
    # response = client.text_detection(image=get_image_url(img_uri))  # Gets img
    my_img = send_base64('gs://dogfitness-vcm/yee-haw.png')
    
    print('my_img')
    # prints(my_img)
    response = client.text_detection(image=my_img)
    print('response')
    print(response) 
    texts = response.text_annotations
    print('In Main mainLogic.py')
    print("Text Read: ") 
    print (texts)

    f = open("demofile.txt", "w")
    f.write(img_uri)

    output = []  # Stores strings of output
    for text in texts:  # For each text input
        desc = ''.join(filter(str.isalpha, text.description)).lower()  # Ensures it is alphabetic, then lower()s it
        if len(desc) > 1:  # Only appends strings of size 2 or more
            output.append(desc)
    return output
 
 
#main(image_url)  # Calls main function