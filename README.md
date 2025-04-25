# Projeto Calculadora com CI no GitHub

Este é um projeto Python simples que implementa uma calculadora com operações básicas. O projeto possui testes automatizados usando `pytest` e está configurado com GitHub Actions para integração contínua.

## Estrutura

- `calc/`: Código da calculadora
- `tests/`: Testes automatizados
- `.github/workflows/ci.yml`: Pipeline de CI
- `requirements.txt`: Dependências
- `pytest.ini`: Configuração do Pytest

## Como funciona a CI

Toda vez que houver um `push` ou `pull request` na branch `main`, os testes automatizados serão executados automaticamente.

A pipeline está definida em `.github/workflows/master.yml`.

## Tarefas executadas na pipeline

- Instalação do Python
- Instalação das dependências
- Execução dos testes com Pytest

## Observação

Não é necessário runner local — a execução ocorre totalmente dentro da infraestrutura do GitHub.
