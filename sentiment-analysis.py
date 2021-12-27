import requests as req

headers = {
    "Ocp-Apim-Subscription-Key":"<subscription-key>",
    "Content-Type": "application/json",
    "Accept": "application/json"
			}

endpoint = 'sentiment'
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
            "text": "Fuck you. Are you fool"

        }
    ]
}


response = req.post("<endpoint>//text/analytics/v3.0/" + endpoint, headers=headers, json=body)
result = response.json()
sentiment = result["documents"]
for i in range(len(sentiment)):
    print("Document {0}: Sentiment: {1} ".format(i + 1, sentiment[i]["sentiment"]))

#print("Sentence Level Sentiment\n")
#for i in range(len(sentiment)):
 #   for j in range(len(sentiment[i]["sentences"])):
  #      print("Document {0}: Sentence {1}: {2} -> Sentiment: {3} ".format(i + 1, j + 1, 
   #            sentiment[i]["sentences"][j]["text"], sentiment[i]["sentences"][j]["sentiment"]))