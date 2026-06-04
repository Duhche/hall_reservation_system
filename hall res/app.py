from flask import Flask, render_template
from flask import request, jsonify

from dataclasses import dataclass, asdict

app = Flask(__name__)


@dataclass
class Hall:
    id: int
    name: str
    capacity: int


@dataclass
class Reservation:
    hall_id: int
    user: str
    start_hour: int
    end_hour: int


halls = [
    Hall(1, "Conference Hall", 100),
    Hall(2, "Meeting Room A", 20),
    Hall(3, "Meeting Room B", 15)
]

reservations = []


def has_conflict(hall_id, start_hour, end_hour):

    for reservation in reservations:

        if reservation.hall_id != hall_id:
            continue

        if (
            reservation.start_hour < end_hour
            and reservation.end_hour > start_hour
        ):
            return True

    return False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/reserve", methods=["POST"])
def reserve():

    data = request.json

    if has_conflict(
        data["hall_id"],
        data["start_hour"],
        data["end_hour"]
    ):
        return jsonify({
            "message":
            "Hall already booked."
        })

    reservations.append(
        Reservation(**data)
    )

    return jsonify({
        "message":
        "Reservation created."
    })


@app.route("/reservations")
def get_reservations():

    return jsonify([
        asdict(r)
        for r in reservations
    ])


@app.route("/recommend/<int:attendees>")
def recommend(attendees):

    suitable = [
        hall
        for hall in halls
        if hall.capacity >= attendees
    ]

    if not suitable:
        return jsonify({})

    hall = min(
        suitable,
        key=lambda h: h.capacity
    )

    return jsonify(asdict(hall))


if __name__ == "__main__":
    app.run(debug=True)