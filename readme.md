# Aplicação de Categorizar e Responder Feedbacks de Usuários com IA (Groq)

Esta aplicação tem como objetivo categorizar e responder feedbacks de usuários utilizando IA (Groq). A solução envolve um sistema completo com frontend, backend e integração com diversos dispositivos e canais de comunicação.

## Tecnologias Utilizadas

### Frontend
- **Angular**: Framework utilizado para o desenvolvimento da interface de usuário.

### Totem de Atendimento
- **ESP-32 (C++)**: Utilizado para capturar e processar feedbacks de usuários.

### Banco de Dados
- **MySQL**: Sistema de banco de dados utilizado para armazenar informações.

### Canal de Comunicação
- **Telegram (Python)**: Canal de comunicação com os usuários via bot do Telegram.

### Backend
- **Python**: Utilizado para o desenvolvimento da lógica de backend, incluindo integração com o canal de comunicação e processamento de feedbacks.

### Inteligência Artificial
- **Groq**: A IA utilizada para categorizar e responder automaticamente aos feedbacks dos usuários.

## Como Rodar a Aplicação

### Requisitos

- Docker
- Docker Compose

### Passos para Execução

1. Clone este repositório:
   ```bash
   git clone https://github.com/wolneihd/refactor_tcc.git
   ```

2. Para rodar a aplicação, execute o seguinte comando:
   ```bash
   docker-compose up --build
   ```

   Esse comando irá construir as imagens necessárias e iniciar os contêineres da aplicação.

3. Após a execução, a aplicação estará disponível para uso, com o frontend rodando no ambiente configurado e a integração com o canal de Telegram e IA funcionando.

## Estrutura do Projeto

A estrutura do repositório está organizada da seguinte forma:

```
/frontend                # Código do frontend em Angular
/backend                 # Código do backend em Python
/totem                   # Código do totem de atendimento em C++ (ESP-32)
/database                # Scripts de configuração do MySQL
/docker                  # Arquivos Docker e Docker Compose
```