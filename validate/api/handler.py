import json
import logging

def validate_handler(event, context):
    data = json.loads(event['body'])
    wordsToReplace = {
        "Oracle": "Oracle©",
        "Google": "Google©",
        "Amazon": "Amazon©", 
        "Microsoft" : "Amazon©",
        "Deloitte": "Deloitte©"
    }
    
    if 'sentence' not in data:
        logging.error("Request does not contain `sentence`.")
        return {"statusCode": 500, "body": "Request does not contain `sentence`."}
        
    newSentence = data['sentence']

    if not newSentence:
        logging.error("Request `sentence` does not contain any value.")
        return {"statusCode": 500, "body": "Request `sentence` does not contain any value."}

    for key, value in wordsToReplace.items():
        newSentence = newSentence.replace(key, value)

    return {"statusCode": 200, "body": newSentence}