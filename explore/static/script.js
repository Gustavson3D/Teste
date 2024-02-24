var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


var popup = L.popup()
    .setLatLng([51.513, -0.09])
    .setContent("I am a standalone popup.")
    .openOn(map);

    var popup = L.popup();

    // function onMapClick(e) {
    //     popup
    //         .setLatLng(e.latlng)
    //         .setContent("You clicked the map at " + e.latlng.toString())
    //         .openOn(map);
    // }
    
    // map.on('click', onMapClick);

    // document.addEventListener("DOMContentLoaded", function() {
    //   // Obtendo elementos
    //   var dropdown = document.querySelector('.dropdown');
    //   var acomodacaoOptions = document.getElementById('acomodacao-options');
    //   var comidaOptions = document.getElementById('comida-options');
    
    //   // Adicionando evento de clique no dropdown
    //   dropdown.addEventListener('click', function() {
    //     // Alternando a visibilidade das opções
    //     acomodacaoOptions.classList.toggle('show');
    //     comidaOptions.classList.toggle('show');
    //   });
    // });
    