from .abstract_election import AbstractElection
from .ballot import Ballot

class FirstPastThePost(AbstractElection):
    @staticmethod
    def run_election_round(ballots, votes):
        if len(votes) > 0:
            num_votes_max = votes.most_common(1)[0]
            victors = {k for (k,v) in votes.items() if v == num_votes}
            return victors
        else:
            return []
