let my_div = document.getElementById('#red_header');
my_div.addEventListener('click', () => {
    document.getElementsByTagName("header")[0].classList.add('red');
});