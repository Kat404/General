let count = 0;
const counter = document.querySelector('.counter');
const increaseBtn = document.getElementById('increase');
const decreaseBtn = document.getElementById('decrease');
const multiplyBtn = document.getElementById('multiply');
const divideBtn = document.getElementById('divide');
const darkModeToggle = document.getElementById('darkModeToggle');

// Función para actualizar el display
function updateDisplay() {
    counter.textContent = count;
}

// Event listener para el botón de sumar
increaseBtn.addEventListener('click', () => {
    count++;
    updateDisplay();
});

// Event listener para el botón de restar
decreaseBtn.addEventListener('click', () => {
    count--;
    updateDisplay();
});

// Event listener para el botón de multiplicar
multiplyBtn.addEventListener('click', () => {
    count *= 2;
    updateDisplay();
});

// Event listener para el botón de dividir
divideBtn.addEventListener('click', () => {
    count = Math.floor(count / 2); // Redondeamos hacia abajo
    updateDisplay();
});

// Event listener para el botón de modo oscuro
darkModeToggle.addEventListener('click', () => {
    const html = document.documentElement;
    if (html.classList.contains('dark')) {
        html.classList.remove('dark');
        darkModeToggle.setAttribute('title', 'Cambiar a modo oscuro');
        darkModeToggle.querySelector('.light-mode').style.display = 'none';
        darkModeToggle.querySelector('.theme-icon').style.display = 'block';
    } else {
        html.classList.add('dark');
        darkModeToggle.setAttribute('title', 'Cambiar a modo claro');
        darkModeToggle.querySelector('.light-mode').style.display = 'block';
        darkModeToggle.querySelector('.theme-icon').style.display = 'none';
    }
});

// Inicializar el display
updateDisplay();