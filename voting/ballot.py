class Ballot:
    def __init__(self, candidates = []):
        self.candidates = candidates
        self.candidates.reverse()

    def candidate(self):
        if self.isexhausted():
            return None
        else:
            return self.candidates[-1]

    def failover(self):
            self.candidates.pop()

    def isexhausted(self):
        return not self.candidates
