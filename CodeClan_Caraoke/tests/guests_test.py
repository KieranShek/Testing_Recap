import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room
# from src.venue import Venue

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Frodo", 10.00, "Poker Face")
        self.guest1 = Guest("Same", 10.00, "Just Dance")
        self.room = Room(4, 3, 3)
        self.song1 = Song("Lady GaGa", "Poker Face")
        self.song2 = Song("Lady GaGa", "Just Dance")
        
    def test_guest_has_name(self):
        self.assertEqual("Frodo", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(10.00, self.guest.money)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Poker Face", self.guest.favourite_song)

    def test_fav_song_in_song_list(self):
        self.room.add_song_to_list(self.song1)
        self.room.add_song_to_list(self.song2)
        self.assertEqual("Whoo", self.guest.cheer_for_song(self.room.song_list))