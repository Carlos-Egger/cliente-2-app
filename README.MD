# cliente-2-app

Processador de CSV com cálculo de média de idade, desenvolvido como parte de um desafio técnico sobre integração de pipelines centralizadas com GitHub Actions.

## 🔧 Descrição

A aplicação lê um arquivo `usuarios.csv`, calcula a média de idade dos usuários, e fornece testes com `pytest` para validar o cálculo.

## ⚙️ Pipelines

Este repositório utiliza templates centralizados a partir de [`empresa-pipelines`](https://github.com/sua-org/empresa-pipelines), via `workflow_call`:

- `pipeline_testes_empresa.yml`: executa os testes automatizados.
- `pipeline_build_empresa.yml`: constrói e publica a imagem Docker da aplicação.

