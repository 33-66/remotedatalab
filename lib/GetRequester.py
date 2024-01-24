import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)  # Corrected the method name from ge to get
        return response.content

    def load_json(self):
        data = []
        info = json.loads(self.get_response_body())
        for each_info in info:
            data.append({"name": each_info["name"], "occupation": each_info["occupation"]})
        return data

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
print(get_requester.load_json())
# Output:
# [{'name': 'Daniel', 'occupation': 'LG Fridge Salesman'}, {'name': 'Joe', 'occupation': 'WiFi Fixer'}, {'name': 'Avi', 'occupation': 'DJ'}, {'name': 'Howard', 'occupation': 'Mountain Legend'}]
