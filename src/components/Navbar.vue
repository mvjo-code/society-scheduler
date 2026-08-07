<script setup>
import { ref } from 'vue'

// O 'ref' guarda qual é a aba atual. Vamos começar com a 'Home' selecionada.
const abaAtiva = ref('HOME')
</script>

<template>
    <nav class="navegacao">
        <ul class="links">
            <!-- 
              O :class verifica se a abaAtiva é igual ao nome do botão. Se for, ele ganha a classe 'ativo'.
              O @click muda o valor da abaAtiva quando o usuário clica.
            -->
            <li 
                class="link" 
                :class="{ ativo: abaAtiva === 'HOME' }" 
                @click="abaAtiva = 'HOME'"
            >
                HOME
            </li>
            
            <li 
                class="link" 
                :class="{ ativo: abaAtiva === 'ESTRUTURA' }" 
                @click="abaAtiva = 'ESTRUTURA'"
            >
                ESTRUTURA
            </li>
            
            <li 
                class="link" 
                :class="{ ativo: abaAtiva === 'HORÁRIOS' }" 
                @click="abaAtiva = 'HORÁRIOS'"
            >
                HORÁRIOS
            </li>
            
            <li 
                class="link" 
                :class="{ ativo: abaAtiva === 'CONTATO' }" 
                @click="abaAtiva = 'CONTATO'"
            >
                CONTATO
            </li>
        </ul> 
    </nav>
</template>

<style scoped>
    .navegacao {
        
        margin: 0;
        padding: 0;
        display: inline-flex;
        height: 49px;
        width: auto;
        align-items: flex-start;
        align-content: flex-start;
        gap: 63px 45.189px;
        flex-wrap: wrap;

    }

    .links {
        display: flex;
        align-items: center;
        gap: 50px;
        list-style: none;
        margin: 0;
        padding: 0;
        color: rgba(255, 255, 255, 0.938);
        text-align: right;
        font-family: Montserrat;
        font-size: 16px;
        font-style: normal;
        font-weight: 900;
        line-height: normal;
        letter-spacing: 0.948px;
    }

    .link {
        display: flex;
        width: 160px;
        height: 30px;
        padding: 0;
        margin: 0;
        justify-content: center;
        align-items: center;
        border-radius: 35.805px;
        border: 2px solid #6a812980;
        cursor: pointer;
        padding: 3px;
    }

    /* O que acontece quando o usuário passa o mouse (Hover) */
    .link:hover {
        border-color: #91b33580;
        color: white;
    }

    /* O estilo exato do botão quando ele está SELECIONADO */
    .link.ativo {
        padding: 3px;
        display: flex;
        width: 160px;
        height: 30px;
        justify-content: center;
        align-items: center;
        border-radius: 65.764px;
        border: 1.6px solid #ffffff82;
        background: var(--feiche-verde, linear-gradient(96deg, rgba(12, 14, 6, 0.66) 11.15%, #425019 41.05%, rgba(16, 18, 8, 0.64) 136.86%));
        color: rgba(255, 255, 255, 0.998);
        text-align: right;
        font-family: Montserrat;
        font-size: 16px;
        font-style: normal;
        font-weight: 900;
        line-height: normal;
        letter-spacing: 0.948px;
        transition: all 0.3s ease-in-out;
    }

    .link.ativo:hover {
        color: rgba(255, 255, 255, 0.896);
    }

    @media (max-width: 768px) {
        .navegacao {
            flex-direction: row;
            align-items: center;
            justify-content: space-around;
            gap: 20px;
            padding-left: 20px;
            padding-right: 20px;
            }

        .links {
            flex-direction: row;
            gap: 20px;
        }

        .link {
            width: 100px;
            height: 25px;
            font-size: 14px;
        }

        .link.ativo {
            width: 100px;
            height: 25px;
            font-size: 14px;
        }

    }

@media (max-width: 480px) {
        .navegacao {
            flex-direction: row;
            align-items: center;
            gap: 10px;
        }

        .links {
            flex-direction: row;
            width: 100%;
            gap: 30px;
        }

        .link {
            width: 50px;
            height: 3%;
            font-size: 7px;
        }

        .link.ativo {
            width: 50px;
            height: 3%;
            font-size: 7px;
        }
    }
</style>