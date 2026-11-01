def book_room(rooms,guest_names,guest_phones,booked_rooms,reservation_nights,reservation_costs,guest_name,guest_phone,room_number,nights):
	room_found = False
	for i in range(len(rooms)):
		number= rooms[i][0]
		category = rooms[i][1]
		price = rooms[i][2]
		status = rooms[i][3]

		if number == room_number:
			room_found = True

			if status == "Available":
				total_cost = price * nights

				rooms[i]=(number,category,price,"Occupied")

				guest_names.append(guest_name)
				guest_phones.append(guest_phone)
				booked_rooms.append(room_number)
				reservation_nights.append(nights)
				reservation_costs.append(total_cost)
				print("\nSuccesss! Room number",number,"is booked for",guest_name, "!")
				print("Total Cost for",nights,"is",total_cost,"DT.")
			else:
				print("\nRoom is already Occupied.")

	if room_found == False :
		print("\nRoom does not exist.")
