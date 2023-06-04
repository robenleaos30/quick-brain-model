import requests

api_endpoint = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"
question_data = requests.get(api_endpoint).json()['results']