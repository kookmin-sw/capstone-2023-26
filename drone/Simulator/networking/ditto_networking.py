import requests

class Networking:
    def __init__(self):
        pass

    def send_msg_to_server_with_params(self, url, params):
        response = requests.post(url, json=params)
        return response
    
    def is_alive(self, url):
        try:
            response = requests.get(url)
            return response.status_code == requests.codes.ok
        except requests.exceptions.RequestException as e:
            return False