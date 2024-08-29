<script>
	export let events = [];
	export let busqueda = '';
	export let searchFields = [];
	function buscar() {
		// Filtrar eventos por busqueda
		let filteredEvents = events.filter((event) => {
			// Buscar en los campos definidos en searchFields
			return (
				!busqueda ||
				// Buscar en cada campo del evento si alguno incluye el parametro de busqueda
				searchFields.some((field) => {
					if (field in event) {
						return event[field].toLowerCase().includes(busqueda.toLowerCase());
					}
					return false;
				})
			);
		});
		return filteredEvents;
	}
</script>

<div>
	{#each buscar() as event}
		<div class="turno">
			<h3>{event.title}</h3>
			<p>{event.description}</p>
			<div class="container">
				<div class="column">
					<p><strong>Marca:</strong> {event.marca}</p>
					<p><strong>Tipo:</strong> {event.tipo}</p>
					<p><strong>Categoría:</strong> {event.categoria}</p>
				</div>
				<div class="column">
					<p><strong>Fecha:</strong> {new Date(event.start).toLocaleDateString()}</p>
					<p><strong>Hora:</strong> {new Date(event.start).toLocaleTimeString()}</p>
				</div>
				<div class="column">
					<p><strong>Cliente:</strong> {event.cliente}</p>
					<p><strong>DNI:</strong> {event.dni}</p>
					<p><strong>Teléfono:</strong> {event.telefono}</p>
					<p><strong>Email:</strong> {event.email}</p>
				</div>
			</div>
		</div>
	{/each}
</div>

<style>
	.turno {
		border: 1px solid #ccc;
		padding: 10px;
		margin: 10px 0;
	}
	.container {
		display: flex;
		justify-content: space-between;
	}
	.column {
		flex: 1;
		padding: 10px;
	}
</style>
