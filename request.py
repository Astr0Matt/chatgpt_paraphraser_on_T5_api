import requests
import json

API_URL = "http://127.0.0.1:5000/paraphrase"

def get_paraphrase(prompt):
    payload = {"prompt": prompt}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(API_URL, data=json.dumps(payload), headers=headers)
    print(response.json()["result"][0])

    if response.status_code == 200:
        return response.json()["result"]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == "__main__":
    sentence = "I am an hardware architect who try to imrpove architects work with ai"
    
    paraphrased = get_paraphrase(sentence)
    if paraphrased:
        print(f"Original: {sentence}")
    #print(paraphrased[1])
    print()
    i = 0
    for parphrase in paraphrased:
        print(f"Paraphrase {i} : {parphrase}")
        i+=1
