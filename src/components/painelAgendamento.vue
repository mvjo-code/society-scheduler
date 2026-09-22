<script setup>
import { ref, computed } from 'vue'

const modalAgendar = ref(null)
const emit = defineEmits(['agendado'])

const data = ref('')          // ex: "2026-09-15"
const horaInicio = ref('')    // ex: "19:00"
const duracao = ref(1)        // em horas, mínimo 1
const erro = ref('')
const sucesso = ref(null)     // vai guardar a resposta do backend (preço, etc.)
const carregando = ref(false)

const abrirModal = () => {
  // reseta o formulário toda vez que abrir
  data.value = ''
  horaInicio.value = ''
  duracao.value = 1
  erro.value = ''
  sucesso.value = null
  modalAgendar.value.showModal()
}

const fecharModal = () => {
  modalAgendar.value.close()
}

// Monta as datas completas (início e fim) a partir do que o usuário escolheu
const montarDataHora = (dataStr, horaStr, horasParaSomar) => {
  // dataStr = "2026-09-15", horaStr = "19:00"
  const [ano, mes, dia] = dataStr.split('-').map(Number)
  const [hora, minuto] = horaStr.split(':').map(Number)

  // O mês no JS começa em 0 (Janeiro = 0), por isso "mes - 1"
  const dataObj = new Date(ano, mes - 1, dia, hora, minuto)
  dataObj.setHours(dataObj.getHours() + horasParaSomar)

  // Formata manualmente pra "YYYY-MM-DDTHH:mm:ss", sem conversão de fuso (evita bug de horário)
  const pad = (n) => String(n).padStart(2, '0')
  return `${dataObj.getFullYear()}-${pad(dataObj.getMonth() + 1)}-${pad(dataObj.getDate())}T${pad(dataObj.getHours())}:${pad(dataObj.getMinutes())}:00`
}

const confirmarAgendamento = async () => {
  erro.value = ''
  sucesso.value = null

  if (!data.value || !horaInicio.value) {
    erro.value = 'Escolha a data e o horário.'
    return
  }

  const inicio = montarDataHora(data.value, horaInicio.value, 0)
  const fim = montarDataHora(data.value, horaInicio.value, Number(duracao.value))

  carregando.value = true

  try {
    const token = localStorage.getItem('token')

    const resposta = await fetch('http://localhost:8000/agendamento/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        data_hora_inicio: inicio,
        data_hora_final: fim,
        status: 'confirmado',
      }),
    })

    const dados = await resposta.json()

    if (!resposta.ok) {
      // O backend manda o motivo em "detail" (choque de horário, fora do expediente, etc.)
      erro.value = dados.detail || 'Não foi possível agendar.'
      return
    }

    sucesso.value = dados // tem o preço, id, datas confirmadas
    emit('agendado', dados)

  } catch (e) {
    erro.value = 'Não foi possível conectar ao servidor.'
  } finally {
    carregando.value = false
  }
}

defineExpose({
  abrirModal
})
</script>

<template>
  <dialog ref="modalAgendar" class="meu-modal">

    <button class="btn-fechar-x" type="button" @click.prevent="fecharModal">X</button>
    <h2>Agendar Jogo</h2>

    <form @submit.prevent="confirmarAgendamento" v-if="!sucesso">
      <div class="preencher">
        <label>
          Data
          <input class="input-padrao" type="date" v-model="data" required />
        </label>

        <label>
          Horário de início
          <input class="input-padrao" type="time" v-model="horaInicio" required />
        </label>

        <label>
          Duração (horas)
          <input class="input-padrao" type="number" v-model="duracao" min="1" max="4" required />
        </label>
      </div>

      <p v-if="erro" style="color: #ff8080;">{{ erro }}</p>

      <div class="botoes-acao">
        <button class="btn-entrar" type="submit" :disabled="carregando">
          {{ carregando ? 'Agendando...' : 'Confirmar Agendamento' }}
        </button>
      </div>
    </form>

    <!-- Tela de sucesso -->
    <div v-else class="confirmacao">
      <p>Jogo agendado com sucesso!</p>
      <p>Valor: R$ {{ sucesso.preco }}</p>
      <button class="btn-entrar" @click="fecharModal">Fechar</button>
    </div>

  </dialog>
</template>

<style scoped>

dialog[open] {
  display: flex;
  margin: auto;
  width: 1115px;
  max-width: 90vw;
  height: auto;
  min-height: 500px;
  max-height: 90vh;
  padding: 80px 100px;
  flex-direction: column;
  justify-content: center;
  gap: 40px;
  align-items: center;
  border-radius: 21px;
  border: 2px solid rgba(255, 255, 255, 0.85);
  background: linear-gradient(0deg, rgba(2, 20, 2, 0.29) 0%, rgba(11, 122, 11, 0.29) 100%);
  backdrop-filter: blur(12.35px);
  color: white;
}

dialog::backdrop {
  background-color: rgba(0, 0, 0, 0.831);
  backdrop-filter: blur(5px);
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
  width: auto;
  padding: 0;
  box-shadow: none;
}

.btn-fechar-x:hover {
  color: white;
}

h2 {
  text-align: center;
  font-family: 'Montserrat', sans-serif;
  font-size: 64px;
  font-weight: 700;
  line-height: 1;
  letter-spacing: 2.88px;
  margin: 0;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
  width: 100%;
}

.preencher {
  display: flex;
  width: 100%;
  max-width: 500px;
  flex-direction: column;
  gap: 25px;
}

label {
  display: flex;
  flex-direction: column;
  gap: 8px;
  color: rgba(255, 255, 255, 0.9);
  font-family: 'Montserrat', sans-serif;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.input-padrao {
  display: flex;
  height: 45px;
  width: 100%;
  padding: 10px 20px;
  font-size: 18px;
  color: white;
  border-radius: 8.33px;
  border: 1px solid #FEFFFA;
  background: rgba(42, 42, 42, 0.475);
  outline: none;
  color-scheme: dark; /* deixa o ícone de calendário/relógio branco, combinando com o fundo escuro */
}

.botoes-acao {
  display: flex;
  width: 100%;
  max-width: 500px;
  gap: 20px;
}

button {
  display: flex;
  flex: 1;
  height: 55px;
  justify-content: center;
  align-items: center;
  font-size: 18px;
  font-weight: bold;
  color: white;
  border-radius: 8.33px;
  cursor: pointer;
  border: none;
}

.btn-entrar {
  width: 100%;
  height: 55px;
  border: 1px solid #FEFFFA;
  background: linear-gradient(96deg, #374814 -22.6%, #61752E 57.13%, #43541C 136.86%);
}

.btn-entrar:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-entrar:hover:not(:disabled) {
  opacity: 0.9;
}

.confirmacao {
  text-align: center;
  color: white;
  display: flex;
  flex-direction: column;
  gap: 30px;
  align-items: center;
  font-family: 'Montserrat', sans-serif;
}

.confirmacao p:first-child {
  font-size: 28px;
  font-weight: 700;
}

.confirmacao p:nth-child(2) {
  font-size: 20px;
  color: #b6ffa4;
}

</style>