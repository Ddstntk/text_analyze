from dataGetter import dataGetter
from matchPattern import matchPattern
from processText import processText

getter = dataGetter()
matcher = matchPattern()
processor = processText()

print(getter.getRules())
print(getter.getTexts())
print(getter.getGrades())

