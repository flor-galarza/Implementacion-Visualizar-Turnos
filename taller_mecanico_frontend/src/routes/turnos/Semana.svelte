<script>
  import { onMount } from "svelte";
  import { writable } from "svelte/store"; //e

  let daysOfWeek = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
  ];
  let hours = [];
  let currentWeek = [];
  let currentDate = new Date();
  let appointments = writable([]); //e

  // Generar horas desde las 7:00 am hasta las 8:00 pm
  for (let i = 7; i <= 20; i++) {
    hours.push(`${i}:00`);
  }

  function getWeekDates(date) {
    let startOfWeek = new Date(date);
    startOfWeek.setDate(date.getDate() - date.getDay() + 1);
    let week = [];
    for (let i = 0; i < 6; i++) {
      let day = new Date(startOfWeek);
      day.setDate(startOfWeek.getDate() + i);
      week.push(day);
    }
    return week;
  }

  function previousWeek() {
    currentDate.setDate(currentDate.getDate() - 7);
    currentWeek = getWeekDates(currentDate);
  }

  function nextWeek() {
    currentDate.setDate(currentDate.getDate() + 7);
    currentWeek = getWeekDates(currentDate);
  }
  //turnos
  function addAppointment(day, hour) {
    const newAppointment = {
      id: Math.random().toString(36).substr(2, 9),
      day,
      hour,
      createdAt: new Date(),
      clientDNI: "12345678",
      vehiclePlate: "ABC123",
    };
    appointments.update((apps) => [...apps, newAppointment]);
  }

  function showDetails(appointment) {
    alert(
      `DNI: ${appointment.clientDNI}\nPatente: ${appointment.vehiclePlate}`
    );
  }

  onMount(() => {
    currentWeek = getWeekDates(currentDate);
  });
</script>

<div class="controls">
  <button on:click={previousWeek}>Anterior</button>
  <h2>
    Semana del {currentWeek[0]?.toLocaleDateString()} al {currentWeek[5]?.toLocaleDateString()}
  </h2>
  <button on:click={nextWeek}>Siguiente</button>
</div>

<div class="calendar">
  <div class="hour header">Hora</div>
  {#each currentWeek as day}
    <div class="day header">
      {day.toLocaleDateString("es-ES", { weekday: "long", day: "numeric" })}
    </div>
  {/each}

  {#each hours as hour}
    <div class="hour">{hour}</div>
    {#each currentWeek as day}
      <button
        class="day"
        on:click={() => addAppointment(day, hour)}
        on:keydown={(e) => e.key === "Enter" && addAppointment(day, hour)}
      >
        {#each $appointments.filter((app) => app.day.toDateString() === day.toDateString() && app.hour === hour) as appointment (appointment.id)}
          <button
            class="appointment"
            on:click={() => showDetails(appointment)}
            on:keydown={(e) => e.key === "Enter" && showDetails(appointment)}
          >
            Turno #{appointment.id} - {appointment.hour}
          </button>
        {/each}
      </button>
    {/each}
  {/each}
</div>

<style>
  .calendar {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 10px;
  }
  .hour {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: center;
  }
  .day {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: center;
    position: relative;
  }
  .header {
    font-weight: bold;
    background-color: #f0f0f0;
  }
  .appointment {
    background-color: pink;
    margin: 5px 0;
    padding: 5px;
    cursor: pointer;
  }
  .controls {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
  }
</style>
