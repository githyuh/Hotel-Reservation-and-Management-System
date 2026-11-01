from modules import rooms as rooms_module
from modules import guests as guests_module
from modules import reservations as reservations_module
from modules import statistics as statistics_module

guest_names = []
guest_phones = []

booked_rooms = []
reservation_nights = []
reservation_costs = []


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
    print("6. Exit")
    print("=======================================")

    choice_text = input("Enter your choice (1-6): ")

    if choice_text.isdigit() == False:
        print("\n[Error] Invalid input. Please enter a number from 1 to 6.")
        continue

    choice = int(choice_text)

    if choice == 1:
        rooms_module.view_catalog()

    elif choice == 2:
        print("\n--- NEW RESERVATION ---")

        guest_name, guest_phone = guests_module.get_guest_details()

        reservations_module.book_room(
            rooms_module.rooms, guest_names, guest_phones, booked_rooms,
            reservation_nights, reservation_costs,
            guest_name, guest_phone
        )  

    elif choice == 3:
        guests_module.view_guest_records(
            guest_names, guest_phones, booked_rooms,
            reservation_nights, reservation_costs
        )

    elif choice == 4:
        rooms_module.add_maintenance()

    elif choice == 5:
        statistics_module.calculate_statistics(rooms_module.rooms, reservation_costs)

    elif choice == 6:
        print("\nExiting application. Goodbye!")
        running = False

    else:
        print("\n[Error] Invalid choice! Please enter a number between 1 and 6.")