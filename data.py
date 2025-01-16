import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

question_bank = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_bank.raise_for_status()
question_data = question_bank.json()["results"]

