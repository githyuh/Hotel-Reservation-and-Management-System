def calculate_statistics(rooms_list, reservation_costs_list):
    total_rooms = len(rooms_list)
    if total_rooms == 0:
        print("No rooms in the system.")
        return
    occupied_count = 0
    current_revenue = 0.0  
    for room in rooms_list:
        if room[4] == "Occupied":
            occupied_count += 1
    for cost in reservation_costs_list:
        current_revenue += cost   
    occupancy_rate = (occupied_count / total_rooms) * 100

    print(
            f'''--- HOTEL STATISTICS ---
          Total Rooms in System: {total_rooms}
          Occupied Rooms: {occupied_count}
          Occupancy Rate: {occupancy_rate:.2f}%
          Total Revenue Generated: {current_revenue} DT''')