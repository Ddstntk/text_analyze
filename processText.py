import re


class processText():
    def basicize(self, text):
        pass

    def alphaAndLower(self, text):
        regex = re.compile('[^a-zA-Z \.]')
        return regex.sub('', text)
