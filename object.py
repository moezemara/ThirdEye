import requests
import urllib
import json
import config

def run():

	url = "http://"+config.camurl+":8080/shot.jpg"
	output_file=open(config.localfile,'w')

	urllib.request.urlretrieve(url, config.image)

	url = config.modelurl

	data = {'file': open(config.image, 'rb')}

	response = requests.post(url, auth=requests.auth.HTTPBasicAuth(config.nanonetskey, ''), files=data)

	json_resp = (json.loads(response.text))

	#print(response.text)
#	print('============================================')
	print(json.dumps(json_resp, indent=4,sort_keys=True))
	print('============================================')
	result_list = json_resp['result']
	first_item = result_list[0]
	prediction_item = first_item['prediction']
	index = 0
	labels_array = []
	while(index<len(prediction_item)):
		first_prediction_item = prediction_item[index]
		final_label = first_prediction_item['label']
		labels_array.append(final_label[3:])
		index += 1
	print(*labels_array, sep = ", ")

	labels_array_index = 0
	comma = ", "
	labels_array_count = len(labels_array)

	while(labels_array_index<labels_array_count):
		output_file.writelines(labels_array[labels_array_index])
		if(labels_array_index < labels_array_count - 1):
			output_file.writelines(comma)
		labels_array_index += 1
	output_file.close()