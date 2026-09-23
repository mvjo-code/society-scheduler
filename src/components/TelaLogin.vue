<script setup>
import { ref } from 'vue'
import { useAuth } from './useAuth.js'
const { fazerLogin } = useAuth()  

const modalLogin = ref(null)
const emit = defineEmits(['abrirCadastro', 'loginSucesso'])

// Variáveis que faltavam
const email = ref('')
const senha = ref('')
const erro = ref('')

const abrirModal = () => {
  modalLogin.value.showModal()
}

const fecharModal = () => {
  modalLogin.value.close()
}

const irParaCadastro = () => {
  fecharModal()
  emit('abrirCadastro')
}

// Só UMA função processarLogin agora
const processarLogin = async () => {
  erro.value = ''

  try {
    const corpo = new URLSearchParams()
    corpo.append('username', email.value)
    corpo.append('password', senha.value)
    corpo.append('grant_type', 'password')

    const resposta = await fetch('https://society-scheduler-y7lb.onrender.com/cliente/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: corpo,
    })

    if (!resposta.ok) {
      erro.value = 'Email ou senha inválidos.'
      return
    }

    const dados = await resposta.json()
    fazerLogin(dados.access_token) // Chama a função do useAuth para salvar o token e buscar o perfil

    emit('loginSucesso')
    fecharModal()

  } catch (e) {
    erro.value = 'Não foi possível conectar ao servidor.'
  }
}

defineExpose({
  abrirModal
})
</script>


<template>
  <dialog ref="modalLogin" class="meu-modal">
  
    <button class="btn-fechar-x" type="button" @click.prevent="fecharModal">X</button>
    <h2>Faça Login</h2>
    
    <!-- O formulário agora abraça tanto os inputs quanto os botões -->
    <form @submit.prevent="processarLogin">
    
      <div class="preencher">
        <input class="input-padrao" type="email" v-model="email" placeholder="Login/Email" required />
        <input class="input-padrao" type="password" v-model="senha" placeholder="Senha" required />
      </div>

      <p v-if="erro" class="erro">{{ erro }}</p>
        
      <div class="botoes-acao">
        <button class="btn-entrar" type="submit">ENTRAR</button>
      </div>
      <p class="texto-cadastro">Ainda não tem uma cnnta? <a href="#" @click.prevent="irParaCadastro" >Cadastrar-se</a></p>
      
    </form>

  </dialog>
</template>

<style scoped>
/* O modal em si (mantive suas configurações de vidro/blur) */
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

/* O formulário agora centraliza tudo que tem dentro */
form {
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
}

/* Unifiquei as classes login e senha aqui */
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

/* Muda a cor do texto do placeholder (Login/Senha) para um cinza clarinho */
.input-padrao::placeholder {
  color: rgba(83, 83, 83, 0.6);
  font-size: 14px;
}

/* Caixa que segura os botões lado a lado */
.botoes-acao {
  display: flex;
  width: 100%;
  max-width: 609px;
  gap: 20px;
}

/* Estilo base dos botões */
button {
  display: flex;
  flex: 1; /* Faz os botões dividirem o espaço igualmente */
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

/* Botão principal de ENTRAR */
.btn-entrar {
  width: 100px;
  height: 45px;
  border: 1px solid #FEFFFA;
  background: linear-gradient(96deg, #374814 -22.6%, #61752E 57.13%, #43541C 136.86%);
  }

/* Botão secundário de CANCELAR (Fica transparente só com a borda para não roubar a atenção) */
.btn-cancelar {
  border: 1px solid rgba(255, 255, 255, 0.5);
  background: transparent;
}

/* Estilo para a frase e o link de cadastro na base do modal */
.texto-cadastro {
  color: rgba(255, 255, 255, 0.7); /* Deixa a pergunta levemente cinza */
  font-family: 'Montserrat', sans-serif;
  font-size: 16px;
  margin-top: -30px; /* Puxa o texto um pouco mais pra perto do botão */
}

.texto-cadastro a {
  color: white; /* Deixa o "Cadastrar-se" em destaque */
  font-weight: bold;
  text-decoration: none; /* Tira o sublinhado padrão */
}

.texto-cadastro a:hover {
  color: rgba(255, 255, 255, 0.828); /* Efeito suave ao passar o mouse */
}


</style>