// let my_div = document.getElementById('#red_header');
// my_div.addEventListener('click', () => {
//     document.getElementsByTagName("header")[0].classList.add('red');
// });
$('DIV#red_header').click(function () {
    $('HEADER').addClass('red');
  });
