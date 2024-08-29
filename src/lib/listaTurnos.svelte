<script>
  export let events = [];
</script>

<style>
  .turno {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px 0;
  }
</style>

<div>
  {#each events as event}
    <div class="turno">
      <h3>{event.title}</h3>
      <p>{event.description}</p>
      <p><strong>Marca:</strong> {event.marca}</p>
      <p><strong>Tipo:</strong> {event.tipo}</p>
      <p><strong>Categoría:</strong> {event.categoria}</p>
      <p><strong>Cliente:</strong> {event.cliente}</p>
      <p><strong>DNI:</strong> {event.dni}</p>
      <p><strong>Teléfono:</strong> {event.telefono}</p>
      <p><strong>Email:</strong> {event.email}</p>
    </div>
  {/each}
</div>
