# web3-api
API em Python para comunicação com Smart Contracts implantados em blockchain do Ethereum

# Requerimentos para instalação:
    - Python versão 3.10 ou superior

# Processo de instalação e execução
### 1. Após clonar este repositório rode o comando abaixo para criar um ambiente virtual próprio na pasta raiz do projeto:

```sh
python -m venv venv/
```

```sh
source venv/bin/activate
```

Obs.: Para encerrar o ambiente (recomendado após finalizar o uso):

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

Obs.: Caso tudo tenha ocorrido conforme esperado o resultado pode ser visto no navegador nas urls: http://127.0.0.1:8000 ou http://127.0.0.1:8000/docs