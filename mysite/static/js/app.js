console.log('hello')


function toggleMenu() {
    const menu = document.querySelector('.menu');
    const hamburger = document.querySelector('.hamburger');
    menu.classList.toggle('active');
    hamburger.classList.toggle('active');
}

function hideMenu(){
    const menu = document.querySelector('.menu');
    menu.classList.remove('active');
    const hamburger = document.querySelector('.hamburger');
    hamburger.classList.remove('active');
}

