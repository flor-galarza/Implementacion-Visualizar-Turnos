<script>
	export let events = [];
</script>

<div>
	{#each events as event}
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
					<p><strong>Fecha:</strong> {event.start}</p>
					<p><strong>Hora:</strong> {event.start}</p>
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
