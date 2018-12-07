import abc
from abc import ABC

class AbstractElection(ABC):
    # this method should run a single round of an election
    # it should return None if there is no winner in that round
    # otherwise it should return an array of winner(s)
    @classmethod
    @abc.abstractmethod
    def run_election_round(cls, ballots, votes):
        pass
