import unittest
import voting
from voting import ballot

class TestBallot(unittest.TestCase):
    def test_isexhausted_no(self):
        good_ballot = ballot.Ballot(['blah'])
        self.assertEqual(good_ballot.isexhausted(), False)

    def test_isexhausted_yes(self):
        bad_ballot = ballot.Ballot()
        self.assertEqual(bad_ballot.isexhausted(), True)

    def test_candidate_ok(self):
        vote1 = 'Obama'
        vote2 = 'Romney'
        candidates = [vote1, vote2]
        good_ballot = ballot.Ballot(candidates)
        self.assertEqual(good_ballot.candidate(), vote1)

    def test_candidate_bad(self):
        bad_ballot = ballot.Ballot()
        self.assertEqual(bad_ballot.candidate(), None)

    def test_failover_multiple(self):
        vote1 = 'Obama'
        vote2 = 'Romney'
        candidates = [vote1, vote2]
        good_ballot = ballot.Ballot(candidates)
        good_ballot.failover()
        self.assertEqual(good_ballot.candidate(), vote2)

    def test_failover_single(self):
        bare_ballot = ballot.Ballot(['cat'])
        bare_ballot.failover()
        self.assertEqual(bare_ballot.candidate(), None)
