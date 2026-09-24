<script setup>
import { ref, onMounted, computed } from 'vue'
import { useAuth } from './useAuth.js';
import painelAgendamento from './painelAgendamento.vue';
import BannerJogo from './bannerJogo.vue';

const { usuario, fazerLogout } = useAuth()

const emit = defineEmits(['agendar'])
const refModalAgendamento = ref(null)

const primeiroNome = computed(() => {
    const nome = usuario?.value?.nome?.split(' ')[0] || 'Jogador'
    return nome.charAt(0).toUpperCase() + nome.slice(1)
})

const irParaAgendamento = () => {
    refModalAgendamento.value.abrirModal()
}

const sair = () => {
    fazerLogout()
}

// lógica para buscar agendamentos do usuário
const meusJogos = ref([])
const carregandoJogos = ref(true)

const buscarMeusAgendamentos = async () => {
    try {
        const token = localStorage.getItem('token')
        const resposta = await fetch('https://society-scheduler-y7lb.onrender.com/agendamento/meus', {
            headers: { Authorization: `Bearer ${token}` },
        })

        if (resposta.ok) {
            meusJogos.value = await resposta.json()
        }
    } catch (e) {
        console.error('Erro ao buscar agendamentos', e)
    } finally {
        carregandoJogos.value = false
    }
}

// --- helpers para formatar os dados do jogo pro BannerJogo ---
// obs: ajusta os nomes dos campos (duracao_minutos, instagram) conforme
// o que o seu endpoint /agendamento/meus realmente devolve.
const formatarDia = (isoString) => {
    const data = new Date(isoString)
    return data.toLocaleDateString('pt-BR', { weekday: 'short', day: '2-digit', month: '2-digit' })
        .replace('.', '')
        .toUpperCase()
}

const formatarHorario = (isoString) => {
    const data = new Date(isoString)
    return data.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })
}

const formatarDuracao = (minutos) => {
    if (!minutos) return '1H 00'
    const horas = Math.floor(minutos / 60)
    const min = minutos % 60
    return `${horas}H ${min.toString().padStart(2, '0')}`
}

onMounted(() => {
    buscarMeusAgendamentos()
})
</script>

<template>
    <div class="painel-usuario">
        <div class="cabecalho">
            <h2>Fala, {{ primeiroNome }}!</h2>
            <h3>Meus agendamentos:</h3>
        </div>

        <div class="corpo">
            <div class="coluna-lista">
                <div class="lista-jogos" v-if="!carregandoJogos">
                    <p v-if="meusJogos.length === 0" class="lista-vazia">
                        Você ainda não tem jogos agendados.
                    </p>

                    <BannerJogo v-for="jogo in meusJogos" :key="jogo.id" :titulo="`Jogo de ${primeiroNome}`"
                        :dia="formatarDia(jogo.data_hora_inicio)" :horario="formatarHorario(jogo.data_hora_inicio)"
                        :duracao="formatarDuracao(jogo.duracao_minutos)" />
                </div>

                <p v-else class="lista-vazia">Carregando seus jogos...</p>
            </div>

            <div class="coluna-acoes">
                <button type="button" class="agendar-site" @click="irParaAgendamento">
                    Agendar meu jogo
                    <span class="seta">→</span>
                </button>
                <button type="button" class="sair-conta" @click="sair">Sair</button>
            </div>
        </div>
    </div>

    <painelAgendamento ref="refModalAgendamento" @agendado="buscarMeusAgendamentos" />
</template>

<style scoped>
.painel-usuario {
    background-image: url('../assets/images/fundo_painel_usuario_4.png');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center 100%;
    width: 100vw;
    height: 100vh;
    margin: 0 auto;
    padding: 60px 40px;
    display: flex;
    flex-direction: column;
    gap: 32px;
    color: white;

}

.cabecalho {
    display: flex;
    flex-direction: column;
    gap: 18px;
}

.cabecalho h2 {
    margin: 0;
    font-family: 'Montserrat', sans-serif;
    font-size: 2em;
    font-weight: 700;
    letter-spacing: 0.5px;
    white-space: nowrap;      /* Impede que o texto desça para a linha de baixo */
    overflow: hidden;         /* Esconde o que passar do ecrã */
    text-overflow: ellipsis;  /* Coloca "..." no final do texto cortado */
    max-width: 100%;
}

.cabecalho h3 {
    margin: 0;
    margin-bottom: 1em;
    font-family: 'Montserrat', sans-serif;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: rgba(255, 255, 255, 0.9);
}

.corpo {
    display: flex;
    align-items: center;
    gap: 40px;
}

/* ---------- coluna esquerda: lista com scroll independente ---------- */
.coluna-lista {
    flex: 1;
    min-width: 0;
}

.lista-jogos {
    display: flex;
    flex-direction: column;
    gap: 16px;
    max-height: 340px;
    overflow-y: auto;
    padding-right: 6px;
}

.lista-jogos::-webkit-scrollbar {
    width: 6px;
}

.lista-jogos::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.25);
    border-radius: 999px;
}

.lista-vazia {
    color: rgba(255, 255, 255, 0.7);
    font-family: 'Montserrat', sans-serif;
    font-size: 15px;
}

/* ---------- coluna direita: ações ---------- */
.coluna-acoes {
    flex-shrink: 0;
    width: 240px;
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.coluna-acoes button {
    display: flex;
    height: 56px;
    padding: 0 20px;
    justify-content: center;
    align-items: center;
    gap: 10px;
    border-radius: 999px;
    font-family: 'Montserrat', sans-serif;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.5px;
    cursor: pointer;
    transition: transform 0.15s ease-in-out, border-color 0.15s ease-in-out;
}

.coluna-acoes button:hover {
    transform: scale(1.02);
}

.agendar-site {
    border: 1px solid #fefffa;
    background: linear-gradient(96deg, #374814 -22.6%, #61752e 57.13%, #43541c 136.86%);
    color: rgba(255, 255, 255, 0.95);
}

.agendar-site .seta {
    font-size: 16px;
}

.sair-conta {
    height: 44px;
    border: 1px solid rgba(255, 255, 255, 0.6);
    background: transparent;
    color: rgba(255, 255, 255, 0.85);
    align-self: center;
    width: 140px;
}

.agendar-site:hover,
.sair-conta:hover {
    border-color: #ffffff;
}

/* ---------- responsivo ---------- */
/* ---------- responsivo painel-usuario ---------- */
@media (max-width: 860px) {
    .painel-usuario {
        padding: 40px 16px; /* Reduzimos o padding brutalmente de 40px para 16px nas laterais */
        gap: 20px;
    }

    .corpo {
        flex-direction: column;
        align-items: stretch;
        gap: 24px;
    }

    .coluna-acoes {
        width: 100%;
        flex-direction: row;
        justify-content: space-between; /* Afasta os botões em vez de os centralizar juntos */
    }
    
    .agendar-site {
        flex: 1; /* Faz o botão agendar ocupar o espaço restante */
    }

    .sair-conta {
        align-self: auto;
        width: 80px; /* Reduz a largura do botão sair no telemóvel */
        padding: 0;
    }
    
    /* Reduz o tamanho das fontes no telemóvel */
    .cabecalho h2 {
        font-size: 1.6em;
    }
    .cabecalho h3 {
        font-size: 18px;
    }
}
    
</style>