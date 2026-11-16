from modules import rooms as rooms_module
from modules import guests as guests_module
from modules import reservations as reservations_module
from modules import statistics as statistics_module

running = True

while running:
    print("\n=======================================")
    print("      HOTEL MANAGEMENT SYSTEM          ")
    print("=======================================")
    print("1. View Room Catalog & Status ")
    print("2. Make a Reservation")
    print("3. View Guest Records")
    print("4. Add Room to Maintenance")
    print("5. View Hotel Statistics")
    print("6. View reservations")
    print("7. Check-in")
    print("8. Check-out")
    print("9. Cancel a Reservation")
    print("10.Add a service")
    print("11.Record a Payment")
    print("12. Show Invoice")
    print("0. Exit")
    print("=======================================")

    choice_text = input("Enter your choice (0-12): ")

    if choice_text.isdigit() == False:
        print("\nInvalid input. Please enter a number from 0 to 12.")
        continue

    choice = int(choice_text)

    if choice == 1:
       rooms_module.view_catalog(reservations_module.booked_rooms, reservations_module.arrivals,
                                  reservations_module.departures, reservations_module.statuses)

    elif choice == 2:
        print("\n--- NEW RESERVATION ---")

        guest_id = guests_module.ask_guest_id()                              
        if guest_id in reservations_module.guest_ids:                        
            i = reservations_module.guest_ids.index(guest_id)
            guest_name = reservations_module.guest_names[i]
            guest_phone = reservations_module.guest_phones[i]
            print("Returning guest:", guest_name)
        else:
            guest_name, guest_phone = guests_module.get_guest_details()
        reservations_module.book_room(rooms_module.rooms, guest_name, guest_phone, guest_id)   
    elif choice == 3:
            guests_module.view_guest_records(                     
            reservations_module.guest_names, reservations_module.guest_phones, reservations_module.guest_ids,
            reservations_module.booked_rooms, reservations_module.reservation_nights,
            reservations_module.reservation_costs
        )
    elif choice == 4:
        rooms_module.add_maintenance(reservations_module.booked_rooms, reservations_module.arrivals,
                                     reservations_module.departures, reservations_module.statuses) 

    elif choice == 5:
        statistics_module.calculate_statistics(rooms_module.rooms)
    elif choice == 6:
         reservations_module.view_reservations()
    elif choice == 7:                                  
        reservations_module.check_in()

    elif choice == 8:                                 
        reservations_module.check_out()

    elif choice == 9:
        reservations_module.cancel_reservation()
    elif choice == 10:
        reservations_module.add_service()
    elif choice == 11:
        reservations_module.add_payment()
    elif choice == 12:
        reservations_module.show_invoice()
    elif choice == 0:                               
        print("\nExiting application. Goodbye!")
        running = False
    else:
        print("\n Invalid choice! Please enter a number between 0 and 12.")