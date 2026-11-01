def get_guest_details():
    # Ask the user for a guest's name and phone number
    name = input("Enter guest full name: ")
    phone = input("Enter guest phone number: ")
    return name, phone


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