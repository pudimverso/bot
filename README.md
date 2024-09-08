# Pudimatrix

## Um bot do discord para o serivdor do Pudimverso

<div align="center">
    <p align="center">
        <a href="https://github.com/pudimverso/bot">
            <img alt="Repo size" src="https://img.shields.io/github/repo-size/pudimverso/bot?style=for-the-badge&logo=github&color=FAB387&logoColor=FAB387&labelColor=302D41"/></a>
        <a href="https://github.com/pudimverso/bot/issues">
            <img alt="Issues" src="https://img.shields.io/github/issues/pudimverso/bot?style=for-the-badge&logo=githubactions&color=F9E2AF&logoColor=F9E2AF&labelColor=302D41"></a>
        <a href="https://github.com/pudimverso/bot/commits/main/">
            <img alt="Commits" src="https://img.shields.io/github/commit-activity/t/pudimverso/bot?style=for-the-badge&logo=conventionalcommits&color=09CDAA&logoColor=F9E2AF&labelColor=302D41"></a>
        <a href="https://discord.gg/yK25rv2E56">
            <img alt="Discord" src="https://img.shields.io/discord/1216042188996083774?style=for-the-badge&logo=discord&color=B4BEFE&logoColor=B4BEFE&labelColor=302D41"></a>
    </p>
</div>

> [!WARNING]
**Esse bot não está pronto para ser usado em produção. Não recomendamos o uso do mesmo no estado atual.**

## Sobre
Pudimatrix é um bot que procura trazer diversão e utilidade para o servidor do Pudimverso.

Ele foi feito para implementar uma variedade de features para o servidor, incluindo moderação, suporte, utilidade e múlitplos comandos de diversão.

## Stack
- Python 3.12 juntamente da bibliteca discord.py
- PDM Para gerenciamento de dependências
- PostgreSQL Juntamente do SQLAlchemy
- Linting e formatação atráves do ruff
- Justfile para facilitar execução de comandos CLI

### Pré-requisitos
- Python 3.12
- [PDM](https://pdm-project.org/latest/)
- Optional: [Just](https://github.com/casey/just/)

### Como instalar
Assumindo que você tenha os pré requisitos, siga esses passos para começar a desenvolver para o projeto:

1. Clone o repositório
```bash
git clone https://github.com/pudimverso/bot && cd bot
```

2. Instale as dependências
```bash
pdm install
```

3. Ative o ambiente virtual
```bash
eval "$(pdm venv activate in-project)"
```

4. Copie o arquivo `.env.sample` para `.env` e preencha os valores nescessários
```bash
cp .env.sample .env
```

5. Inicie o bot!
```bash
python -m bot
```

![Metrics](https://repobeats.axiom.co/api/embed/06d2b47f2171aae6f6a09b680caefe9af1607a26.svg "Repobeats analytics image")

[![Contributors](https://contrib.rocks/image?repo=pudimverso/bot)](https://github.com/pudimverso/bot/graphs/contributors)
