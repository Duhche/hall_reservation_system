from dataclasses import dataclass

# Hall model
@dataclass
class Hall:
    id: int
    name: str
    capacity: int


# Reservation model
@dataclass
class Reservation:
    hall_id: int
    user: str
    start_hour: int
    end_hour: int


# Sample halls
halls = [
    Hall(1, "Conference Hall", 100),
    Hall(2, "Meeting Room A", 20),
    Hall(3, "Meeting Room B", 15)
]

# Reservation storage
reservations = []


def has_conflict(hall_id, start_hour, end_hour):
    for reservation in reservations:

        if reservation.hall_id != hall_id:
            continue

        overlap = (
            reservation.start_hour < end_hour
            and reservation.end_hour > start_hour
        )

        if overlap:
            return True

    return False


def reserve_hall():

    hall_id = int(input("Hall ID: "))
    user = input("User: ")

    start = int(input("Start Hour: "))
    end = int(input("End Hour: "))

    if has_conflict(hall_id, start, end):
        print("Hall already booked.")
        return

    reservations.append(
        Reservation(
            hall_id,
            user,
            start,
            end
        )
    )

    print("Reservation created.")


def recommend_hall(attendees):

    suitable = [
        hall
        for hall in halls
        if hall.capacity >= attendees
    ]

    if not suitable:
        return None

    return min(
        suitable,
        key=lambda h: h.capacity
    )


# Test
hall = recommend_hall(18)
print("Recommended hall:", hall)

reserve_hall()

print("\nReservations:")
for reservation in reservations:
    print(reservation)