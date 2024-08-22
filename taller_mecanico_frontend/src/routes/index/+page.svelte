<script>
    import { goto } from '$app/navigation';
</script>

<main>
    <h1>¡Bienvenido al Sistema de Gestión de Turnos!</h1>
    <p>Seleccione una opción:</p>
    <button on:click={ () => goto('/turnos')}>Visualizar Turnos</button>
    
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
