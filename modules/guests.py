def get_guest_details():
    # Ask the user for a valid guest's name
    while True:
        name = input("Enter guest full name: ")
        # Just check if the input is empty or just spaces
        if name.strip() == "":
            print("[Error] Name cannot be empty. Please enter a valid name.")
            continue
        break

    # Ask the user for a valid phone number using try...except
    while True:
        phone_text = input("Enter guest phone number: ")
        try:
            phone = int(phone_text)
            break
        except ValueError:
            print("[Error] Invalid phone number. Please enter digits only.")
            continue

    return name, str(phone)


def view_guest_records(guest_names, guest_phones, booked_rooms, reservation_nights, reservation_costs):
    # Show every guest together with their booking info
    print("\n--- GUEST & BOOKING RECORDS ---")

    if len(guest_names) == 0:
        print("No reservations recorded yet.")
        return

    for i in range(len(guest_names)):
        name = guest_names[i]
        phone = guest_phones[i]
        room = booked_rooms[i]
        nights = reservation_nights[i]
        cost = reservation_costs[i]
        print("Guest:", name, "| Phone:", phone, "---> Room:", room, "|", nights, "nights | Total:", cost, "DT")