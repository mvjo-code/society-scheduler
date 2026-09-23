<template>
  <div class="loading-container">
    <div class="orbit-system">
      <!-- Auras / Anéis Minimalistas -->
      <div class="ring-outer"></div>
      <div class="ring-inner"></div>

      <!-- Bola de Futebol Construída apenas com linhas (Line-art SVG) -->
      <svg class="soccer-ball-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <!-- Círculo base (contorno da bola) -->
        <circle cx="50" cy="50" r="46" fill="none" stroke="var(--ball-stroke)" stroke-width="1.5"/>
        
        <!-- Pentágono central -->
        <polygon points="50,28 35,39 40,57 60,57 65,39" fill="none" stroke="var(--ball-stroke)" stroke-width="1.5" stroke-linejoin="round"/>
        
        <!-- Linhas conectando o pentágono central aos cantos -->
        <line x1="50" y1="28" x2="50" y2="4" stroke="var(--ball-stroke)" stroke-width="1.5"/>
        <line x1="35" y1="39" x2="11" y2="29" stroke="var(--ball-stroke)" stroke-width="1.5"/>
        <line x1="65" y1="39" x2="89" y2="29" stroke="var(--ball-stroke)" stroke-width="1.5"/>
        <line x1="40" y1="57" x2="23" y2="80" stroke="var(--ball-stroke)" stroke-width="1.5"/>
        <line x1="60" y1="57" x2="77" y2="80" stroke="var(--ball-stroke)" stroke-width="1.5"/>
        
        <!-- Traços para formar a ilusão 3D dos pentágonos laterais -->
        <path d="M11,29 L4,50 L23,80" fill="none" stroke="var(--ball-stroke)" stroke-width="1.5" stroke-linejoin="round"/>
        <path d="M89,29 L96,50 L77,80" fill="none" stroke="var(--ball-stroke)" stroke-width="1.5" stroke-linejoin="round"/>
        <path d="M23,80 L50,96 L77,80" fill="none" stroke="var(--ball-stroke)" stroke-width="1.5" stroke-linejoin="round"/>
      </svg>
    </div>

    <div class="loading-text">
      {{ texto }}
    </div>
  </div>
</template>

<script setup>
// Permite mudar o texto passando <LoaderProcessando texto="autenticando..." />
defineProps({
  texto: {
    type: String,
    default: 'processando...'
  }
})
</script>

<style scoped>
/* Scoped garante que essas animações e estilos afetem SÓ este componente */
.loading-container {
  /* Paleta Premium isolada no escopo do container */
  --ring-base: #c9f5862e; 
  --ring-accent: #74a629; 
  --ball-stroke: #ffffffc3; 
  --text-color: #cbd5e1;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 32px;
  font-family: 'Inter', ui-sans-serif, system-ui, sans-serif;
  
  /* Mantém o componente centralizado na div pai */
  width: 100%;
  padding: 2rem 0;
}

.orbit-system {
  position: relative;
  width: 120px;
  height: 120px;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Anel externo lento */
.ring-outer {
  position: absolute;
  width: 110px;
  height: 110px;
  border-radius: 50%;
  border: 1px solid var(--ring-base);
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  animation: spin 3s linear infinite;
}

/* Anel interno com o destaque azul corporativo */
.ring-inner {
  position: absolute;
  width: 86px;
  height: 86px;
  border-radius: 50%;
  border: 1px solid var(--ring-base);
  border-bottom: 1px solid var(--ring-accent);
  box-shadow: 0 4px 12px rgba(77, 177, 34, 0.306);
  animation: spin-reverse 2.5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}

/* A bola em si girando muito lentamente para mostrar os detalhes */
.soccer-ball-svg {
  position: relative;
  width: 54px;
  height: 54px;
  animation: spin 8s linear infinite;
  opacity: 0.8;
}

/* Texto minimalista */
.loading-text {
  font-size: 0.75rem;
  font-weight: 300;
  letter-spacing: 0.25em;
  color: var(--text-color);
  text-transform: lowercase;
  animation: pulse-opacity 2s ease-in-out infinite alternate;
}

@keyframes spin {
  100% { transform: rotate(360deg); }
}

@keyframes spin-reverse {
  100% { transform: rotate(-360deg); }
}

@keyframes pulse-opacity {
  0% { opacity: 0.3; }
  100% { opacity: 0.9; }
}
</style>