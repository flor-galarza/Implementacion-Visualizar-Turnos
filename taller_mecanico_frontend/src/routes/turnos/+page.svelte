<script>
  import VisualizarTurno from "/src/VisualizarTurno.svelte";
  import Icon from "@iconify/svelte";
  import Semana from "./Semana.svelte";
</script>

<main>
  <h1>
    <Icon
      icon="mdi:calendar"
      style=" margin-right: 10px;
    font-size: 28px;
    position: relative;
    top: 5px"
    />Turnos
  </h1>
  <Semana />
</main>

<style>
  main {
    font-family: Arial, sans-serif;
    padding: 20px;
  }
</style>
