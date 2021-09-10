import unittest
from src.venue import Venue
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar

class TestVenue(unittest.TestCase):
    
    def setUp(self):
        self.venue = Venue("CodeClan Caraoke", 1000.00)
        self.room = Room(3, 10, 5)
        self.room2 = Room(2, 1, 5)
        self.guest1 = Guest("Jack", 100, "fav_song")
        self.guest2 = Guest("John", 10, "fav_song")
        self.song1 = Song("Lady GaGa", "Poker Face")
        self.song2 = Song("Lady GaGa", "Just Dance")
        self.bar = Bar()
              
    def test_venue_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.venue.name)

    def test_venue_has_till(self):
        self.assertEqual(1000.00, self.venue.till)

### moved to room
    # def test_venue_can_add_to_room_guest_list(self):
    #     self.venue.add_guest_to_room(self.room, self.guest)
    #     self.assertEqual(['John'], self.room.guests)

    # def test_venue_can_add_to_room_guest_money(self):
    #     self.venue.add_guest_to_room(self.room, self.guest)
    #     self.assertEqual(6, self.guest.money)

    # def test_venue_can_add_to_room_till_cash(self):
    #     self.venue.add_guest_to_room(self.room, self.guest)
    #     self.assertEqual(1004, self.venue.till)
###
    def test_guests_can_pay_tab(self):
        self.room.check_guest_in(self.guest1, self.bar)
        self.room.check_guest_in(self.guest2, self.bar)
        self.guest1.buy_drink(self.bar, "Beer")
        self.guest2.buy_drink(self.bar, "Wine")
        self.assertEqual("£16.5 bill paid for room 3; Jack has £85.0 remaining. John has £8.5 remaining. ", self.venue.pay_bar_tab(self.room, self.bar))

    def test_guests_does_a_runner(self):
        self.room.check_guest_in(self.guest1, self.bar)
        self.room.check_guest_in(self.guest2, self.bar)
        self.room.check_guest_out(self.guest1)
        self.guest1.buy_drink(self.bar, "Beer")
        self.guest2.buy_drink(self.bar, "Wine")
        self.assertEqual("Not enough money!", self.venue.pay_bar_tab(self.room, self.bar))

    def test_guests_can_pay_tab_check_till(self):
        self.room.check_guest_in(self.guest1, self.bar)
        self.room.check_guest_in(self.guest2, self.bar)
        self.guest1.buy_drink(self.bar, "Beer")
        self.guest2.buy_drink(self.bar, "Wine")
        self.venue.pay_bar_tab(self.room, self.bar)
        self.assertEqual(1016.50, self.venue.till)
