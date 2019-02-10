import requests, os, json

model_id = "c0c3c611-dc87-4576-bb11-53a265d55a60" # your model id
AUTH_KEY = "V1_-CV8arzT-DTTH2cu6d0DhThUQ1y-l" # your API key

BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
url = BASE_URL + 'Train/'

querystring = {'modelId': model_id}
response = requests.request('POST', url, auth=requests.auth.HTTPBasicAuth(AUTH_KEY, ''), params=querystring)

result = json.loads(response.text)
print (result)

print("\n\nNEXT RUN: python ./code/model-state.py")
