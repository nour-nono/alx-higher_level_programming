// document.getElementById('update_header').addEventListener('click', () => {
//     let my_head = document.getElementsByTagName('header')[0];
//     my_head.innerHTML = 'New Header!!!';
// });
$('DIV#update_header').click(function () {
    $('HEADER').text('New Header!!!');
  });
