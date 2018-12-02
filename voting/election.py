import collections
import random
import sys
from .ballot import Ballot

class Election:
    def __init__(self):
        self.votes = collections.Counter()
        self.ballots = {}

    def initialize_election(file_name):
        election_info = self.read_election_info(file_name)
        for ballot_info in election_info:
            new_ballot = Ballot(ballot_info.split())
            self.register_ballot(new_ballot)

    def run_election(self):
        while True:
            winner = self.run_election_round()
            if winner is not None:
                break

    def register_ballot(self, ballot):
        if not ballot.isexhausted():
            candidate = ballot.candidate()
            self.votes[candidate] += 1
            if candidate in self.ballots:
                self.ballots[candidate].append(ballot)
            else:
                self.ballots[candidate] = [ballot]

    def read_election_info(self, file_name):
        with open(file_name) as f:
            first_line = f.read_line()
            election_info = f.readlines()
            return election_info

    def run_election_round(self):
        print("Current state: " + str(self.votes))
        total_num_votes = sum(self.votes.values())
        num_votes_required = total_num_votes/2 + 1 # odd numbers will round down, which is OK
        leader = self.votes.most_common(1)[0]
        if leader[1] >= num_votes_required:
            print(leader[0] + " won!")
            return leader[0]
        else:
            self.eliminate_least_popular_candidate()
            return None

    def eliminate_least_popular_candidate(self):
        to_remove = self.least_popular_candidate()
        print("eliminating " + to_remove)
        ballots_to_remove = self.ballots[to_remove]
        for ballot in ballots_to_remove:
            ballot.failover()
            self.register_ballot(ballot)
        del self.ballots[to_remove]
        del self.votes[to_remove]

    # find the least popular candidate(s) and randomly select one
    def least_popular_candidate(self):
        lowest_votes = self.votes.most_common()[-1][1]
        least_popular_candidates = {k for (k,v) in self.votes.items() if v == lowest_votes}
        if len(least_popular_candidates) > 1:
            print("Least popular candidates: " + str(least_popular_candidates))
        return random.choice(tuple(least_popular_candidates))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 election.py path_to_file")
    else:
        file_path = sys.argv[1]
        elect = Election(file_path)
        winner = elect.run_election()
