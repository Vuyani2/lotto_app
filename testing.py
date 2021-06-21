import unittest
from LogIns import player_id, Player
import datetime


class TestLogins(unittest.TestCase):
    def test_player_id(self):
        #self.assertTrue(player_id.player_id(), "Player id not created")
        self.assertEqual(player_id("Vuyani Kunelisi", "0003195216084"), "KV5216", 'pLAYER ID NOT CREATED')

    def test_player_instance(self):
        instance = Player("Vuyani Kunelisi", "vuyanikunelisi@gmail.com", "0003195216084", "KV5216", datetime.date.today())
        self.assertEqual(instance.email, "vuyanikunelisi@gmail.com", "Instance not created succesfully")



