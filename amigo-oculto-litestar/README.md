# 🎉 Amigo Oculto  ( Versão no framework litestar )

## 🛠️ Tecnologias Utilizadas

As principais tecnologias utilizadas neste projeto são:

- **[Litestar](https://litestar.dev/)**: Um framework web leve e flexível para construção de APIs rápidas e escaláveis.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: Um ORM (Object-Relational Mapper) do tipo data mapper, utilizado para gerenciar a interação com o banco de dados.

## 🚀 Funcionalidades
- Login na aplicação utilizando middleware e aplicando conceitos de arquitetura limpa

## 📂 Estrutura do Projeto
Este projeto foi construído com base nos princípios da arquitetura limpa, com camadas bem definidas para facilitar a compreensão e manutenção do código. A estrutura de diretórios é a seguinte:

```bash
.
├── src
│   ├── domain       # Camada de Domínio: Regras de negócio e entidades centrais
│   ├── application  # Camada de Aplicação: Casos de uso e orquestração
│   ├── infrastructure # Camada de Infraestrutura: Persistência e detalhes técnicos
│   └── interface    # Camada de Interface: Endpoints da API (Litestar)
├── docs             # Documentação do projeto
└── tests            # Testes automatizados
```
