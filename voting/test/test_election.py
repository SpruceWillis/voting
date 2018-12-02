import unittest
import voting
from voting import ballot, election

class TestElection(unittest.TestCase):
    def setUp(self):
        self.standard_election = 'election.txt'
        self.elect = election.Election()

    def test_election_info(self):
        with open(self.standard_election) as f:
            self.assertEqual(f.readlines(),
                 self.elect.read_election_info(self.standard_election))

    def test_register_ballot_bad(self):
        bad_ballot = ballot.Ballot()
        self.elect.register_ballot(bad_ballot)
        self.assertEqual(sum(self.elect.votes.values()), 0)
        self.assertEqual(len(self.elect.ballots), 0)

    def test_register_ballot_good(self):
        candidate = 'cat'
        good_ballot = ballot.Ballot([candidate])
        self.elect.register_ballot(good_ballot)
        num_votes = self.elect.votes[candidate]
        self.assertEqual(num_votes, 1)
        self.assertEqual(self.elect.ballots[candidate], [good_ballot])
