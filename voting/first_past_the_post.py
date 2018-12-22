from electoral_system import ElectoralSystem
from ballot import Ballot

class FirstPastThePost(ElectoralSystem):
    def run_election_round(self):
        if len(self.votes) > 0:
            num_votes_max = self.votes.most_common(1)[0][1]
            victors = {k for (k,v) in self.votes.items() if v == num_votes_max}
            return victors
        else:
            return None
