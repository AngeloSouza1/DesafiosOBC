// script.js
document.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;
  
    document.querySelectorAll('.parallax').forEach((parallax, index) => {
      const speed = 0.5 + index * 0.1; // Velocidade ajustável
      parallax.style.backgroundPositionY = `${scrollPosition * speed}px`;
    });
  });
  