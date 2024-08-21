<script>
    import { onMount } from 'svelte';
    let turnos = [];

    onMount(async () => {
        const response = await fetch('http://localhost:3000/turnos/');
        turnos = await response.json();
    });
</script>

<main>
    <h1>Visualizar Turnos</h1>
    {#if turnos.length > 0}
        <table>
            <thead>
                <tr>
                    <th>Fecha</th>
                    <th>Hora</th>
                    <th>Cliente</th>
                    <th>Vehículo</th>
                </tr>
            </thead>
            <tbody>
                {#each turnos as turno}
                    <tr>
                        <td>{turno.fecha}</td>
                        <td>{turno.hora}</td>
                        <td>{turno.cliente}</td>
                        <td>{turno.vehiculo}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    {:else}
        <p>No hay turnos disponibles.</p>
    {/if}
</main>