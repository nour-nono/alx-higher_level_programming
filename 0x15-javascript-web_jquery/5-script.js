// document.getElementById('add_item').addEventListener('click', () => {
//     let my_head = document.getElementById('my_list');
//     let new_item = document.createElement('li');
//     new_item.innerHTML = 'Item';
//     my_head.appendChild(new_item);
// });
$('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
