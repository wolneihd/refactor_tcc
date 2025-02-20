FROM python:3.9-slim

# Atualiza o pip
RUN apt-get update && pip install --upgrade pip

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o arquivo .env (se necessário)
COPY .env .env

# Define o diretório de trabalho da aplicação Flask
WORKDIR /api

# Exponha a porta 5000
EXPOSE 5000

# Carrega o arquivo .env e inicia a aplicação Flask
CMD ["python", "api.py"]
