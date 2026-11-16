from datetime import date
def ask_date(text):
    while True:
        try:
            return date.fromisoformat(input(text).strip())
        except ValueError:
            print("enter a valid date (example: 2026-12-20)")
rooms = [
    (101, "Standard", 2, 100.0),
    (202, "Standard", 2, 120.0),
    (303, "Deluxe", 3, 180.0),
    (404, "Suite", 4, 250.0)
]
maintenance_rooms = []
maintenance_starts = []  
maintenance_ends = []
def overlaps(arrival1, departure1, arrival2, departure2):
    return arrival1 < departure2 and departure1 > arrival2
def is_room_free(room_number, arrival, departure, booked_rooms, arrivals, departures, statuses):
    for i in range(len(maintenance_rooms)):                                 
        if maintenance_rooms[i] == room_number:
            if overlaps(arrival, departure, maintenance_starts[i], maintenance_ends[i]):
                return False
    for i in range(len(booked_rooms)):
        if booked_rooms[i] == room_number:
            if statuses[i] == "Confirmed" or statuses[i] == "Checked-in":
                if overlaps(arrival, departure, arrivals[i], departures[i]):
                    return False
    return True
def room_state(room_number, day, booked_rooms, arrivals, departures, statuses):
    for i in range(len(maintenance_rooms)):                                 
        if maintenance_rooms[i] == room_number:
            if maintenance_starts[i] <= day < maintenance_ends[i]:
                return "Maintenance"
    for i in range(len(booked_rooms)):
        if booked_rooms[i] == room_number:
            if statuses[i] == "Confirmed" or statuses[i] == "Checked-in":
                if arrivals[i] <= day < departures[i]:
                    if statuses[i] == "Checked-in":
                        return "Occupied"
                    return "Reserved"
    return "Available"
def view_catalog(booked_rooms, arrivals, departures, statuses):
    print("--- ROOM CATALOG (today)---")
    for room in rooms:
        state = room_state(room[0], date.today(), booked_rooms, arrivals, departures, statuses)
        print(f"Room {room[0]} | Category: {room[1]} |Capacity: {room[2]} | Price: {room[3]} DT | Status: {state}")
def add_maintenance(booked_rooms, arrivals, departures, statuses):
    while True:
        try:
            room_number = int(input("\nEnter room number to put under maintenance (or type 0 to cancel): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if room_number == 0:
            print("Maintenance action cancelled.")
            return

        room_found = False
        for room in rooms:                                            
            if room[0] == room_number:
                room_found = True
        if room_found == False:
            print(f"Room does not exist. Please try again.")
            continue
        print(f"Room {room_number} is already blocked on these dates:")      
        blocked = False
        for i in range(len(maintenance_rooms)):
            if maintenance_rooms[i] == room_number:
                print(f"   Maintenance: {maintenance_starts[i]} -> {maintenance_ends[i]}")
                blocked = True
        for i in range(len(booked_rooms)):
            if booked_rooms[i] == room_number:
                if statuses[i] == "Confirmed" or statuses[i] == "Checked-in":
                    print(f"   Reservation {i + 1}: {arrivals[i]} -> {departures[i]}")
                    blocked = True
        if blocked == False:
            print("none")
        start = ask_date("Maintenance start (example: 2026-12-20): ")          
        end = ask_date("Maintenance end : ")              
        if end <= start:                                             
            print("The end date must be after the start date.")
            continue
        if is_room_free(room_number, start, end, booked_rooms, arrivals, departures, statuses) == False:
            print("The room has a reservation or maintenance in this period.")
            continue

        maintenance_rooms.append(room_number)                         
        maintenance_starts.append(start)                              
        maintenance_ends.append(end)                                 
        print(f"Success! Room number {room_number} is under Maintenance from {start} to {end}.")
        return