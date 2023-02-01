import requests, uuid, json
import pandas as pd
from tqdm import tqdm

# Add your subscription key and endpoint
subscription_key = ""
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "westus2"

path = '/translate'
constructed_url = endpoint + path

params_english2french = {
    'api-version': '3.0',
    'from': 'en',
    'to': 'fr'
}

params_french2English = {
	'api-version': '3.0',
	'from': 'fr',
	'to': 'en'
}

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

def main():
	
	pivoting_result = []

	df = pd.read_csv('data.csv')

	for idx,row in tqdm(df.iterrows()):
		sentence = row['javaDocFirstSentence']
		
		# First translation Step
		# I.E English2French
		body = [{
		    'text': sentence
		}]

		request = requests.post(constructed_url, params=params_english2french, headers=headers, json=body)
		response_first = request.json()

		#print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
		#############################################################################

		# Second translation Step
		# I.E French2English

		body = [{
		    'text': response_first[0]['translations'][0]["text"]
		}]

		request = requests.post(constructed_url, params=params_french2English, headers=headers, json=body)
		response_second = request.json()

		print("******************************")
		print("Starting from: {}".format(sentence))
		print("English 2 French: {}".format(response_first[0]['translations'][0]["text"]))
		print("French 2 English: {}".format(response_second[0]['translations'][0]['text']))
		print("******************************\n\n")

		pivoting_result.append(response_second[0]['translations'][0]['text'])

	df['pivoting'] = pivoting_result
	df.to_csv('final-data.csv')

if __name__ == "__main__":
	main()
