import abc
from abc import ABC
import collections

class ElectoralSystem(ABC):
    # this method should run a single round of an election
    # it should return None if there is no winner in that round
    # otherwise it should return an array of winner(s)
    def __init__(self):
        self.votes = collections.Counter()
        self.ballots = {}

    def count_ballot_for_candidate(self, candidate, ballot):
        if candidate:
            self.votes[candidate] += 1
            if candidate in self.ballots:
                self.ballots[candidate].add(ballot)
            else:
                self.ballots[candidate] = {ballot}

    # TODO: implement different ways of choosing if there are ties
    def least_popular_candidate(self):
        least_popular_candidates = self.least_popular_candidates()
        return random.choice(tuple(least_popular_candidates))

    # find the least popular candidate(s) and randomly select one
    def least_popular_candidates(self):
        lowest_votes = self.votes.most_common()[-1][1]
        least_popular_candidates = {k for (k,v) in self.votes.items() if v == lowest_votes}
        if len(least_popular_candidates) > 1:
            print("Least popular candidates: " + str(least_popular_candidates))
        return least_popular_candidates

    def register_ballot(self, ballot):
        candidate = ballot.candidate()
        self.count_ballot_for_candidate(candidate, ballot)

    def remove_candidate(self, candidate):
        del self.ballots[candidate]
        del self.votes[candidate]

    @abc.abstractmethod
    def run_election_round(self):
        pass
