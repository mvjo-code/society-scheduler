from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta, timezone


# motor de criptografia
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash_senha(senha: str) -> str:
    """
    Recebe a senha limpa e devolve o hash embaralhado.
    """
    return pwd_context.hash(senha)

def verificar_senha(senha_limpa: str, senha_hash: str) -> bool:
    """
    Compara a senha que o usuário digitou no login com o hash salvo no banco.
    Retorna True se baterem, e False se a senha estiver errada.
    """
    return pwd_context.verify(senha_limpa, senha_hash)



# GERAÇÃO DE CRACHÁ DIGITAL

SECRET_KEY = "DFJKEJFEFEFHDHFEFQAJKDJKGJJFEUIQOEJFLFEIJDFJEIJEIJFIEJIQJFAJFÉIHIOE"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20 # O token (crachá) vai durar 1 hora (60 minutos)

def criar_token_de_acesso(dados: dict):
    """
    Recebe um dicionário com os dados do usuário (ex: {"sub": "matheus@email.com"}) 
    e devolve o token JWT assinado.
    """
    copia_dados = dados.copy()
    
    # 2. Calcula que horas o token vai vencer (Hora atual + 20 minutos)
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # 3. Adiciona a data de validade dentro do token (o campo 'exp' é um padrão do JWT)
    copia_dados.update({"exp": expiracao})
    
    # 4. Assina o token com a sua chave secreta
    token_jwt = jwt.encode(copia_dados, SECRET_KEY, algorithm=ALGORITHM)
    
    return token_jwt




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="cliente/login")

def obter_usuario_atual(token: str = Depends(oauth2_scheme)):
    """
    O 'Segurança da Porta'. Ele pega o token, verifica se é falso ou 
    se está vencido, e devolve o e-mail que está lá dentro.
    """
    try:
        # Tenta abrir o token usando a sua chave secreta
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        
        if email is None:
            raise HTTPException(status_code=401, detail="Credenciais inválidas.")
            
        return email
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="O seu token expirou. Faça login novamente.")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido.")

