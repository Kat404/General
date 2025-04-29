let count = 0;
const counter = document.querySelector('.counter');
const increaseBtn = document.getElementById('increase');
const decreaseBtn = document.getElementById('decrease');

// Función para actualizar el contador
function updateCounter() {
    counter.textContent = count;
}

// Event listener para el botón de sumar
increaseBtn.addEventListener('click', () => {
    count++;
    updateCounter();
});

// Event listener para el botón de restar
decreaseBtn.addEventListener('click', () => {
    count--;
    updateCounter();
});
