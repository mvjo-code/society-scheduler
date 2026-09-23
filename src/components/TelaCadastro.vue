<script setup>
import { ref } from 'vue'

const modalCadastro = ref(null)
const emit = defineEmits(['abrirLogin'])

// Uma variável reativa pra cada campo do formulário
const nome = ref('')
const telefone = ref('')
const cidade = ref('')
const bairro = ref('')
const rua = ref('')
const numero = ref('')
const email = ref('')
const senha = ref('')
const confirmarSenha = ref('')
const erro = ref('')

const abrirModal = () => {
  modalCadastro.value.showModal()
}

const fecharModal = () => {
  modalCadastro.value.close()
}

const irParaLogin = () => {
  fecharModal()
  emit('abrirLogin')
}

const processarCadastro = async () => {
  erro.value = ''

  // Confere ANTES de gastar uma requisição com o backend
  if (senha.value !== confirmarSenha.value) {
    erro.value = 'As senhas não coincidem.'
    return
  }

  try {
    const resposta = await fetch('https://society-scheduler-y7lb.onrender.com/cliente/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',   // essa rota é JSON normal, não form
      },
      body: JSON.stringify({
        nome: nome.value,
        telefone: telefone.value,
        cidade: cidade.value,
        bairro: bairro.value,
        rua: rua.value,
        n_casa: numero.value,
        email: email.value,
        senha_hash: senha.value,   // manda a senha pura, o backend deve hashear
      }),
    })

    if (!resposta.ok) {
      const dadosErro = await resposta.json()
      console.log(dadosErro) // ajuda a ver o motivo exato do 422, se acontecer
      erro.value = 'Não foi possível cadastrar. Confira os dados.'
      return
    }

    // Cadastro deu certo → manda direto pra tela de login
    fecharModal()
    emit('abrirLogin')

  } catch (e) {
    erro.value = 'Não foi possível conectar ao servidor.'
  }
}

defineExpose({
  abrirModal
})
</script>

<template>
  <dialog ref="modalCadastro" class="meu-modal">
  
    <button class="btn-fechar-x" type="button" @click.prevent="fecharModal">X</button>
    <h2>Cadastro</h2>
    
    <form @submit.prevent="processarCadastro">
    
      <div class="preencher">
        <input class="input-padrao" type="text" v-model="nome" placeholder="Nome" required />
        <input class="input-padrao" type="text" v-model="telefone" placeholder="Telefone" required />
        <input class="input-padrao" type="text" v-model="cidade" placeholder="Cidade" required />
        <input class="input-padrao" type="text" v-model="bairro" placeholder="Bairro" required />
        <input class="input-padrao" type="text" v-model="rua" placeholder="Rua" required />
        <input class="input-padrao" type="text" v-model="numero" placeholder="Número casa / Apartamento" required />
        <input class="input-padrao" type="email" v-model="email" placeholder="Email" required />
        <input class="input-padrao" type="password" v-model="senha" placeholder="Senha" required />
        <input class="input-padrao" type="password" v-model="confirmarSenha" placeholder="Confirmar Senha" required />
      </div>

      <p v-if="erro" style="color: #ff8080;">{{ erro }}</p>
        
      <div class="botoes-acao">
        <button class="btn-entrar" type="submit">CADASTRAR</button>
      </div>
      
      <p class="texto-cadastro">Já tem uma conta? <a href="#" @click.prevent="irParaLogin">Entrar</a></p>
      
    </form>

  </dialog>
</template>


<style scoped>
/* O modal em si (com altura adaptada e rolagem para não quebrar em telas menores) */
dialog[open] {
  display: flex;
  margin: auto; 
  width: 1115px;
  max-width: 90vw; 
  height: auto; 
  min-height: 659px;
  max-height: 90vh;
  padding: 60px 100px; /* Padding vertical levemente reduzido para otimizar espaço */
  flex-direction: column;
  justify-content: flex-start; /* Melhor para quando tem scroll */
  gap: 40px; 
  align-items: center;
  border-radius: 21px;
  border: 2px solid rgba(255, 255, 255, 0.85);
  background: linear-gradient(0deg, rgba(2, 20, 2, 0.29) 0%, rgba(11, 122, 11, 0.29) 100%);
  backdrop-filter: blur(12.35px);
  color: white; 
  overflow-y: auto; /* Garante que é possível rolar para baixo se a tela for pequena */
}

/* Scrollbar customizada para o modal (opcional, mas fica mais elegante) */
dialog[open]::-webkit-scrollbar {
  width: 8px;
}
dialog[open]::-webkit-scrollbar-thumb {
  background-color: rgba(255, 255, 255, 0.3);
  border-radius: 10px;
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

/* O fundo escuro atrás do modal */
dialog::backdrop {
  background-color: rgba(0, 0, 0, 0.831); 
  backdrop-filter: blur(5px); 
}

h2 {
  text-align: center;
  font-family: 'Montserrat', sans-serif;
  font-size: 80px; /* Um pouco menor que no login para equilibrar o espaço vertical */
  font-weight: 700;
  line-height: 1; 
  letter-spacing: 2.88px;
  margin: 0;
  margin-top: 20px;
}

/* O formulário centraliza tudo que tem dentro */
form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px; /* Reduzido de 60 para 40 para acomodar mais campos */
  width: 100%;
}

/* Transformado em Grid para colocar os campos lado a lado e economizar altura */
.preencher {
  display: grid;
  grid-template-columns: 1fr 1fr; /* Duas colunas de tamanhos iguais */
  gap: 20px 30px; /* 20px de espaçamento vertical, 30px horizontal */
  width: 100%;
  max-width: 800px; /* Levemente mais largo para as duas colunas respirarem */
}

/* Faz o primeiro input (Nome) e o Email ocuparem a linha inteira, caso queira */
.preencher input[type="email"],
.preencher input[placeholder="Nome Completo"] {
  grid-column: span 2;
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
}

/* Muda a cor do texto do placeholder para um cinza clarinho */
.input-padrao::placeholder {
  color: rgba(83, 83, 83, 0.6);
  font-size: 14px;
}

/* Caixa que segura o botão de cadastrar */
.botoes-acao {
  display: flex;
  width: 100%;
  max-width: 609px;
  gap: 20px;
}

/* Estilo base dos botões */
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
}

button:hover {
  opacity: 0.9; 
}

/* Botão principal de CADASTRAR */
.btn-entrar {
  width: 100px;
  height: 45px;
  border: 1px solid #FEFFFA;
  background: linear-gradient(96deg, #374814 -22.6%, #61752E 57.13%, #43541C 136.86%);
}

/* Estilo para a frase e o link de login na base do modal */
.texto-cadastro {
  color: rgba(255, 255, 255, 0.7); 
  font-family: 'Montserrat', sans-serif;
  font-size: 16px;
  margin-top: -10px; 
  margin-bottom: 20px;
}

.texto-cadastro a {
  color: white; 
  font-weight: bold;
  text-decoration: none; 
}

.texto-cadastro a:hover {
  color: rgba(255, 255, 255, 0.828); 
}
</style>