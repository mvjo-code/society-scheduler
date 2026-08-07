<script setup>
// Importamos a Navbar para dentro do Hero para ela flutuar sobre a imagem
import Navbar from './Navbar.vue'
</script>

<template>
  <section class="hero-container" id="home">
    <Navbar />
    
    <!-- O conteúdo de texto e botão vai aqui -->
    <div class="hero-content">
      <h1 class="titulo">Arena<br>Society</h1>
      <p class="subtitulo">O Seu Jogo Levado a Sério.</p>
      <button class="btn-agendar">Agendar Meu Jogo 
        <img src="../assets/icons/ceta_direita.svg" class="icone-seta" alt="icone-seta-direita" />
      </button>
    </div>
  </section>
</template>

<style scoped>
.hero-container {
    background-image: url('../assets/images/hero_image.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center 100%;

    min-height: 100vh;
    width: 100%;
    
    display: flex;
    flex-direction: column;

    margin: 0;
    padding-top: 96px;
    padding-left: 85px;
    padding-right: 116px;
    box-sizing: border-box;
    gap: 88px;

    box-sizing: border-box;
}

.hero-content {
    display: flex;
    width: 734px;
    flex-direction: column;
    align-items: flex-end;
    gap: 73px;
    align-self: flex-end;
}

.titulo {
    color: rgba(255, 255, 255, 0.90);
    text-align: right;
    
    /* Nome entre aspas e com fallback (sans-serif) */
    font-family: 'Montserrat', sans-serif; 
    
    font-size: 170.963px;
    font-weight: 700;
    line-height: 92%; 
    letter-spacing: 7.159px;
    margin: 0;
}

.subtitulo {
    color: rgba(255, 255, 255, 0.90);
    text-align: center;
    font-family: Inter;
    font-size: 32px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    margin: 0;
}

.btn-agendar {
    display: flex;
    padding: 15px 30px; 
    justify-content: center;
    align-items: center;
    gap: 15px; 
    border-radius: 16px;
    
    /* Fundo dinâmico */
    background: linear-gradient(
        96deg, 
        rgba(81, 107, 11, 0.268) 0%,     
        rgba(102, 133, 16, 0.822) 25%,   
        rgba(118, 153, 22, 0.379) 50%,   
        rgba(111, 149, 8, 0.245) 75%,    
        rgba(82, 107, 11, 0.40) 100%    
    );
    background-size: 200% auto;
    background-position: 0% center;
    
    color: rgba(255, 255, 255, 0.90);
    font-family: 'Montserrat', sans-serif;
    font-size: 36px;
    font-weight: 700;
    
    border: 1px solid transparent; 
    cursor: pointer;
    
    transition: background-position 0.3s ease, border 0.3s ease;
}

.icone-seta {
    display: block;
    width: 45px;
    height: auto;
}

.btn-agendar:hover {
    background-position: 50% center;
    border: 1px solid rgba(255, 255, 255, 0.90);
}

@media (max-width: 768px) {
    .hero-container {
        padding: 50px 20px;
    }

    .hero-content {
        width: 100%;
        align-items: center;
        gap: 60px;
    }

    .titulo {
        font-size: 150px;
        text-align: center;
    }

    .subtitulo {
        font-size: 24px;
    }

    .btn-agendar {
        font-size: 24px;
        padding: 10px 20px;
    }
}

@media (max-width: 480px) {
    .titulo {
        font-size: 70px;
    }

    .subtitulo {
        font-size: 18px;
    }

    .btn-agendar {
        font-size: 18px;
        padding: 8px 16px;
    }
}
</style>