from config import apiKey, apiToken, email, password
import requests
import json

session = requests.Session()
def auth():
    headers = {'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}

    data = {
            'email': email,  # Email
            'password': password  # Пароль
            }
    url = 'https://trello.com/b/XCkISB86/%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%B0%D1%8F-%D0%B4%D0%BE%D1%81%D0%BA%D0%B0'


def get_listID():
    auth()
    url = 'https://trello.com/b/XCkISB86/%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%B0%D1%8F-%D0%B4%D0%BE%D1%81%D0%BA%D0%B0.json' # Ссылка на доску
    response = requests.get(url)
    data = json.loads(response.text)
    lists = data['lists']
    listID = lists[0]["id"]
    return listID

def create_card(listID):
    import requests
    url = 'https://api.trello.com/1/cards/'

    headers = {
      "Accept": "application/json"
    }

    query = {
      "name": "test_card",
      'idList': listID,
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


