import collections
import argparse
import random
import sys
from ballot import Ballot
from instant_runoff_voting import InstantRunoffVoting
from first_past_the_post import FirstPastThePost

class Election:
    def __init__(self, voting_method):
        self.votes = collections.Counter()
        self.ballots = {}
        self.voting_method = voting_method

    def initialize_election(self, file_name):
        election_info = self.read_election_info(file_name)
        for ballot_info in election_info:
            new_ballot = Ballot(ballot_info.split())
            self.register_ballot(new_ballot)

    def run_election(self):
        while True:
            winner = self.run_election_round()
            if winner is not None:
                break

    def read_election_info(self, file_name):
        with open(file_name) as file:
            first_line = file.readline()
            election_info = file.readlines()
            return election_info


if __name__ == "__main__":
    usage = "usage: %prog [options] ballot_file"
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-m', '--method', metavar='method', choices=['irv', 'fptp'],
        default = 'fptp')
    parsed_args = parser.parse_args()
    elect = Election(parsed_args.method)
    elect.initialize_election(parsed_args.file)
    elect.run_election()
