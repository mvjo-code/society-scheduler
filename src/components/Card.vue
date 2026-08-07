<script setup>

    defineProps({
        titulo: String,
        horario1: String,
        horario2: String,
        valor1: String,
        valor2: String
    })
</script>

<template>
    <div class="card">
        <h2 class="titulo">{{ titulo }}</h2>
        <div class="conteudo">
            <div class="beneficios">
                <p>Valor por Hora</p>
                <p>Todos os Benefícios Incluídos</p>
                <p>Bola Oficial e Coletes</p>
            </div>
            <div class="horarios">
                <div class="horario">
    

                    <p>{{ horario1 }}</p>
                    <p>R$ {{ valor1 }}</p>
                </div>
                <div class="horario" v-if="horario2">
                    <p>{{ horario2 }}</p>
                    <p>R$ {{ valor2 }}</p>
                </div>
            </div>
            <button class="agendar">Agendar</button>
        </div>

    </div>

</template>

<style scoped>

.titulo {
    margin: 0;
    margin-bottom: 10px;
    color: rgba(255, 255, 255, 0.85);
    text-align: center;
    font-family: Montserrat;
    font-size: 1.699em;
    font-style: italic;
    font-weight: 900;
    letter-spacing: 0.64px;
}

.card {
    margin: 0;
    display: flex;
    width: 300px;
    height: auto;
    padding: 35px 44px 76px 44px;
    padding-bottom: 50px;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    flex-shrink: 0;
    align-self: stretch;
    border-radius: 21px;
    border: 2px solid rgba(255, 255, 255, 0.85);
    background: rgba(2, 20, 2, 0.29);
    backdrop-filter: blur(12.350000381469727px);

    transition: all 0.3s ease; /* Transição suave para o efeito de hover */
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 
        0px 5px 20px -5px rgba(255, 255, 255, 0.185),  /* Luz interna mais focada */
        0px 30px 50px -10px rgba(254, 255, 252, 0.101); /* Luz externa mais espalhada */
}

.conteudo {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    align-self: stretch;
    gap: 30px;
    flex: 1;
}

.beneficios {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    align-self: stretch;
    color: rgba(255, 255, 255, 0.94);
    font-family: Montserrat;
    font-size: 10px;
    font-style: normal;
    font-weight: 700;
    line-height: 95%;
    letter-spacing: 0.9px;
}

.horarios { 
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    align-self: stretch;
}

.horario {
    display: flex;
    justify-content: space-between;
    align-items: center;
    align-self: stretch;
}

.agendar {
    margin: 0;
    color: white;
    display: flex;
    padding: 8.139px 11.531px;
    width: 100%;
    justify-content: center;
    align-items: center;
    gap: 3.391px;
    border-radius: 8.331px;
    border: 1px solid #fefffa60;
    box-shadow: 0 0 13.8px 0 rgba(101, 128, 48, 0.58);
    color: rgba(255, 255, 255, 0.90);
    text-align: right;
    font-family: Montserrat;
    font-size: 24px;
    font-style: normal;
    font-weight: 700;
    line-height: 121.888%; /* 29.253px */
    letter-spacing: 3.36px;
    margin-top: auto;

        /* Fundo dinâmico */
    background: linear-gradient(
        96deg, 
        rgba(81, 107, 11, 0.268) 0%,     
        rgba(102, 133, 16, 0.822) 25%,   
        rgba(118, 153, 22, 0.379) 50%,   
        rgba(111, 149, 8, 0.245) 75%,    
        rgba(82, 107, 11, 0.40) 100%    
    );
    border: 2px solid transparent;
    background-size: 200% auto;
    background-position: 0% center;
    transition: all 0.2s ease; /* Transição suave para o efeito de hover */

}

.agendar:hover {
    border: 2px solid #b6ffa495;
    background-position: 50% center; 
}

@media (max-width: 768px) {
    .card {
        width: 37%;
        min-height: 300px;
        padding: 20px;
        margin: 0 auto;
        background-color: rgba(24, 255, 24, 0.29);
    }

    .titulo {
        font-size: 1.2em;
    }

    .beneficios {
        font-size: 8px;
    }

    .agendar {
        font-size: 18px;
        padding: 6px 8px;
    }
}



</style>