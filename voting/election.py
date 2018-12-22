import collections
import argparse
import random
import sys
from ballot import Ballot
from first_past_the_post import FirstPastThePost
from instant_runoff_voting import InstantRunoffVoting

class Election:
    def __init__(self, electoral_system_type):
        self.electoral_system = Election.create_electoral_system(electoral_system_type)

    def initialize_election(self, file_name):
        election_info = self.read_election_info(file_name)
        for ballot_info in election_info:
            new_ballot = Ballot(ballot_info.split())
            self.electoral_system.register_ballot(new_ballot)

    def run_election(self):
        while True:
            winner = self.electoral_system.run_election_round()
            if winner is not None:
                break
        return winner

    def read_election_info(self, file_name):
        with open(file_name) as file:
            election_info = file.readlines()
            return election_info

    @staticmethod
    def create_electoral_system(system_type):
        try:
            type = {
                'fptp': FirstPastThePost,
                'irv': InstantRunoffVoting,
            }[system_type]
            return type()
        except KeyError as err:
            print("invalid electoral system" + system_type)

if __name__ == "__main__":
    usage = "usage: %prog [options] ballot_file"
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-m', '--method', metavar='method', choices=['irv', 'fptp'],
        default = 'fptp')
    parsed_args = parser.parse_args()
    elect = Election(parsed_args.method)
    elect.initialize_election(parsed_args.file)
    print(elect.run_election())
