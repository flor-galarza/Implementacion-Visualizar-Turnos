<script>
  import Icon from "@iconify/svelte";
  export let turnos = [];

  let mostrarFiltros = false;
  let tipoFiltro = "";
  let fechaInicio = "";
  let fechaFin = "";
  let marca = "";
  let tipoVehiculo = "";
  let categoriaVehiculo = "";

  let mostrarOrdenamiento = false;
  let tipoOrdenamiento = "";

  function filtrarTurnos() {
    return turnos.filter((turno) => {
      const fechaTurno = new Date(turno.fecha);
      const fechaInicioValida = fechaInicio
        ? new Date(fechaInicio) <= fechaTurno
        : true;
      const fechaFinValida = fechaFin ? new Date(fechaFin) >= fechaTurno : true;
      const marcaValida = marca
        ? turno.marca.toLowerCase().includes(marca.toLowerCase())
        : true;
      const tipoVehiculoValido = tipoVehiculo
        ? turno.tipoVehiculo.toLowerCase().includes(tipoVehiculo.toLowerCase())
        : true;
      const categoriaVehiculoValida = categoriaVehiculo
        ? turno.categoriaVehiculo
            .toLowerCase()
            .includes(categoriaVehiculo.toLowerCase())
        : true;

      return (
        fechaInicioValida &&
        fechaFinValida &&
        marcaValida &&
        tipoVehiculoValido &&
        categoriaVehiculoValida
      );
    });
  }

  function ordenarTurnos(turnos) {
    if (tipoOrdenamiento === "fecha") {
      return turnos.sort((a, b) => new Date(a.fecha) - new Date(b.fecha));
    } else if (tipoOrdenamiento === "dni") {
      return turnos.sort((a, b) => a.clientDNI.localeCompare(b.clientDNI));
    } else if (tipoOrdenamiento === "patente") {
      return turnos.sort((a, b) =>
        a.vehiclePlate.localeCompare(b.vehiclePlate)
      );
    }
    return turnos;
  }

  function mostrarOpcionesFiltro() {
    mostrarFiltros = !mostrarFiltros;
  }

  function mostrarOpcionesOrdenamiento() {
    mostrarOrdenamiento = !mostrarOrdenamiento;
  }
</script>

<h2>
  <Icon
    icon="mdi:clipboard-list"
    style=" margin-right: 10px;
    font-size: 28px;
    position: relative;
    top: 5px"
  />Listado de Turnos
</h2>

<button on:click={mostrarOpcionesFiltro}>
  <Icon icon="mdi:filter" style=" margin-right: 5px;" />
  {#if mostrarFiltros}
    Ocultar
  {:else}
    Filtros
  {/if}
</button>

{#if mostrarFiltros}
  <div>
    <label>
      Tipo de Filtro:
      <select bind:value={tipoFiltro}>
        <option value="">Seleccionar</option>
        <option value="fecha">Fecha</option>
        <option value="marca">Marca del Vehículo</option>
        <option value="tipoVehiculo">Tipo de Vehículo</option>
        <option value="categoriaVehiculo">Categoría del Vehículo</option>
      </select>
    </label>

    {#if tipoFiltro === "fecha"}
      <label>
        Fecha Inicio:
        <input type="date" bind:value={fechaInicio} />
      </label>
      <label>
        Fecha Fin:
        <input type="date" bind:value={fechaFin} />
      </label>
    {/if}

    {#if tipoFiltro === "marca"}
      <label>
        Marca del Vehículo:
        <input
          type="text"
          bind:value={marca}
          placeholder="Marca del vehículo"
        />
      </label>
    {/if}

    {#if tipoFiltro === "tipoVehiculo"}
      <label>
        Tipo de Vehículo:
        <input
          type="text"
          bind:value={tipoVehiculo}
          placeholder="Tipo de vehículo"
        />
      </label>
    {/if}

    {#if tipoFiltro === "categoriaVehiculo"}
      <label>
        Categoría del Vehículo:
        <input
          type="text"
          bind:value={categoriaVehiculo}
          placeholder="Categoría del vehículo"
        />
      </label>
    {/if}
  </div>
{/if}

<button on:click={mostrarOpcionesOrdenamiento}>
  <Icon icon="mdi:sort" class="icono-boton" />
  {#if mostrarOrdenamiento}
    Ocultar
  {:else}
    Ordenar
  {/if}
</button>

{#if mostrarOrdenamiento}
  <div>
    <label>
      Tipo de Ordenamiento:
      <select bind:value={tipoOrdenamiento}>
        <option value="">Seleccionar</option>
        <option value="fecha">Fecha</option>
        <option value="dni">DNI</option>
        <option value="patente">Patente</option>
      </select>
    </label>
  </div>
{/if}

<ul>
  {#each ordenarTurnos(filtrarTurnos()) as turno}
    <li class="turno">
      <p>Fecha: {turno.fecha}</p>
      <p>Hora: {turno.hora}</p>
      <p>Descripción: {turno.descripcion}</p>
      <p>Marca: {turno.marca}</p>
      <p>Tipo de Vehículo: {turno.tipoVehiculo}</p>
      <p>Categoría del Vehículo: {turno.categoriaVehiculo}</p>
      <p>DNI: {turno.clientDNI}</p>
      <p>Patente: {turno.vehiclePlate}</p>
    </li>
  {/each}
</ul>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap");

  ul {
    list-style-type: none;
    padding: 0;
  }

  .turno {
    background-color: #e0f7fa;
    border: 1px solid #00897b;
    border-radius: 10px;
    padding: 10px;
    margin: 10px 0;
    font-family: "Roboto", sans-serif;
    width: auto;
  }

  .turno p {
    margin: 5px 0;
    font-size: 14px;
  }
</style>
