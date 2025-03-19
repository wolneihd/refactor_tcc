FROM python:3.9-slim

# Atualiza o pip
RUN apt-get update && pip install --upgrade pip

# Instalar ffmpeg e dependências do sistema
RUN apt-get update && \
    apt-get install -y \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /messageHandler

# Copia o arquivo requirements.txt e instala as dependências
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copia o arquivo .env (se necessário)
COPY .env .env

# Exponha a porta 5001
EXPOSE 5001

# Carrega o arquivo .env e inicia a aplicação Telebot
CMD ["python", "main.py"]
