<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
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


// config para efeito de fumaça
const cine = ref(null)
let limpar = null

onMounted(() => {
    const c = cine.value
    const x = c.getContext('2d')
    const parado = matchMedia('(prefers-reduced-motion:reduce)').matches
    let W, H, t = 0, i, rafId

    function ajustar() {
        const r = c.getBoundingClientRect()
        W = c.width = r.width / 2
        H = c.height = r.height / 2
    }
    ajustar()
    const ro = new ResizeObserver(ajustar)
    ro.observe(c)

    // partículas com "profundidade": as de trás são menores, mais lentas e mais fracas
    const poeira = Array.from({ length: innerWidth < 768 ? 60 : 120 }, () => {
        const z = Math.random() // 0 = longe, 1 = perto
        return {
            x: Math.random(), y: Math.random(),
            z,
            r: 0.5 + z * 1.1,
            v: 0.00004 + z * 0.00014,
            a: 0.12 + z * 0.40,
            p: Math.random() * 6
        }
    })

    function quadro() {
        t += 0.004
        x.globalCompositeOperation = 'source-over'
        x.clearRect(0, 0, W, H)

        // fumaça: verde muito escuro, quase invisível
        for (i = 0; i < 5; i++) {
            const cx = W * (0.5 + 0.45 * Math.sin(t * 0.7 + i * 1.9))
            const cy = H * (0.55 + 0.3 * Math.cos(t * 0.5 + i * 2.3))
            const r = Math.max(W, H) * (0.45 + 0.1 * Math.sin(t + i))
            const g = x.createRadialGradient(cx, cy, 0, cx, cy, r)
            g.addColorStop(0, i % 2 ? 'rgba(7,18,7,.30)' : 'rgba(7,26,7,.10)')
            g.addColorStop(0.6, 'rgba(25,40,8,.02)')
            g.addColorStop(1, 'rgba(0,0,0,0)')
            x.fillStyle = g
            x.fillRect(0, 0, W, H)
        }

        // holofote: só um brilho que passa devagar
        x.globalCompositeOperation = 'lighter'
        const bx = W * (0.5 + 0.35 * Math.sin(t * 0.8))
        const lg = x.createLinearGradient(bx - W * 0.2, 0, bx + W * 0.2, H)
        lg.addColorStop(0, 'rgba(200,225,190,0.01)')
        lg.addColorStop(0.5, 'rgba(200,225,190,.022)')
        lg.addColorStop(1, 'rgba(200,225,190,0)')
        x.save()
        x.translate(W / 2, H / 2); x.rotate(-0.35); x.translate(-W / 2, -H / 2)
        x.fillStyle = lg
        x.fillRect(-W, -H, W * 3, H * 3)
        x.restore()

        // poeira: o foco do efeito
        x.globalCompositeOperation = 'source-over'
        poeira.forEach(d => {
            d.y -= d.v * 16
            d.x += Math.sin(t * 2 + d.p) * 0.0003 * (0.5 + d.z)
            if (d.y < -0.02) { d.y = 1.02; d.x = Math.random() }
            const brilho = d.a * (0.65 + 0.35 * Math.sin(t * 2.5 + d.p))
            x.fillStyle = `rgba(200,230,185,${brilho})`
            x.beginPath()
            x.arc(d.x * W, d.y * H, d.r, 0, 6.283)
            x.fill()
        })
        x.shadowBlur = 0

        // granulado: bem leve
        for (i = 0; i < 150; i++) {
            x.fillStyle = `rgba(255,255,255,${Math.random() * 0.035})`
            x.fillRect(Math.random() * W, Math.random() * H, 1, 1)
        }

        if (!parado) rafId = requestAnimationFrame(quadro)
    }
    quadro()

    limpar = () => { cancelAnimationFrame(rafId); ro.disconnect() }
})

onBeforeUnmount(() => limpar && limpar())



</script>

<template>
    <section class="horario-container" id="horarios">

        <!--  o video-->
        <video class="horario-video" autoplay muted loop playsinline>
            <source src="../assets/images/videocardluz2.mp4" type="video/mp4" />
        </video>

        <!-- O fundo animado -->
        <canvas ref="cine" class="horario-video" style="mix-blend-mode:"
            aria-hidden="true"></canvas>

        <!-- O Título vem de baixo -->
        <div class="titulo escondido-baixo">
            <h1 class="texto-titulo">HORÁRIOS</h1>
            <p class="descricao-titulo">Feche o seu horário mensal e garanta o desconto, ou reserve jogos<br> avulsos
                para o seu time</p>
        </div>

        <div class="os-cards">
            <!-- Embrulhamos o card 1 na caixa que vem da esquerda -->
            <div class="escondido-esq">
                <Card titulo="Segunda a Sexta" horario1="08h as 18h" valor1="80,00" horario2="18h as 00h"
                    valor2="120,00" />
            </div>

            <!-- Embrulhamos o card 2 na caixa que vem da direita -->
            <div class="escondido-dir">
                <Card titulo="Sábado e Domingo" horario1="08h as 18h" valor1="120,00" />
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
.horario-video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 100%;
    z-index: 0;
}

/* escurecimento nas bordas, por cima do canvas */
.horario-container::before {
    content: "";
    position: absolute;
    inset: 0;
    z-index: 1;
    pointer-events: none;
    background:
        radial-gradient(ellipse at 50% 40%, transparent 35%, rgba(2, 20, 2, .5) 100%),
        linear-gradient(180deg, rgba(2, 20, 2, .45), transparent 30%, transparent 70%, rgba(2, 20, 2, .55));

}

.titulo,
.os-cards,
.contatos {
    position: relative;
    z-index: 2;
}


.horario-container {
    position: relative;
    overflow: hidden;

    box-sizing: border-box;
    display: flex;
    padding-top: 2em;
    flex-direction: column;
    justify-content: space-around;
    width: 100%;
    min-height: 100vh;
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
    line-height: 95%;
    /* 22.8px */
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
    transform: translate(0, 0);
    /* Reseta as posições X e Y para o zero original */
}

@media (max-width: 768px) {
    .os-cards {
        flex-direction: column;
        gap: 30px;
        padding: 50px;
        align-items: stretch;

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

    .descricao-titulo {
        font-size: 11px;
        padding: 0 20px;
    }

    .os-cards {
        margin-top: 20px;
        padding: 10px;
        gap: 20px;
    }



    .contatos {
        grid-template-columns: repeat(2, 1fr);
        gap: 15px;
        padding-bottom: 20px;
        /* Garante que os contatos não colem no limite inferior do celular */
    }
}
</style>