<script>
    export let currentEvent;
    export let close;
  </script>
  
  <div class="modal">
    <div class="modal-content">
      <span class="close" on:click={close}>&times;</span>
      <h1>{currentEvent.title}</h1>
      <p><strong>Descripción:</strong> {currentEvent.description || 'No disponible'}</p>
      <p><strong>Marca:</strong> {currentEvent.marca || 'No disponible'}</p>
      <p><strong>Tipo:</strong> {currentEvent.tipo || 'No disponible'}</p>
      <p><strong>Categoría:</strong> {currentEvent.categoria || 'No disponible'}</p>
      <p><strong>Fecha y Hora:</strong> {new Date(currentEvent.start).toLocaleString()}</p>
    </div>
  </div>
  
  <style>
    .modal {
      display: block;
      position: fixed;
      z-index: 1;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      background-color: rgb(0,0,0);
      background-color: rgba(0,0,0,0.4);
    }
  
    .modal-content {
      background-color: #fefefe;
      margin: 15% auto;
      padding: 20px;
      border: 1px solid #888;
      width: 80%;
    }
  
    .close {
      color: #aaa;
      float: right;
      font-size: 28px;
      font-weight: bold;
    }
  
    .close:hover,
    .close:focus {
      color: black;
      text-decoration: none;
      cursor: pointer;
    }
  
    p {
      margin: 10px 0;
    }
  </style>
  