from config import apiKey, apiToken
def create_card():
    import requests
    url = 'https://api.trello.com/1/cards/'

    headers = {
      "Accept": "application/json"
    }

    query = {
      "name": "test_card",
      'idList': "64a45bac43cbeac0254867b4",
      'key': apiKey,
      'token': apiToken,
    }

    response = requests.request(
       "POST",
       url,
       headers=headers,
       params=query
    )

    print(response.text)