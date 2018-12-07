from .ballot import Ballot
from .abstract_election import AbstractElection

class InstantRunoffVoting(AbstractElection):
    # TODO: take the election as a parameter and use that one's methods. Also don't be an abstract class. Makes a lot more sense
    @classmethod
    def run_election_round(cls, ballots, votes)
        print("Current state: " + str(votes))
        total_num_votes = sum(votes.values())
        num_votes_required = total_num_votes/2 + 1 # odd numbers will round down, which is OK
        leader = votes.most_common(1)[0]
        if leader[1] >= num_votes_required: # there can be only one winner by this method
            print(leader[0] + " won!")
            return leader[0]
        else:
            cls.eliminate_least_popular_candidate(ballots, votes)
            return None
    @classmethod
    def eliminate_least_popular_candidate(cls, ballots, votes)
        to_remove = cls.least_popular_candidate(votes)
        print("eliminating " + to_remove)
        ballots_to_remove = ballots[to_remove]
        for ballot in ballots_to_remove:
            ballot.failover()
            cls.register_ballot(ballot, ballots, votes)
        del ballots[to_remove]
        del votes[to_remove]

    # find the least popular candidate(s) and randomly select one
    @classmethod
    def least_popular_candidate(cls, votes):
        lowest_votes = votes.most_common()[-1][1]
        least_popular_candidates = {k for (k,v) in votes.items() if v == lowest_votes}
        if len(least_popular_candidates) > 1:
            print("Least popular candidates: " + str(least_popular_candidates))
        return random.choice(tuple(least_popular_candidates))

    @classmethod
    def register_ballot(cls, ballot, ballots, votes):
        if not ballot.isexhausted():
            candidate = ballot.candidate()
            votes[candidate] += 1
            if candidate in ballots:
                ballots[candidate].append(ballot)
            else:
                ballots[candidate] = [ballot]

