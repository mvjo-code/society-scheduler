
import { ref } from 'vue'

// Essas variáveis ficam FORA da função → são compartilhadas por todo mundo que importar
const estaLogado = ref(!!localStorage.getItem('token'))
const usuario = ref(null) // vai guardar nome, email, etc.

export function useAuth() {

  const fazerLogin = (token) => {
    localStorage.setItem('token', token)
    estaLogado.value = true
    buscarPerfil()
  }

  const fazerLogout = () => {
    localStorage.removeItem('token')
    estaLogado.value = false
    usuario.value = null
  }

  const buscarPerfil = async () => {
    const token = localStorage.getItem('token')
    if (!token) return

    try {
      const resposta = await fetch('https://society-scheduler-y7lb.onrender.com/cliente/me', {
        headers: { Authorization: `Bearer ${token}` },
      })
      if (resposta.ok) {
        usuario.value = await resposta.json()
      } else {
        fazerLogout() // token inválido/expirado
      }
    } catch (e) {
      console.error('Erro ao buscar perfil', e)
    }
  }

  return { estaLogado, usuario, fazerLogin, fazerLogout, buscarPerfil }
}

