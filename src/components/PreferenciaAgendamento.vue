<script setup>
import { ref } from 'vue'

//Referência para o modal
const modalOpcoes = ref(null)

//  Declaramos que esse componente pode emitir um "grito/aviso" chamado 'abrirLogin'
const emit = defineEmits(['abrirLogin'])

// Funções padrão de abrir e fechar
const abrirModal = () => {
  modalOpcoes.value.showModal()
}

const fecharModal = () => {
  modalOpcoes.value.close()
}

// Quando clicar em "Agendar Pelo Site"
const irParaSite = () => {
  fecharModal() // Fecha o modal de opções
  emit('abrirLogin') // Grita pro componente pai: "Ei, abre o Login!"
}

// 5. Quando clicar em "Falar com o Responsável"
const irParaWhatsapp = () => {
  // Substitua pelo número da Arena (coloquei o DDD 81 de Pernambuco de exemplo)
  const numero = "5581988780290" 
  const texto = "Olá, gostaria de saber os horários disponíveis para agendar um jogo!"
  window.open(`https://wa.me/${numero}?text=${encodeURI(texto)}`, '_blank')
}

// Expõe a função para o Card conseguir abrir essa tela
defineExpose({
  abrirModal
})
</script>

<template>
  <dialog ref="modalOpcoes" class="meu-modal">
  
    <button class="btn-fechar-x" type="button" @click.prevent="fecharModal">X</button>
    <h2>Você prefere</h2>
    
    <div class="container-opcoes">
      <div class="preencher">
       
        <button type="button" class="agendar-site" @click="irParaSite">Agendar Pelo Site</button>
        <button type="button" class="falar-responsavel" @click="irParaWhatsapp">Falar com o Responsável</button>
      </div>
          
      <p class="texto-dica">É mais rápido agendar diretamente pelo site!</p>
    </div>

  </dialog>
</template>

<style scoped>

dialog[open] {
  display: flex;
  margin: auto; 
  width: 1115px;
  max-width: 90vw; 
  height: 659px;
  max-height: 90vh;
  padding: 80px 100px;
  flex-direction: column;
  justify-content: center;
  gap: 60px; /* Dá um respiro entre o título e o formulário */
  align-items: center;
  border-radius: 21px;
  border: 2px solid rgba(255, 255, 255, 0.85);
  background: linear-gradient(0deg, rgba(2, 20, 2, 0.29) 0%, rgba(11, 122, 11, 0.29) 100%);
  backdrop-filter: blur(12.35px);
  color: white; /* Garante que os textos base sejam brancos */
}

.btn-fechar-x {
  position: absolute;
  top: 30px;
  right: 40px;
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.6);
  font-size: 28px;
  font-family: sans-serif;
  font-weight: bold;
  cursor: pointer;
  transition: color 0.2s ease;
  width: auto; /* Sobrescreve o width: 100% do botão padrão */
  padding: 0;
  box-shadow: none; /* Tira a sombra se o botão base tiver */
}

.btn-fechar-x:hover {
  color: white; /* Acende a cor quando o mouse passa por cima */
}

/* O fundo escuro atrás do modal */
dialog::backdrop {
  background-color: rgba(0, 0, 0, 0.831); 
  backdrop-filter: blur(5px); 
}

h2 {
  text-align: center;
  font-family: 'Montserrat', sans-serif;
  font-size: 96px;
  font-weight: 700;
  line-height: 1; 
  letter-spacing: 2.88px;
  margin: 0;
}

.container-opcoes {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 60px;
    width: 100%;
}

.preencher {
    display: flex;
    width: 100%;
    max-width: 609px;
    flex-direction: column;
    gap: 30px;
    color: rgba(255, 255, 255, 0.90);
    
}

.preencher button {
    display: flex;
    height: 70px;
    padding: 8.139px 11.531px;
    justify-content: center;
    align-items: center;
    gap: 21px;
    align-self: stretch;
    border-radius: 8.331px;
    border: 1px solid #FEFFFA;
    text-align: right;
    font-family: Montserrat;
    font-size: 32px;
    font-style: normal;
    font-weight: 700;
    line-height: 121.888%; /* 39.004px */
    letter-spacing: 4.48px;
    color: rgba(255, 255, 255, 0.891);
}


.preencher button:hover{
    cursor: pointer;
    
}

.preencher .agendar-site {
    background: linear-gradient(96deg, #374814 -22.6%, #61752E 57.13%, #43541C 136.86%);
    
}

.preencher .falar-responsavel {
    background-color: #37481400;
}

.falar-responsavel, .agendar-site {
  transition: all 0.1s ease-in-out;
}

.falar-responsavel:hover, .agendar-site:hover {
  /* Aumenta o botão em exatos 2% (quase imperceptível, mas dá a sensação de clique) */
  transform: scale(1.02);
  border: 1px solid rgba(255, 255, 255, 1);
}

</style>