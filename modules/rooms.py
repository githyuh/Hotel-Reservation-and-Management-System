rooms = [
    (101, "Standard", 2, 100.0, "Available"),
    (202, "Standard", 2, 120.0, "Available"),
    (303, "Deluxe", 3, 180.0, "Available"),
    (404, "Suite", 4, 250.0, "Available")
]
maintenance_rooms = []
def view_catalog():
    print("--- ROOM CATALOG ---")
    for room in rooms:
        print(f"Room {room[0]} | Category: {room[1]} |Capacity: {room[2]} | Price: {room[3]} DT | Status: {room[4]}")
def add_maintenance():
    while True:
        try:
            room_number = int(input("\nEnter room number to put under maintenance (or type 0 to cancel): "))
        except ValueError:
            print("[Error] Please enter a valid number.")
            continue
            
        if room_number == 0:
            print("Maintenance action cancelled.")
            return

        room_found = False
        for i in range(len(rooms)):
            number = rooms[i][0]
            category = rooms[i][1]
            capacity = rooms[i][2]
            price = rooms[i][3]
            status = rooms[i][4]

            if number == room_number:
                room_found = True
                if status == "Available":
                    rooms[i] = (number, category, capacity, price, "Maintenance")
                    print(f"\nSuccess! Room number {number} is now under Maintenance.")
                    return 
                else:
                    print(f"\n[Error] Room {number} cannot be put in maintenance because it is currently {status}. Please choose another.")
        if room_found == False:
            print(f"\n[Error] Room does not exist. Please try again.")