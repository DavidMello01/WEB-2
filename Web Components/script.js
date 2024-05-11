class ThemeToggle extends HTMLElement {
    constructor() {
      super();
      this.attachShadow({ mode: 'open' });
      this.shadowRoot.innerHTML = `
        <style>
          .theme-button {
            cursor: pointer;
            padding: 8px 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            outline: none;
          }
          .theme-button:hover {
            background-color: #0056b3;
          }
        </style>
        <button class="theme-button">Alternar Tema</button>
      `;
    }

    connectedCallback() {
      this.shadowRoot.querySelector('.theme-button').addEventListener('click', () => {
        document.body.classList.toggle('dark-theme');
      });
    }
  }

  customElements.define('theme-toggle', ThemeToggle);

  let carouselIndex = 0;

    function showImage(index) {
      const slides = document.querySelectorAll('.carousel-item');
      if (index >= slides.length) {
        carouselIndex = 0;
      } else if (index < 0) {
        carouselIndex = slides.length - 1;
      }

      const slideWidth = slides[0].offsetWidth;
      document.querySelector('.carousel-inner').style.transform = `translateX(-${carouselIndex * slideWidth}px)`;
    }

    function nextSlide() {
      carouselIndex++;
      showImage(carouselIndex);
    }

    function previousSlide() {
      carouselIndex--;
      showImage(carouselIndex);
    }

    setInterval(nextSlide, 3000); // Troca a imagem a cada 3 segundos

    showImage(carouselIndex); // Mostra a primeira imagem inicialmente