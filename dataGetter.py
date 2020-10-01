import json


class dataGetter():
    def getRules(self):
        with open("./static/categories.json", "r") as input_data:
            return json.loads(input_data.read())

    def getGrades(self):
        with open("./static/grades.json", "r") as input_data:
            return json.loads(input_data.read())

    def getTexts(self):
        with open("static/texts.txt", "r") as input_data:
            return input_data.read().split("!$**")
