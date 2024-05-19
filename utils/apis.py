import requests

def fox():
    url = 'https://randomfox.ca/floof/'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        image = data.get('image')
        return image