# main.py

import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Ensure the response is returned in bytes

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body.decode('utf-8'))  # Decode bytes to string and parse as JSON

if __name__ == "__main__":
    # Example usage
    url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
    get_requester = GetRequester(url)
    data = get_requester.load_json()
    print(data)




