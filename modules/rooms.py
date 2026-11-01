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
        print(f"Room {room[0]} | Category: {room[1]} | Price: {room[2]} DT | Status: {room[3]}")
def add_maintenance():
    print("\n--- ROOM MAINTENANCE ---")
    try:
        m_room = int(input("Enter room number to put it under maintenance: "))
    except ValueError:
        print("[Error] Invalid room number.")
        return
    
    room_exists = False
    for i in range(len(rooms)):
        if rooms[i][0] == m_room:
            room_exists = True
            if rooms[i][4] == "Available":
                rooms[i] = (rooms[i][0], rooms[i][1], rooms[i][2], rooms[i][3], "Maintenance")
                maintenance_rooms.append(m_room)
                print(f"Room {m_room} is now under maintenance.")
            else:
                print(f"Room {m_room} is not available for maintenance.")
            return
    if not room_exists:
        print(f"Room {m_room} does not exist.")