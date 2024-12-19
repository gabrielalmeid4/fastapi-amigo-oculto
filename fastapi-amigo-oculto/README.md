# 🎉 Amigo Oculto (Versão no framework FastAPI)

## 🛠️ Tecnologias Utilizadas

As principais tecnologias utilizadas neste projeto são:

- **[FastAPI](https://fastapi.tiangolo.com/)**: Um framework moderno, rápido (alta performance) e fácil de usar para construir APIs com Python.
- **[asyncpg](https://github.com/MagicStack/asyncpg):** Um driver PostgreSQL assíncrono, rápido e eficiente, utilizado para gerenciar a interação com o banco de dados.

## 🚀 Funcionalidades
- Login na aplicação utilizando middleware customizado e aplicando conceitos de arquitetura limpa.
- Realização de sorteio
- Cadastro de eventos
- Separação clara das responsabilidades no código para facilitar a manutenção e evolução do sistema.

## Diferenciais
- Não utiliza ORM, faz as buscas utilizando o driver do postgresql assíncrono

## 📂 Estrutura do Projeto

Este projeto foi construído com base nos princípios da arquitetura limpa, adaptado à estrutura de diretórios a seguir:

```bash
.
├── authentication  # Middleware e lógica de autenticação
├── config          # Configurações globais do projeto
├── models          # Definição de modelos e esquemas
├── presentation    # Lógica relacionada às rotas e controladores
├── providers       # Serviços externos ou helpers do sistema
├── repositories    # Interação direta com o banco de dados
├── services        # Regras de negócio e casos de uso
├── main.py         # Arquivo principal de inicialização da aplicação
└── venv            # Ambiente virtual (não incluído no controle de versão)
