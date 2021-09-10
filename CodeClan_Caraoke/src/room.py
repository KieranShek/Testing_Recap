class Room:

    def __init__(self, room_number, capacity, room_cost):
        self.room_number = room_number
        self.song_list = []
        self.guests = []
        self.capacity = capacity
        self.room_cost = room_cost
        self.total_guest_money = 0
        self.guest_money = {}

    def check_guest_in(self, guest, bar):
        if len(self.guests) < self.capacity and guest.money >= self.room_cost:
            self.guests.append(guest.name)
            self.guest_money[guest.name] = guest.money
            self.total_guest_money += guest.money 
            bar.tab += self.room_cost  
        return "Room full"

    def check_guest_out(self, guest):
        self.guests.remove(guest.name)
        del self.guest_money[guest.name]
        self.total_guest_money -= guest.money 

    def add_song_to_list(self, song):
        self.song_list.append(song.title)  

    # def pay_bar_tab(self, bar):
    #     guest_remaining_money = "£" + str(bar.tab) + " bill paid for room " + str(self.room_number) + "; "
    #     if self.total_guest_money >= bar.tab:
    #         for person in self.guests:
    #             self.guest_money[person] = (self.guest_money[person] / self.total_guest_money) * (self.total_guest_money - bar.tab)
    #         self.total_guest_money -= bar.tab
    #         for person in self.guests:
    #             guest_remaining_money += person + " has £" + str(self.guest_money[person]) + " remaining. "
    #         return guest_remaining_money
    #     return "Not enough money!"



