from modules import reservations as reservations_module
def ask_guest_id():
    while True:
        guest_id = input("Enter guest ID number (CIN or passport): ").strip()
        if guest_id == "":
            print("[Error] ID number cannot be empty.")
            continue
        return guest_id
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
        cleaned = phone_text.replace("+","").replace(" ","")
        try:
            if cleaned.isdigit()==False:
                raise ValueError
            break
        except ValueError:
            print("[Error] Invalid phone number. Please enter digits only.")
            continue

    return name.strip(),phone_text.strip()


def view_guest_records(guest_names, guest_phones,guest_ids, booked_rooms, reservation_nights, reservation_costs):
    
    # Show every guest together with their booking info
    print("\n--- GUEST & BOOKING RECORDS ---")

    if len(guest_names) == 0:
        print("No reservations recorded yet.")
        return

    for i in range(len(guest_names)):
        name = guest_names[i]
        phone = guest_phones[i]
        guest_id = guest_ids[i]
        room = booked_rooms[i]
        nights = reservation_nights[i]
        cost = reservations_module.invoice_total(i)
        print("Guest:", name, "| Phone:", phone, guest_id, "---> Room:", room, "|", nights, "nights | Total:", cost, "DT")