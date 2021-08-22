import requests


class DataProcess:
    def __init__(self, **kwargs):
        self.question_data = []
        self.response_code = 0
        self.id = 0
        self.amount = kwargs["amount"]
        self.category = kwargs["category"]
        self.difficulty = kwargs["difficulty"]

    def loading_quiz(self):
        self.category = self.load_category()
        
        params = {
            "amount": self.amount,
            "type": "boolean",
            "category": self.category,
            "difficulty": self.difficulty
        }

        request = requests.get(url="https://opentdb.com/api.php", params=params)
        request.raise_for_status()
        self.question_data = request.json()["results"]
        self.response_code = request.json()["response_code"]
        return self.question_data, self.response_code

    def load_category(self):
        request = requests.get(url="https://opentdb.com/api_category.php")
        request.raise_for_status()
        category_data = request.json()["trivia_categories"]

        for category in category_data:

            if self.category in category["name"]:
                self.id = category["id"]
                break
        return self.id
