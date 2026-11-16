from datetime import date
from modules import rooms as rooms_module
guest_names = []
guest_phones = []
booked_rooms = []
reservation_nights = []
reservation_costs = []
arrivals=[]
departures=[]
statuses = [] 
occupants_list = []
guest_ids = []  
cancellation_fees = []
service_totals = []
paid_amounts = []
discounts = []
nightly_prices = [] 
service_names = ["Breakfast", "Laundry", "Parking", "Airport transfer"]
service_prices = [15.0, 10.0, 8.0, 40.0] 
def invoice_total(i):
    if statuses[i] == "Cancelled":
        return cancellation_fees[i]                      
    return reservation_costs[i] + service_totals[i]
def balance(i):
    return invoice_total(i) - paid_amounts[i]
def book_room(rooms, guest_name, guest_phone,guest_id):
    while True:
        try:
            room_number = int(input("\nEnter room number to book (or type 0 to cancel): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if room_number == 0:
            print("Reservation cancelled.")
            return
        
        room_found = False
        for i in range(len(rooms)):
            number = rooms[i][0]
            category = rooms[i][1]
            capacity = rooms[i][2]
            price = rooms[i][3]


            if number == room_number:
                room_found = True

                while True:
                    arrival= rooms_module.ask_date("Arrival date (example: 2026-12-20):")
                    departure=rooms_module.ask_date("departure date:")
                    if arrival < date.today():
                        print("arrival time cant be in the past")
                        continue 
                    if departure<= arrival:
                        print("departure must be after arrival")
                        continue
                    break
                while True:                                                
                    try:
                        occupants = int(input("Number of occupants: "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
                    if occupants < 1 or occupants > capacity:
                        print(f"Occupants must be between 1 and {capacity} for this room.")
                        continue
                    break
                if rooms_module.is_room_free(room_number, arrival, departure, booked_rooms,arrivals, departures, statuses) == False:
                    print(f"\n Room {number} is not available for these dates. Please choose another.")
                    break
                while True:                                                 
                    try:
                        discount = float(input("Discount % (0 for none): "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
                    if discount < 0 or discount > 30:
                        print("[Error] The discount must be between 0 and 100.")
                        continue
                    break
                nights = (departure-arrival).days
                total_cost = price * nights * (1 - discount / 100)

                guest_names.append(guest_name)
                guest_phones.append(guest_phone)
                guest_ids.append(guest_id)
                booked_rooms.append(room_number)
                reservation_nights.append(nights)
                arrivals.append(arrival)
                departures.append(departure)
                reservation_costs.append(total_cost)
                statuses.append("Confirmed")
                occupants_list.append(occupants)
                cancellation_fees.append(0.0)
                service_totals.append(0.0)
                paid_amounts.append(0.0)
                discounts.append(discount)
                nightly_prices.append(price)
                print(f"\nSuccess! Room number {number} is booked for {guest_name}!")
                print(f"Total Cost for {nights} nights is {total_cost} DT.")
                return  
           

        if room_found == False:
            print("\nRoom does not exist. Please try again.")
def ask_reservation_index():
    if len(booked_rooms) == 0:
        print(" There are no reservations yet.")
        return -1
    while True:
        try:
            number = int(input("Reservation number (or type 0 to go back): "))
        except ValueError:
            print(" Please enter a valid number.")
            continue
        if number == 0:
            return -1
        if number < 1 or number > len(booked_rooms):
            print(" Reservation does not exist.")
            continue
        return number - 1


def view_reservations():
    print("\n--- RESERVATIONS ---")
    if len(booked_rooms) == 0:
        print("No reservations recorded yet.")
        return
    for i in range(len(booked_rooms)):
        print(f"{i + 1}. {guest_names[i]} | Room {booked_rooms[i]} | {arrivals[i]} -> {departures[i]} | {statuses[i]} | Balance: {balance(i)} DT")
def check_in():
    i = ask_reservation_index()
    if i == -1:
        return
    if statuses[i] != "Confirmed":
        print(" Only a Confirmed reservation can check in.")
        return
    if date.today() < arrivals[i]:
        print(f" Too early: the arrival date is {arrivals[i]}.")
        return
    statuses[i] = "Checked-in"
    print("Check-in done.")

def check_out():
    i = ask_reservation_index()
    if i == -1:
        return
    if statuses[i] != "Checked-in":
        print(" Check-out is only possible after check-in.")
        return
    if balance(i) > 0:
        print(f"WARNING: the guest still owes {balance(i)} DT.")
    statuses[i] = "Checked-out"
    print("Check-out done.")
def cancel_reservation():
        i = ask_reservation_index()
        if i == -1:
            return
        if statuses[i] != "Confirmed":                      
            print(" Only a Confirmed reservation can be cancelled.")
            return
        days_left = (arrivals[i] - date.today()).days
        fee = 0.0
        if days_left < 2:                                   
            fee = 0.2 * reservation_costs[i]               
        statuses[i] = "Cancelled"
        cancellation_fees[i] = fee
        print("Reservation cancelled. Cancellation fee:", fee, "DT")
        if paid_amounts[i] > fee:                             
            refund = paid_amounts[i] - fee
            paid_amounts[i] = paid_amounts[i] - refund
            print("Refund to the guest:", refund, "DT")
def add_service():
    i = ask_reservation_index()
    if i == -1:
        return
    if statuses[i] == "Cancelled" or statuses[i] == "Checked-out":
        print("Services can only be added to an active reservation.")
        return

    print("Services:")
    for k in range(len(service_names)):
        print(f"{k + 1}. {service_names[k]} - {service_prices[k]} DT")

    while True:
        try:
            service_choice = int(input("Service number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if service_choice < 1 or service_choice > len(service_names):
            print("This service does not exist.")
            continue
        break

    while True:
        try:
            quantity = int(input("Quantity: "))
        except ValueError:
            print(" Please enter a valid number.")
            continue
        if quantity < 1:                                 
            print(" Quantity must be at least 1.")
            continue
        break

    cost = service_prices[service_choice - 1] * quantity
    service_totals[i] = service_totals[i] + cost         
    print(f"{quantity} x {service_names[service_choice - 1]} added. Services total: {service_totals[i]} DT")
def add_payment():
    i = ask_reservation_index()
    if i == -1:
        return

    print("1. Deposit   2. Payment   3. Refund")
    while True:
        try:
            kind = int(input("Type (1-3): "))
        except ValueError:
            print("[Error] Please enter a valid number.")
            continue
        if kind < 1 or kind > 3:
            print("[Error] Choose 1, 2 or 3.")
            continue
        break

    while True:
        try:
            amount = float(input("Amount (DT): "))
        except ValueError:
            print("[Error] Please enter a valid number.")
            continue
        if amount <= 0:                                   
            print("[Error] The amount must be above 0.")
            continue
        break

    if kind == 3:                                         
        if amount > paid_amounts[i]:
            print("[Error] Refund is higher than the amount already paid.")
            return
        paid_amounts[i] = paid_amounts[i] - amount
    else:                                                
        if amount > balance(i):                           
            print(f"[Error] Payment is higher than the remaining balance ({balance(i)} DT).")
            return
        paid_amounts[i] = paid_amounts[i] + amount

    print("Payment recorded. Remaining balance:", balance(i), "DT")
def show_invoice():
    i = ask_reservation_index()
    if i == -1:
        return
    nights = (departures[i] - arrivals[i]).days
    print(f"\n--- INVOICE: reservation {i + 1} ({statuses[i]}) ---")
    print("Guest:", guest_names[i], "| ID:", guest_ids[i])
    print("Room:", booked_rooms[i], "|", arrivals[i], "->", departures[i], f"({nights} nights)")
    print(f"Accommodation: {nights} x {nightly_prices[i]} DT", end="")
    if discounts[i] > 0:
        print(f" - {discounts[i]}% discount", end="")
    print(" =", reservation_costs[i], "DT")
    print("Services:", service_totals[i], "DT")
    if statuses[i] == "Cancelled":
        print("Cancellation fee:", cancellation_fees[i], "DT")
    print("TOTAL:", invoice_total(i), "DT")
    print("Paid:", paid_amounts[i], "DT")
    print("BALANCE TO PAY:", balance(i), "DT")   