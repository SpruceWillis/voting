from electoral_system import ElectoralSystem
from ballot import Ballot

class FirstPastThePost(ElectoralSystem):
    def run_election_round(self):
        if len(self.votes) > 0:
            num_votes_max = self.votes.most_common(1)[0][1]
            victors = {k for (k,v) in self.votes.items() if v == num_votes_max}
            if len(victors) > 1:
                print("Multiple winners detected, breaking ties between " + ', '.join(list(victors)))
            # this is a hack to get the key out of the set even if there's only one winner
            return self.tiebreak(victors)
        else:
            return "No winner"
