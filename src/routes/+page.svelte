<script>
    import Calendario from '$lib/calendario.svelte';
    import Filtros from '$lib/filtros.svelte';
  
    let tiposVehiculo = ['Sedán', 'SUV', 'Camión'];
    let fechas = [];
  
    // Datos de ejemplo
    let turnos = [
      { title: 'Revisión SUV', start: '2024-08-27' },
      { title: 'Revisión Sedán', start: '2024-08-28' }
    ];
  
    function applyFilters() {
      // Actualiza los eventos en el calendario según los filtros aplicados
    }
  </script>
  
  <h1>Gestión de Turnos de Revisiones Técnicas</h1>
  
  <Filtros {tiposVehiculo} {fechas} on:filter={applyFilters} />
  
  <Calendario {turnos} />
  
