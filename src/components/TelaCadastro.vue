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
    const resposta = await fetch('http://localhost:8000/cliente/', {
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
        <input class="input-padrao" type="text" v-model="nome" placeholder="Nome Completo" required />
        <input class="input-padrao" type="text" v-model="telefone" placeholder="Telefone" required />
        <input class="input-padrao" type="text" v-model="cidade" placeholder="Cidade" required />
        <input class="input-padrao" type="text" v-model="bairro" placeholder="Bairro" required />
        <input class="input-padrao" type="text" v-model="rua" placeholder="Rua" required />
        <input class="input-padrao" type="text" v-model="numero" placeholder="Número" required />
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

dialog[open] {
  display: flex;
  margin: auto; 
  width: 1115px;
  max-width: 90vw; 
  /* Como o cadastro tem mais campos, a altura pode precisar ficar como 'auto' ou maior */
  height: auto; 
  min-height: 659px;
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

/* Restante das suas classes (btn-fechar-x, input-padrao, btn-entrar, etc...) */
</style>