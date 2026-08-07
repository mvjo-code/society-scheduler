<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  // Criamos o nosso "Vigia"
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      // Se o elemento entrou na tela...
      if (entry.isIntersecting) {
        // ...adicionamos a classe 'mostrar' nele
        entry.target.classList.add('mostrar')
      }
    })
  }, { 
    threshold: 0.2 // O gatilho dispara quando 20% do elemento aparecer na tela
  })

  // 2. Mandamos o vigia olhar para tudo que tem as classes 'escondido-esq' ou 'escondido-dir'
  const elementos = document.querySelectorAll('.escondido-esq, .escondido-dir')
  elementos.forEach((el) => observer.observe(el))
})
</script>

<template>
  <section class="beneficios-container" id="estrutura">
    
    <!-- Bar e Churrasqueira -->
    <div class="beneficio-item">
      <!-- A imagem começa escondida na esquerda -->
      <div class="imagem escondido-esq">
        <img src="../assets/images/bar e Churrasqueira.jpg " alt="Bar e Churrasqueira">
      </div>
      
      <!-- O texto começa escondido na direita -->
      <div class="conteudo escondido-dir">
        <h2>Bar e Churrasqueira</h2>
        <p>A resenha pós-jogo já tem lugar certo. Espaço amplo e reservado com churrasqueira completa, mesas e visão privilegiada do campo. O ambiente ideal para reunir a equipe, assar uma carne e comemorar a vitória.</p>
      </div>
    </div>

    <!-- Gramado Padrão Fifa -->
    <div class="beneficio-item">
      <div class="imagem escondido-esq">
        <img src="../assets/images/Gramado Padrão Fifa.jpeg" alt="Gramado Padrão Fifa">
      </div>
      <div class="conteudo escondido-dir">
        <h2>Gramado Padrão Fifa</h2>
        <p>Grama sintética de última geração com sistema de amortecimento avançado. O rolar da bola é perfeito e o impacto nas articulações é reduzido, garantindo alta performance e segurança para o seu time do apito inicial ao fim do jogo.</p>
      </div>
    </div>

    <!-- Vestiário Climatizado -->
    <div class="beneficio-item">
      <div class="imagem escondido-esq">
        <img src="../assets/images/Vestiário Climatizado.jpg" alt="Vestiário Climatizado">
      </div>
      <div class="conteudo escondido-dir">
        <h2>Vestiário Climatizado</h2>
        <p>Estrutura premium para o seu conforto antes e depois da partida. Vestiários amplos, chuveiros com aquecimento e ambiente climatizado para você se recuperar com tranquilidade e conforto após deixar tudo em campo.</p>
      </div>
    </div>

  </section>
</template>

<style scoped>
.beneficios-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 80px;
    padding: 100px 85px; 
    color: white;
    overflow-x: hidden; 

    /* EMPILHAMENTO DE FUNDOS: */
    background-image: 
        /* 1º (Mais acima): Luz verde no canto superior direito */
        radial-gradient(circle at 90% 10%, rgba(82, 174, 213, 0.339) 0%, transparent 40%),
        
        /* 2º: Luz verde no canto inferior esquerdo */
        radial-gradient(circle at 10% 90%, rgba(82, 174, 213, 0.191) 0%, transparent 50%),
        
        /* 3º: A sua textura de fumaça em SVG */
        
        /* 4º (Mais ao fundo): O seu degradê base */
        linear-gradient(90deg, rgba(6, 17, 2, 0.336) 0%, rgba(0, 0, 0, 0.7) 100%);
    
    /* Configurações para a textura se adaptar bem */
    background-size: cover; 
    background-position: center;
    
    /* Opcional: Se você colocar o attachment como fixed, a fumaça fica parada enquanto você rola o site, dando um efeito 3D muito massa! */

}
.beneficio-item {
  display: flex;
  align-items: center;
  gap: 50px;
  transition: transform 0.5s ease-in-out;
}

.beneficio-item:hover {
  transform: translateX(20px);
  background-color: #cccccc0b;
  

}

.imagem img {
  width: 400px; 
  height: 250px;
  object-fit: cover;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

.conteudo {
  max-width: 600px;
}

.conteudo h2 {
  font-family: 'Montserrat', sans-serif;
  font-size: 40px;
  font-weight: 700;
  margin: 0 0 20px 0;
}

.conteudo p {
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  line-height: 1.6;
  color: #cccccc;
  margin: 0;
}



/* Elementos na esquerda */
.escondido-esq {
  opacity: 0;
  transform: translateX(-200px); /* Empurra 150px para a esquerda */
  transition: all 0.8s cubic-bezier(0.17, 0.55, 0.55, 1); /* Animação suave */
}

/* Elementos na direita */
.escondido-dir {
  opacity: 0;
  transform: translateX(150px); /* Empurra 150px para a direita */
  transition: all 0.8s cubic-bezier(0.17, 0.55, 0.55, 1); 
  transition-delay: 0.2s; /* O texto demora uma fração de segundo a mais para entrar, dando um efeito de cascata! */
}

/* A classe que o JavaScript vai injetar quando o elemento aparecer na tela */
.mostrar {
  opacity: 1;
  transform: translateX(0); 
}

@media (max-width: 768px) {
  .beneficio-item {
    flex-direction: column;
    gap: 30px;
  }

  .imagem img {
    width: 100%;
    height: auto;
  }

  .conteudo {
    max-width: 100%;
  }
}

@media (max-width: 480px) {
  .beneficio-item {
    gap: 20px;
  }

  .conteudo h2 {
    font-size: 28px;
  }

  .conteudo p {
    font-size: 16px;
  }
}
</style>