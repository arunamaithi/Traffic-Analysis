"""
This code is to upload traning dataset

Set training dataset path correctly before execute

Use your own API key and model id if you create model for your dataset

"""
import os, requests

BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
url = BASE_URL + 'UploadFile/'

categories = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35"]
ext = ['.jpeg', '.jpg', ".JPG", ".JPEG",".png", ".PNG"]
image_folder_path = "./images/train/"

model_id = "c0c3c611-dc87-4576-bb11-53a265d55a60" # your model id
AUTH_KEY = "V1_-CV8arzT-DTTH2cu6d0DhThUQ1y-l" # your API key

for category in categories:        
    class_image_path = os.path.join(image_folder_path, category)    
    all_class_images = [os.path.join(class_image_path, x) for x in os.listdir(class_image_path) if x.endswith(tuple(ext))]        
    for image in all_class_images:
        print (image)
        data = {'file' :open(image, 'rb'), 'category' :('', category), 'modelId' :('', model_id)}
        response = requests.post(url, auth= requests.auth.HTTPBasicAuth(AUTH_KEY, ''), files=data)
        if response.status_code > 250 or response.status_code<200:
            print(response.text), response.status_code

print("\n\n\nNEXT RUN: python ./code/train-model.py") 

