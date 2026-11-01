def book_room(rooms, guest_names, guest_phones, booked_rooms, reservation_nights, reservation_costs, guest_name, guest_phone):
    while True:
        try:
            room_number = int(input("\nEnter room number to book (or type 0 to cancel): "))
        except ValueError:
            print("[Error] Please enter a valid number.")
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
            status = rooms[i][4]

            if number == room_number:
                room_found = True

                if status == "Available":
                    # Now it asks for nights only after verifying the room exists and is free!
                    try:
                        nights = int(input("Enter number of nights: "))
                    except ValueError:
                        print("[Error] Please enter a valid number for nights.")
                        continue

                    total_cost = price * nights
                    rooms[i] = (number, category, capacity, price, "Occupied")

                    guest_names.append(guest_name)
                    guest_phones.append(guest_phone)
                    booked_rooms.append(room_number)
                    reservation_nights.append(nights)
                    reservation_costs.append(total_cost)
                    
                    print(f"\nSuccess! Room number {number} is booked for {guest_name}!")
                    print(f"Total Cost for {nights} nights is {total_cost} DT.")
                    return  
                else:
                    print(f"\n[Error] Room {number} is already {status}. Please choose another.")
                    break 

        if room_found == False:
            print("\nRoom does not exist. Please try again.")