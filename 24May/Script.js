async function reserveHall() {

    const hall_id =
        parseInt(document.getElementById("hallId").value);

    const user =
        document.getElementById("user").value;

    const start_hour =
        parseInt(document.getElementById("start").value);

    const end_hour =
        parseInt(document.getElementById("end").value);

    const response = await fetch("/reserve", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            hall_id,
            user,
            start_hour,
            end_hour
        })
    });

    const result = await response.json();

    document.getElementById("message").innerText =
        result.message;

    loadReservations();
}

async function recommendHall() {

    const attendees =
        document.getElementById("attendees").value;

    const response =
        await fetch(`/recommend/${attendees}`);

    const hall =
        await response.json();

    document.getElementById("recommendation").innerText =
        hall.name
            ? `${hall.name} (${hall.capacity} seats)`
            : "No hall available";
}

async function loadReservations() {

    const response =
        await fetch("/reservations");

    const reservations =
        await response.json();

    const list =
        document.getElementById("reservationList");

    list.innerHTML = "";

    reservations.forEach(r => {

        const li =
            document.createElement("li");

        li.textContent =
            `${r.user} booked Hall ${r.hall_id}
             from ${r.start_hour}:00
             to ${r.end_hour}:00`;

        list.appendChild(li);
    });
}

loadReservations();