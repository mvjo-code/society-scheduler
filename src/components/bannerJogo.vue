<script setup>
defineProps({
  titulo: {
    type: String,
    default: 'Jogo de Usuário'
  },
  dia: {
    type: String,
    required: true
  },
  horario: {
    type: String,
    required: true
  },
  duracao: {
    type: String,
    required: true
  },
  instagram: {
    type: String,
    default: ''
  }
})
</script>

<template>
  <div class="banner-jogo">
    <div class="bola">
      <span class="dots"></span>
      <img src="/src/assets/icons/bola.svg" alt="Bola" />
    </div>

    <div class="divisor"></div>

    <div class="info-container">
      <h2>{{ titulo }}</h2>

      <div class="info">
        <div class="info-item">
          <span class="label">Dia</span>
          <span class="valor">{{ dia }}</span>
        </div>
        <div class="info-item">
          <span class="label">Horário</span>
          <span class="valor">{{ horario }}</span>
        </div>
        <div class="info-item">
          <span class="label">Duração</span>
          <span class="valor">{{ duracao }}</span>
        </div>
      </div>

      <div class="contato">
        <span class="arena">
          <span class="ponto"></span>
          Arena society
        </span>
        <span v-if="instagram" class="insta">
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="3" y="3" width="18" height="18" rx="5" />
            <circle cx="12" cy="12" r="4" />
            <circle cx="17.5" cy="6.5" r="0.5" fill="currentColor" />
          </svg>
          insta: <strong>@{{ instagram }}</strong>
        </span>
      </div>
    </div>

    <span class="arco"></span>
  </div>
</template>

<style scoped>
.banner-jogo {
  position: relative;
  width: 100%;
  max-width: 915px;
  height: 150px;
  border-radius: 10px;
  border: 1px solid #3b4915;
  background: linear-gradient(91deg, #4e6511 1.46%, #2f3911 100.95%);
  display: flex;
  align-items: stretch;
  overflow: hidden;
  transition: all 300ms;
}

.banner-jogo:hover {
  transform: translateX(20px);
}

/* ---------- bola + pontinhos decorativos ---------- */
.bola {
  position: relative;
  width: 190px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.bola img {
  width: 96px;
  height: 96px;
  filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.35));
}

.bola .dots {
  position: absolute;
  top: 14px;
  left: 14px;
  width: 42px;
  height: 30px;
  background-image: radial-gradient(
    rgba(180, 255, 120, 0.55) 1.6px,
    transparent 1.6px
  );
  background-size: 10px 10px;
}

/* ---------- linha diagonal separando bola e texto ---------- */
.divisor {
  position: relative;
  width: 2px;
  flex-shrink: 0;
  background: #7ee62c;
  transform: skewX(-18deg);
  margin: 0 22px;
}

/* ---------- conteúdo de texto ---------- */
.info-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 14px;
  padding: 18px 26px 18px 0;
  min-width: 0;
}

.info-container h2 {
  margin: 0;
    margin-left: 20px;
    font-size: 1em;
    font-style: italic;
    font-weight: 700;
    color: #f4f7f0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 100%;
}

.info {
  display: flex;
  align-items: center;
  gap: 22px;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding-right: 22px;
  border-right: 1px solid rgba(255, 255, 255, 0.25);
}

.info-item:last-child {
  border-right: none;
  padding-right: 0;
}

.info-item .label {
  font-size: 10px;
  letter-spacing: 0.04em;
  color: rgba(255, 255, 255, 0.65);
}

.info-item .valor {
  font-size: 15px;
  font-weight: 700;
  color: #ffffff;
}

.contato {
  display: flex;
  align-items: center;
  gap: 24px;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.85);
}

.contato .arena {
  display: flex;
  align-items: center;
  gap: 6px;
  font-style: italic;
  font-weight: 600;
}

.contato .ponto {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #7ee62c;
}

.contato .insta {
  display: flex;
  align-items: center;
  gap: 5px;
  font-style: italic;
}

.contato .insta strong {
  font-weight: 700;
}

/* ---------- arco tracejado no canto ---------- */
.arco {
  position: absolute;
  top: -30px;
  right: -30px;
  width: 90px;
  height: 90px;
  border-radius: 50%;
  border: 2px dashed rgba(180, 255, 120, 0.5);
  border-left-color: transparent;
  border-bottom-color: transparent;
  pointer-events: none;
}

/* ---------- responsivo ---------- */
/* ---------- responsivo banner ---------- */
@media (max-width: 640px) {
  .banner-jogo {
    height: auto;
    flex-direction: row; /* Mantém a bola ao lado do texto */
    padding-bottom: 12px;
  }
  
  /* Diminui drasticamente a secção da bola para dar espaço ao texto */
  .bola {
    width: 70px;
    align-items: flex-start;
    padding-top: 14px;
  }
  
  .bola img {
    width: 48px;
    height: 48px;
  }
  
  .bola .dots {
    display: none; /* Removemos os pontos no telemóvel para um visual mais limpo */
  }
  
  .divisor {
    margin: 0 10px 0 0;
  }
  
  .info-container {
    padding: 14px 12px 14px 0;
    gap: 10px;
  }
  
  .info-container h2 {
    margin-left: 0; /* Remove a margem esquerda extra no telemóvel */
  }
  
  /* Compacta a área de datas e horários */
  .info {
    gap: 12px;
  }
  
  .info-item {
    padding-right: 12px;
  }
  
  .info-item .label {
    font-size: 9px;
  }
  
  .info-item .valor {
    font-size: 13px;
  }
  
  /* Coloca a arena e o instagram em linhas separadas no telemóvel */
  .contato {
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
  }
}
</style>