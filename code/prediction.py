import requests, os, sys, json, numpy, operator, itertools

model_id = "c0c3c611-dc87-4576-bb11-53a265d55a60" # you own model id
AUTH_KEY = "V1_-CV8arzT-DTTH2cu6d0DhThUQ1y-l" # your api key


dir = "images/test/Observation_1"
images_per_observation=35
obs_1=[]
for x in range(1,images_per_observation+1):
	image_path = dir + "/" + str(x) + ".png"
	BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
	url = BASE_URL + 'LabelFile/'
	data = {'file': open(image_path, 'rb'),    'modelId': ('', model_id)}

	response = requests.post(url, auth=requests.auth.HTTPBasicAuth(AUTH_KEY, ''), files=data)
	result = json.loads(response.text)['result'][0]['prediction']

	probabilities = [result_dict['probability'] for result_dict in result]
	best_index = numpy.argmax(probabilities)
	best_label = result[best_index]['label']
	obs_1.append((x,int(best_label)))
	#print('The predicted label for '+ str(x) +' is: ' + str(best_label))
obs_1.sort(key=operator.itemgetter(1))
#print(obs_1)


dir = "images/test/Observation_2"
images_per_observation=35
obs_2=[]
for x in range(1,images_per_observation+1):
	image_path = dir + "/" + str(x) + ".png"
	BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
	url = BASE_URL + 'LabelFile/'
	data = {'file': open(image_path, 'rb'),    'modelId': ('', model_id)}

	response = requests.post(url, auth=requests.auth.HTTPBasicAuth(AUTH_KEY, ''), files=data)
	result = json.loads(response.text)['result'][0]['prediction']

	probabilities = [result_dict['probability'] for result_dict in result]
	best_index = numpy.argmax(probabilities)
	best_label = result[best_index]['label']
	obs_2.append((x,int(best_label)))
	#print('The predicted label for '+ str(x) +' is: ' + str(best_label))
obs_2.sort(key=operator.itemgetter(1))
#print(obs_2)

for x,y in zip(obs_1,obs_2):
	print(x[0]," ",y[0])
