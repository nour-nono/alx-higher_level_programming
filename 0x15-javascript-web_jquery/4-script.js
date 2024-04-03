document.getElementById('toggle_header').addEventListener('click', () => {
    let my_head = document.getElementsByTagName('header')[0];
    my_head.classList.toggle('red');
    my_head.classList.toggle('green');
});