# web3-api
API em Python para comunicação com Smart Contracts implantados em blockchain do Ethereum

## Requerimentos para instalação:
    - Python versão 3.10 ou superior

## Processo de instalação e execução
### 1. Após clonar este repositório rode o comando abaixo para criar um ambiente virtual próprio na pasta raiz do projeto:

```sh
python -m venv venv/
```

```sh
source venv/bin/activate
```

**Importante!** Para encerrar o ambiente (recomendado após finalizar o uso):

```sh
deactivate
```

### 2. Para importar as dependências do projeto rodar:

```sh
pip install -r requirements.txt
```

### 3. Para executar rode o comando:

```sh
fastapi dev src/api/main.py
```

---
Caso tudo tenha ocorrido conforme esperado o resultado pode ser visto no navegador nas urls: http://127.0.0.1:8000 ou http://127.0.0.1:8000/docs

Através da URL http://127.0.0.1:8000/docs é possível fazer as chamadas aos endpoints

### 4. Será necessário subir uma rede local blockchain, <br>Também será necessário fazer o deploy do contrato HelloHardhat<br>Para isto pode ser usado o projeto no github abaixo:

https://github.com/danpatrocinio/hardhat-hello-world

**Importante!** O Projeto hardhat-hello-world deve ser clonado em um diretório lado a lado com este projeto<br>
para que seja possível ler a abi do contrato e o endereço de deploy dele.

