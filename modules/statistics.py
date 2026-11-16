from datetime import timedelta
from modules import rooms as rooms_module
from modules import reservations as reservations_module
def calculate_statistics(rooms_list):
    r = reservations_module
    total_rooms = len(rooms_list)
    if total_rooms == 0:
        print("No rooms in the system.")
        return
    start = rooms_module.ask_date("Period start (example: 2026-12-20): ")
    end = rooms_module.ask_date("Period end : ")
    if end < start:
        print("The end date cannot be before the start date.")
        return
    reservation_count = 0
    occupied_nights = 0
    accommodation_revenue = 0.0
    services_revenue = 0.0
    cancelled_count = 0
    fees = 0.0
    standard_count = 0
    deluxe_count = 0
    suite_count = 0
    for i in range(len(r.booked_rooms)):
        if start <= r.arrivals[i] <= end:
            reservation_count += 1
            if r.statuses[i] == "Cancelled":                       
                cancelled_count += 1
                fees += r.cancellation_fees[i]
            else:
                accommodation_revenue += r.reservation_costs[i]   
                services_revenue += r.service_totals[i]
                for room in rooms_list:                           
                    if room[0] == r.booked_rooms[i]:
                        if room[1] == "Standard":
                            standard_count += 1
                        elif room[1] == "Deluxe":
                            deluxe_count += 1
                        elif room[1] == "Suite":
                            suite_count += 1

        if r.statuses[i] != "Cancelled":
            first = max(r.arrivals[i], start)
            last = min(r.departures[i], end + timedelta(days=1))
            nights_inside = (last - first).days
            if nights_inside > 0:
                occupied_nights += nights_inside

    days = (end - start).days + 1
    occupancy_rate = (occupied_nights / (total_rooms * days)) * 100

    print(
    f'''--- HOTEL STATISTICS ---
    Total Rooms in System: {total_rooms}
    Reservations in the period: {reservation_count}
    Occupancy Rate: {occupancy_rate:.2f}%
    Accommodation revenue: {accommodation_revenue} DT
    Services revenue: {services_revenue} DT
    Cancelled reservations: {cancelled_count} | Cancellation fees: {fees} DT
    Reservations by category:
    Standard: {standard_count} | Deluxe: {deluxe_count} | Suite: {suite_count}''')
    print("Guests with an unpaid balance:") 
    found = False
    for i in range(len(r.booked_rooms)):
        if r.statuses[i] == "Checked-out" or r.statuses[i] == "Cancelled":
            if r.balance(i) > 0:
                print(f"   {r.guest_names[i]} | reservation {i + 1} | {r.balance(i)} DT")
                found = True
    if found == False:
        print("nobody")