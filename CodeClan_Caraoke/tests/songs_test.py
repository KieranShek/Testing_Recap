import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Lady GaGa", "Poker Face")
        
    def test_guest_has_artist(self):
        self.assertEqual("Lady GaGa", self.song.artist)

    def test_guest_has_title(self):
        self.assertEqual("Poker Face", self.song.title)
    