<script>
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import Turnos from "./Turnos.svelte";
  import Icon from "@iconify/svelte";

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
  let appointments = writable([]);
  let searchQuery = "";
  let filteredAppointments = writable([]);

  let mostrarTurnos = false;
  let turnos = [
    {
      fecha: "2024-08-26",
      hora: "12:00",
      descripcion: "Turno 1",
      marca: "Toyota",
      tipoVehiculo: "Sedán",
      categoriaVehiculo: "A",
    },
    {
      fecha: "2024-08-27",
      hora: "07:00",
      descripcion: "Turno 2",
      marca: "Honda",
      tipoVehiculo: "SUV",
      categoriaVehiculo: "B",
    },
    // Agrega más turnos aquí
  ];

  let turnoSeleccionado = null;

  function cambiarVista() {
    mostrarTurnos = !mostrarTurnos;
  }

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
    filterAppointments();
  }

  function showDetails(appointment) {
    turnoSeleccionado = appointment;
  }
  function closeDetails() {
    turnoSeleccionado = null;
  }

  function filterAppointments() {
    appointments.subscribe((apps) => {
      filteredAppointments.set(
        apps.filter(
          (app) =>
            app.clientDNI.includes(searchQuery) ||
            app.vehiclePlate.includes(searchQuery)
        )
      );
    });
  }

  onMount(() => {
    currentWeek = getWeekDates(currentDate);
    filterAppointments();
  });
</script>

<button on:click={cambiarVista}>
  {#if mostrarTurnos}
    Calendario
  {:else}
    Lista Turnos
  {/if}
</button>

<div class="search">
  <Icon
    icon="mdi:magnify"
    style=" margin-right: 10px;
    font-size: 28px;
    position: relative;
    top: 5px"
  />
  <input
    type="text"
    placeholder="Buscar por Cliente o Patente o Fecha"
    bind:value={searchQuery}
    on:input={filterAppointments}
  />
</div>

{#if mostrarTurnos}
  <Turnos {turnos} />
{:else}
  <h2>Calendario</h2>
  <div class="controls">
    <button on:click={previousWeek}>&larr;</button>
    <h2>
      Semana del {currentWeek[0]?.toLocaleDateString()} al {currentWeek[5]?.toLocaleDateString()}
    </h2>
    <button on:click={nextWeek}>&rarr;</button>
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
          on:dblclick={() => addAppointment(day, hour)}
          on:keydown={(e) => e.key === "Enter" && addAppointment(day, hour)}
        >
          {#each $filteredAppointments.filter((app) => app.day.toDateString() === day.toDateString() && app.hour === hour) as appointment (appointment.id)}
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
{/if}

{#if turnoSeleccionado}
  <div class="modal">
    <div class="modal-content">
      <span
        class="close"
        tabindex="0"
        role="button"
        on:click={closeDetails}
        on:keydown={(e) => e.key === "Enter" && closeDetails()}>&times;</span
      >
      <h2>Detalles del Turno</h2>
      <p>ID: {turnoSeleccionado.id}</p>
      <p>DNI: {turnoSeleccionado.clientDNI}</p>
      <p>Patente: {turnoSeleccionado.vehiclePlate}</p>
    </div>
  </div>
{/if}

<style>
  .modal {
    display: block;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0, 0, 0);
    background-color: rgba(0, 0, 0, 0.4);
  }

  .modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
  }

  .close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
  }

  .close:hover,
  .close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
  }
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
    justify-content: center;
    align-items: center;
    margin-bottom: 10px;
  }
  .controls button {
    background: none;
    border: none;
    font-size: 1.5em;
    cursor: pointer;
    margin: 0 10px;
  }
  .search {
    margin-bottom: 10px;
    display: flex;
    justify-content: flex-end;
  }
  .search input {
    width: 300px;
    height: 20px;
    padding: 10px;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
</style>
