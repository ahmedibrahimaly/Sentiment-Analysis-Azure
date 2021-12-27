import requests as req

headers = {
    "Ocp-Apim-Subscription-Key":"<subscription-key>",
    "Content-Type": "application/json",
    "Accept": "application/json"
			}

endpoint = 'keyPhrases'
body = {
    "documents": [
        {
            "language": "en",
            "id": "1",
            "text": "Great atmosphere. Close to plenty of restaurants, hotels, and transit! Staff are friendly and helpful."
        },
        {
            "language": "en",
            "id": "2",
            "text": "Bad atmosphere. Not close to plenty of restaurants, hotels, and transit! Staff are not friendly and helpful."

        },
		
		{
            "language": "en",
            "id": "3",
            "text": "Good morning. I love you :)"

        }
    ]
}


response = req.post("<endpoint>//text/analytics/v3.0/" + endpoint, headers=headers, json=body)
result = response.json()
keyPhrases = result["documents"]
for i in range(len(keyPhrases)):
    document_level_keyphrases = keyPhrases[i]["keyPhrases"]
    print("Document {}: KeyPhrases: {}".format(i+1, document_level_keyphrases))