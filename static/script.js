const meuCabecalho = document.querySelector('h1')
    meuCabecalho.textContent = 'Ola Mundo '


const btnMobile = document.getElementById('btn-mobile');

    function toggleMenu(){
        const nav = document.getElementById('nav')
        nav.classList.toggle('active')
    }

    btnMobile.addEventListener('click', toggleMenu);

