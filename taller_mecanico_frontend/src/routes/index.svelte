<script>
    import { goto } from '@sveltejs/kit';
    
    function goToTurnos() {
        goto('/turnos');
    }
</script>

<main>
    <h1>¡Bienvenido al Sistema de Gestión de Turnos!</h1>
    <p>Seleccione una opción:</p>
    <button on:click={goToTurnos}>Visualizar Turnos</button>
</main>

<style>
    main {
        text-align: center;
        padding: 2rem;
    }

    button {
        padding: 1rem 2rem;
        font-size: 1.2rem;
        cursor: pointer;
    }
</style>