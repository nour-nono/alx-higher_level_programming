// fetch("https://hellosalut.stefanbohacek.dev/?lang=fr").then((response)=>{
//     response.json().then((data)=>{
//         let ele = document.getElementById("hello")
//         ele.innerHTML = data.hello
//     });
// });
$('document').ready(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
