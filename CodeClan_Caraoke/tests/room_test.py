import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room(3, 10, 5)
        self.room2 = Room(2, 1, 5)
        self.guest1 = Guest("Jack", 100, "fav_song")
        self.guest2 = Guest("John", 10, "fav_song")
        self.song1 = Song("Lady GaGa", "Poker Face")
        self.song2 = Song("Lady GaGa", "Just Dance")
        self.bar = Bar()
              
    def test_venue_has_name(self):
        self.assertEqual(3, self.room.room_number)

    def test_venue_has_till(self):
        self.assertEqual(10, self.room.capacity)

    def test_room_can_add_guest(self):
        self.room.check_guest_in(self.guest1, self.bar)
        self.room.check_guest_in(self.guest2, self.bar)
        self.assertEqual(["Jack", "John"], self.room.guests)
    
    def test_room_can_remove_guest(self):
        self.room.check_guest_in(self.guest1, self.bar)
        self.room.check_guest_in(self.guest2, self.bar)
        self.room.check_guest_out(self.guest2)
        self.assertEqual(["Jack"], self.room.guests)

    def test_room_can_add_songs(self):
        self.room.add_song_to_list(self.song1)
        self.room.add_song_to_list(self.song2)
        self.assertEqual(['Poker Face', 'Just Dance'], self.room.song_list)

    def test_room_full_capacity(self):
        self.room.check_guest_in(self.guest1, self.bar)       
        self.assertEqual("Room full", self.room.check_guest_in(self.guest2, self.bar))
        
    # def test_guests_can_pay_tab(self):
    #     self.room.check_guest_in(self.guest1, self.bar)
    #     self.room.check_guest_in(self.guest2, self.bar)
    #     self.guest1.buy_drink(self.bar, "Beer")
    #     self.guest2.buy_drink(self.bar, "Wine")
    #     self.assertEqual("£16.5 bill paid for room 3; Jack has £85.0 remaining. John has £8.5 remaining. ", self.room.pay_bar_tab(self.bar))
    
    # def test_guests_does_a_runner(self):
    #     self.room.check_guest_in(self.guest1, self.bar)
    #     self.room.check_guest_in(self.guest2, self.bar)
    #     self.room.check_guest_out(self.guest1)
    #     self.guest1.buy_drink(self.bar, "Beer")
    #     self.guest2.buy_drink(self.bar, "Wine")
    #     self.assertEqual("Not enough money!", self.room.pay_bar_tab(self.bar))