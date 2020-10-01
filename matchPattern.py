class matchPattern():
    def basicMatch(self, text, pattern):
        matches = set([])
        for category in pattern:
            for value in category:
                if value in text:
                    matches.add(category)

    def complexMatch(self):
        pass


