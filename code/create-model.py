import requests, os, json, sys

# run this if you want to create a new model again with your API key

BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
AUTH_KEY = "V1_-CV8arzT-DTTH2cu6d0DhThUQ1y-l" # you have to place your own API key
url = BASE_URL + "Model/"

categories = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35"]
ext = ['.jpeg', '.jpg', ".JPG", ".JPEG",".png", ".PNG"]

data = {'categories' : categories}
headers = {
        'accept': 'application/x-www-form-urlencoded'
    }

response = requests.request("POST", url, headers=headers, auth=requests.auth.HTTPBasicAuth(AUTH_KEY, ''), data=data)
result = json.loads(response.text)
if not("model_id" in result.keys()):
    print('Error')
    print(result)
    sys.exit(1)
model_id = result["model_id"]

print("NEXT RUN: export NANONETS_MODEL_ID=" + model_id)
print("THEN RUN: python ./code/upload-training.py")
