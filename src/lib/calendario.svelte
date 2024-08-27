<script>
    import { onMount } from 'svelte';
    import { Calendar } from '@fullcalendar/core';
    import dayGridPlugin from '@fullcalendar/daygrid';
    import timeGridPlugin from '@fullcalendar/timegrid';
    import Modal from '$lib/Modal.svelte'; // Asegúrate de que esta ruta sea correcta
  
    let calendarElement;
    let calendar;
    let showModal = false;
    let currentEvent = null;
  
    // Datos de eventos con todos los campos necesarios
    let events = [
      {
        id: '1',
        title: 'Revisión SUV',
        start: '2024-08-27T10:00:00',
        description: 'Revisión técnica para SUV.',
        marca: 'Toyota',
        tipo: 'SUV',
        categoria: 'B'
      },
      {
        id: '2',
        title: 'Revisión Sedán',
        start: '2024-08-28T14:00:00',
        description: 'Revisión técnica para sedán.',
        marca: 'Honda',
        tipo: 'Sedán',
        categoria: 'A'
      },
      {
        id: '3',
        title: 'Revisión SUV',
        start: '2024-08-29T09:00:00',
        description: 'Revisión técnica para SUV.',
        marca: 'Ford',
        tipo: 'SUV',
        categoria: 'B'
        },
        {
    id: '4',
    title: 'Revisión Hatchback',
    start: '2024-08-30T11:00:00',
    description: 'Revisión técnica para hatchback.',
    marca: 'Volkswagen',
    tipo: 'Hatchback',
    categoria: 'A'
  },
  {
    id: '5',
    title: 'Revisión Pickup',
    start: '2024-08-31T13:00:00',
    description: 'Revisión técnica para pickup.',
    marca: 'Chevrolet',
    tipo: 'Pickup',
    categoria: 'C'
  },
  {
    id: '6',
    title: 'Revisión Coupé',
    start: '2024-09-01T10:00:00',
    description: 'Revisión técnica para coupé.',
    marca: 'BMW',
    tipo: 'Coupé',
    categoria: 'B'
  },
  {
    id: '7',
    title: 'Revisión Sedán',
    start: '2024-09-02T15:00:00',
    description: 'Revisión técnica para sedán.',
    marca: 'Toyota',
    tipo: 'Sedán',
    categoria: 'A'
  },
  {
    id: '8',
    title: 'Revisión SUV',
    start: '2024-09-03T08:00:00',
    description: 'Revisión técnica para SUV.',
    marca: 'Nissan',
    tipo: 'SUV',
    categoria: 'C'
  },
  {
    id: '9',
    title: 'Revisión Hatchback',
    start: '2024-09-04T12:00:00',
    description: 'Revisión técnica para hatchback.',
    marca: 'Mazda',
    tipo: 'Hatchback',
    categoria: 'B'
  },
  {
    id: '10',
    title: 'Revisión Pickup',
    start: '2024-09-05T14:00:00',
    description: 'Revisión técnica para pickup.',
    marca: 'Ram',
    tipo: 'Pickup',
    categoria: 'C'
  },
  {
    id: '11',
    title: 'Revisión Coupé',
    start: '2024-09-06T16:00:00',
    description: 'Revisión técnica para coupé.',
    marca: 'Audi',
    tipo: 'Coupé',
    categoria: 'A'
  },
  {
    id: '12',
    title: 'Revisión Sedán',
    start: '2024-09-07T09:00:00',
    description: 'Revisión técnica para sedán.',
    marca: 'Hyundai',
    tipo: 'Sedán',
    categoria: 'B'
  },
  {
    id: '13',
    title: 'Revisión SUV',
    start: '2024-09-08T11:00:00',
    description: 'Revisión técnica para SUV.',
    marca: 'Jeep',
    tipo: 'SUV',
    categoria: 'A'
  },
  {
    id: '14',
    title: 'Revisión Hatchback',
    start: '2024-09-09T13:00:00',
    description: 'Revisión técnica para hatchback.',
    marca: 'Kia',
    tipo: 'Hatchback',
    categoria: 'C'
  },
  {
    id: '15',
    title: 'Revisión Pickup',
    start: '2024-09-10T10:00:00',
    description: 'Revisión técnica para pickup.',
    marca: 'GMC',
    tipo: 'Pickup',
    categoria: 'B'
  },
  {
    id: '16',
    title: 'Revisión Coupé',
    start: '2024-09-11T12:00:00',
    description: 'Revisión técnica para coupé.',
    marca: 'Mercedes-Benz',
    tipo: 'Coupé',
    categoria: 'A'
  },
  {
    id: '17',
    title: 'Revisión Sedán',
    start: '2024-09-12T14:00:00',
    description: 'Revisión técnica para sedán.',
    marca: 'Ford',
    tipo: 'Sedán',
    categoria: 'C'
  },
  {
    id: '18',
    title: 'Revisión SUV',
    start: '2024-09-13T16:00:00',
    description: 'Revisión técnica para SUV.',
    marca: 'Subaru',
    tipo: 'SUV',
    categoria: 'B'
  },
  {
    id: '19',
    title: 'Revisión Hatchback',
    start: '2024-09-14T09:00:00',
    description: 'Revisión técnica para hatchback.',
    marca: 'Honda',
    tipo: 'Hatchback',
    categoria: 'A'
  },
  {
    id: '20',
    title: 'Revisión Pickup',
    start: '2024-09-15T11:00:00',
    description: 'Revisión técnica para pickup.',
    marca: 'Toyota',
    tipo: 'Pickup',
    categoria: 'C'
  },
  {
    id: '21',
    title: 'Revisión Coupé',
    start: '2024-09-16T13:00:00',
    description: 'Revisión técnica para coupé.',
    marca: 'Porsche',
    tipo: 'Coupé',
    categoria: 'B'
  },
  {
    id: '22',
    title: 'Revisión Sedán',
    start: '2024-09-17T15:00:00',
    description: 'Revisión técnica para sedán.',
    marca: 'Chevrolet',
    tipo: 'Sedán',
    categoria: 'A'
  },
  {
    id: '23',
    title: 'Revisión SUV',
    start: '2024-09-18T08:00:00',
    description: 'Revisión técnica para SUV.',
    marca: 'Mazda',
    tipo: 'SUV',
    categoria: 'B'
  },
  {
    id: '24',
    title: 'Revisión Hatchback',
    start: '2024-09-19T10:00:00',
    description: 'Revisión técnica para hatchback.',
    marca: 'Nissan',
    tipo: 'Hatchback',
    categoria: 'C'
  },
  {
    id: '25',
    title: 'Revisión Pickup',
    start: '2024-09-20T12:00:00',
    description: 'Revisión técnica para pickup.',
    marca: 'Ford',
    tipo: 'Pickup',
    categoria: 'B'
  }
    ];

      // Estados para los filtros
    let tipoFiltro = '';
    let marcaFiltro = '';
    let categoriaFiltro = '';

      // Filtros únicos para los selectores
    let tipos = [...new Set(events.map(event => event.tipo))];
    let marcas = [...new Set(events.map(event => event.marca))];
    let categorias = [...new Set(events.map(event => event.categoria))];

     // Función para aplicar filtros
    function aplicarFiltros() {
    let filteredEvents = events.filter(event => {
      return (!tipoFiltro || event.tipo === tipoFiltro) &&
             (!marcaFiltro || event.marca === marcaFiltro) &&
             (!categoriaFiltro || event.categoria === categoriaFiltro);
    });
    calendar.getEvents().forEach(e => e.remove());
    calendar.addEventSource(filteredEvents);
  }

  
  onMount(() => {
    if (calendarElement) {
      calendar = new Calendar(calendarElement, {
        plugins: [dayGridPlugin, timeGridPlugin],
        initialView: 'timeGridWeek',
        events: events,
        eventClick: function(info) {
          currentEvent = {
            title: info.event.title,
            start: info.event.startStr,
            description: info.event.extendedProps.description,
            marca: info.event.extendedProps.marca,
            tipo: info.event.extendedProps.tipo,
            categoria: info.event.extendedProps.categoria
          };
          showModal = true;
        }
      });

      calendar.render();
    }
  });
  
    function closeModal() {
      showModal = false;
      currentEvent = null;
    }
  </script>

<div>
    <label for="tipo">Tipo:</label>
    <select id="tipo" bind:value={tipoFiltro} on:change={aplicarFiltros}>
      <option value="">Todos</option>
      {#each tipos as tipo}
        <option value={tipo}>{tipo}</option>
      {/each}
    </select>
  
    <label for="marca">Marca:</label>
    <select id="marca" bind:value={marcaFiltro} on:change={aplicarFiltros}>
      <option value="">Todas</option>
      {#each marcas as marca}
        <option value={marca}>{marca}</option>
      {/each}
    </select>
  
    <label for="categoria">Categoría:</label>
    <select id="categoria" bind:value={categoriaFiltro} on:change={aplicarFiltros}>
      <option value="">Todas</option>
      {#each categorias as categoria}
        <option value={categoria}>{categoria}</option>
      {/each}
    </select>
  </div>
  
  <div bind:this={calendarElement} id="calendar"></div>
  
  {#if showModal && currentEvent}
    <Modal {currentEvent} close={closeModal} />
  {/if}
  
  <style>
    #calendar {
      max-width: 900px;
      margin: 0 auto;
    }
  
    div {
      margin-bottom: 20px;
    }
  
    select {
      margin-right: 10px;
    }
  </style>
  