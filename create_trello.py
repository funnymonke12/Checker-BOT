



def connect_trello():
    import requests
    import json

    apiKey = '0cfd11dfa4ca603b05a6e2791d7defbd'
    apiToken = 'ATTA84a62b8ba4a1f27b85e6ed6ccf51a5f1a22fd35d2177a3b7476d7be067fc0bd2B1E4724E'

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