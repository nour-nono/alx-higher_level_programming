// fetch("https://swapi-api.alx-tools.com/api/films/?format=json").then(
//     (response) => {
//         response.json().then((data) => {
//             for (const film of data.results) {
//                 let my_list = document.getElementById("list_movies");
//                 let new_item = document.createElement("li");
//                 new_item.innerHTML = film.title;
//                 my_list.appendChild(new_item);
//             }
//         });
//     }
// );
$.get('https://swapi.co/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
