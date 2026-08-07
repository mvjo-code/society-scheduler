<script setup>
import { onMounted } from 'vue'
import Card from './Card.vue'

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('mostrar')
      }
    })
  }, { 
    threshold: 0.2 
  })

  // Agora mandamos o vigia olhar para 3 classes diferentes!
  const elementos = document.querySelectorAll('.escondido-esq, .escondido-dir, .escondido-baixo')
  elementos.forEach((el) => observer.observe(el))
})
</script>

<template>
    <section class="horario-container">
        
        <!-- O Título vem de baixo -->
        <div class="titulo escondido-baixo">
            <h1 class="texto-titulo">HORÁRIOS</h1>
            <p class="descricao-titulo">Feche o seu horário mensal e garanta o desconto, ou reserve jogos<br> avulsos para o seu time</p>
        </div>
        
        <div class="os-cards">
            <!-- Embrulhamos o card 1 na caixa que vem da esquerda -->
            <div class="escondido-esq">
                <Card
                    titulo="Segunda a Sexta"
                    horario1="08h as 18h"
                    valor1="80,00"
                    horario2="18h as 00h"
                    valor2="120,00"
                />
            </div>
            
            <!-- Embrulhamos o card 2 na caixa que vem da direita -->
            <div class="escondido-dir">
                <Card
                    titulo="Sábado e Domingo"
                    horario1="08h as 18h"
                    valor1="120,00"
                />
            </div>
        </div>

        <div class="contatos">
            <h4>Whatszapp<img src="../assets/icons/zap.svg" alt="WhatsApp"></h4>
            <h4>Instagram <img src="../assets/icons/instagram.svg" alt="Instagram"></h4>
            <h4>Telegram <img src="../assets/icons/telegram.svg" alt="telegram"></h4>
            <h4>Snapchat <img src="../assets/icons/snapchat.svg" alt="snapchat"></h4>
            <h4>Tiktok <img src="../assets/icons/tiktok.svg" alt="tiktok"></h4>
            <h4>Discord <img src="../assets/icons/discord.svg" alt="discord"></h4>
        </div>

    </section>


</template>

<style scoped>

.horario-container {
    box-sizing: border-box; 
    display: flex;
    padding-top:  2em;
    flex-direction: column;
    justify-content: space-around;
    width: 100%;
    min-height: 100vh;
    background-image: url('../assets/images/campo cards.jpg');
    background-repeat: no-repeat;
    background-size: cover;

    padding-bottom: 100px;

    color: white;
}

.titulo {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 0;
    align-items: center;

}
.texto-titulo {
    margin: 0;
    text-align: center;
    font-family: Montserrat;
    font-size: 170px;
    font-style: normal;
    font-weight: 700;
    letter-spacing: 5.34px;
}

.descricao-titulo {
    color: rgba(255, 255, 255, 0.71);
    text-align: center;
    font-family: Montserrat;
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: 95%; /* 22.8px */
    letter-spacing: 1.44px;
    margin: 0;
}

.os-cards {
    display: flex;
    box-sizing: border-box;
    width: 100%;
    justify-content: center;
    align-items: stretch;
    gap: 155px;
    padding: 60px;
}

.contatos {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-top: 50px;
    padding-bottom: 2em;
}

.contatos h4 {
    display: flex;
    align-items: center;
    gap: 10px;
    font-family: Montserrat;
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    letter-spacing: 1.44px;
    color: rgba(255, 255, 255, 0.677);
    transition: color 0.3s ease, transform 0.3s ease;
}   

.contatos h4:hover {
    color: rgba(255, 255, 255, 0.829);
    cursor: pointer;
    transform: translateY(-3px);
}

.contatos img {
    width: 24px;
    height: 24px;
}


/* --- CLASSES DE ANIMAÇÃO --- */

/* 1. Elemento saindo da Esquerda */
.escondido-esq {
    display: flex;
    opacity: 0;
    transform: translateX(-150px);
    transition: all 0.8s cubic-bezier(0.17, 0.55, 0.55, 1);
}

/* 2. Elemento saindo da Direita */
.escondido-dir {
    display: flex;
    opacity: 0;
    transform: translateX(150px);
    transition: all 0.8s cubic-bezier(0.17, 0.55, 0.55, 1);
}

/* 3. Elemento subindo (Baixo para Cima) */
.escondido-baixo {
    opacity: 0;
    transform: translateY(100px);
    transition: all 0.8s cubic-bezier(0.17, 0.55, 0.55, 1);
}

/* 4. O Ponto de Chegada (A classe injetada pelo JS) */
.mostrar {
    opacity: 1;
    transform: translate(0, 0); /* Reseta as posições X e Y para o zero original */
}

@media (max-width: 768px) {
    .os-cards {
        flex-direction: column;
        gap: 30px;
        padding: 50px;
        align-items: stretch;

        background-color: red;
    }

    .titulo {
        gap: 10px;
    }

    .texto-titulo {
        font-size: 80px;
    }

    .descricao-titulo {
        font-size: 14px;
    }

    .contatos {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        justify-content: center;
        align-items: center;
        
    }

    .contatos h4 {
        justify-content: center;
    }
}

@media (max-width: 480px) {

    .texto-titulo {
        font-size: 45px;
        letter-spacing: 2px;
    }

    /* 2. A descrição precisa de um "respiro" nas laterais para não encostar nas bordas do celular */
    .descricao-titulo {
        font-size: 11px;
        padding: 0 20px; 
    }

    .os-cards {
        margin-top: 20px; 
        padding: 10px; 
        gap: 20px;
        background-color: red;
    }



    .contatos {
        grid-template-columns: repeat(2, 1fr);
        gap: 15px;
        padding-bottom: 20px; /* Garante que os contatos não colem no limite inferior do celular */
    }
}

</style>