class Venue:

    def __init__(self, name, till):
        self.name = name
        self.till = till

    # def add_guest_to_room(self, room, guest):
    #     if len(room.guests) < room.capacity and guest.money >= room.room_cost:
    #         room.guests.append(guest.name)
    #         guest.money -= room.room_cost  
    #         self.till += room.room_cost 
    #     else:
    #         return "Room full"

    def pay_bar_tab(self, room, bar):
        guest_remaining_money = "£" + str(bar.tab) + " bill paid for room " + str(room.room_number) + "; "
        if room.total_guest_money >= bar.tab:
            for person in room.guests:
                room.guest_money[person] = (room.guest_money[person] / room.total_guest_money) * (room.total_guest_money - bar.tab)
            room.total_guest_money -= bar.tab
            self.till += bar.tab
            for person in room.guests:
                guest_remaining_money += person + " has £" + str(room.guest_money[person]) + " remaining. "
            return guest_remaining_money
        return "Not enough money!"