<script setup>
import Hero from './components/Hero.vue'
import Beneficios from './components/beneficios.vue'
import Horarios from './components/Horários.vue'
</script>

<template>
  <main>
    <Hero />
    <Beneficios />
    <Horarios />

    <!-- Depois, as próximas seções (Cards, Benefícios) entrarão aqui embaixo -->
  </main>
</template>

<style>
/* Importação da sua fonte */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');


* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Resetando a div raiz invisível do Vue */
#app {
  margin: 0;
  padding: 0;
  width: 100%;
}

/* evita scroll fantasma horizontal */
main, html, body {
  overflow-x: hidden; 
  width: 100%;
  background-color: #0d0d0d;
  font-family: 'Montserrat', sans-serif;
}
</style>