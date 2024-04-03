// fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json").then((response) => {
//     response.json().then((data) => {
//         document.getElementById("character").innerHTML = data.name;
//         console.log(data.name);
//     });
//     });
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
