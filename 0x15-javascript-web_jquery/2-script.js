// let my_div = document.getElementById('#red_header');
// my_div.addEventListener('click', () => {
//     document.getElementsByTagName("header")[0].style.color = "#FF0000";
// });
$('DIV#red_header').click(function () {
    $('HEADER').css('color', '#FF0000');
  });
