import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_search_player(self):
        self.assertEqual(self.stats.search("Gretzky").name, "Gretzky")
    
    def test_search_nonexistent_player(self):
        self.assertEqual(self.stats.search("Pelaaja"), None)

    def test_team_players(self):
        self.assertEqual(self.stats.team("PIT")[0].name, "Lemieux")

    def test_top_amout(self):
        self.assertEqual(len(self.stats.top(4)), 5)

    def test_top_sorted_by_points(self):
        top3 = self.stats.top(3)
        self.assertLessEqual(top3[2].points, top3[1].points)
    
    def test_top_player(self):
        self.assertEqual(self.stats.top(1)[0].name, "Gretzky")
