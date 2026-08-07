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
/* Seus estilos globais que já estavam aqui */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

main, html, body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background-color: #0d0d0d;
  font-family: 'Montserrat', sans-serif;
}
</style>