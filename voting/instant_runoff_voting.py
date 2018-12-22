from ballot import Ballot
from electoral_system import ElectoralSystem

class InstantRunoffVoting(ElectoralSystem):
    # TODO: take the election as a parameter and use that one's methods. Also don't be an abstract class. Makes a lot more sense
    def run_election_round(self):
        print("Current state: " + str(self.votes))
        total_num_votes = sum(self.votes.values())
        num_votes_required = total_num_votes/2 + 1 # odd numbers will round down, which is OK
        leader = self.votes.most_common(1)[0]
        if leader[1] >= num_votes_required: # there can be only one winner by this method
            print(leader[0] + " won!")
            return leader[0]
        else:
            self.eliminate_least_popular_candidate()
            return None

    def eliminate_least_popular_candidate(self):
        to_remove = self.least_popular_candidate()
        print("eliminating " + to_remove)
        ballots_to_remove = self.ballots[to_remove]
        self.remove_candidate(to_remove)
        for ballot in ballots_to_remove:
            self.register_ballot(ballot)
