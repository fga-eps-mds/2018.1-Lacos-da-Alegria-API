
[![Travis branch](https://img.shields.io/travis/fga-gpp-mds/2018.1-Lacos-da-Alegria.svg)](https://github.com/fga-gpp-mds/2018.1-Lacos-da-Alegria)

[![Read the Docs](https://img.shields.io/readthedocs/pip.svg)](https://github.com/fga-gpp-mds/2018.1-Lacos-da-Alegria)
[![Maintainability](https://api.codeclimate.com/v1/badges/d4e2fff36d305c96179e/maintainability)](https://codeclimate.com/github/fga-gpp-mds/2018.1-Lacos-da-Alegria/maintainability)
[![GitHub issues](https://img.shields.io/github/issues/fga-gpp-mds/2018.1-Lacos-da-Alegria.svg)](https://github.com/fga-gpp-mds/2018.1-Lacos-da-Alegria)
[![license](https://img.shields.io/github/license/fga-gpp-mds/2018.1-Lacos-da-Alegria.svg)](https://github.com/fga-gpp-mds/2018.1-Lacos-da-Alegria)

![logo-wide-lacos](http://oi66.tinypic.com/2lxvvw7.jpg)

Uma API open source escrita em Python, utilizando Django Rest Framework. É desenhado para ser extendível, escalável, simples e mutável.

Esta API é desenhada para comunicar-se, utilizando uma arquitetura REST entre um banco de dados relacional de forma independente uma aplicação Django Rest de forma otimizada para Ionic Framework, que é o framework escolhido para desenvolvimento da aplicação Laços de Alegria, feita pela mesma equipe. Esta aplicação ainda busca ser facilmente convertida para Java Spring Boot para servir a arquitetura original do website da Laços de Alegria.

## Laços de Alegria
De acordo com a psicóloga Dayana Lima Dantas Valverde (2010), “Embora a palavra hospital venha da palavra hospitalidade, muitos pacientes não o consideram como local hospedeiro. O bem estar psicológico do paciente não é o principal objetivo do atendimento e sim prestar socorro àquele que tem um sofrimento relacionado com o biológico e orgânico”.

É a partir disso que a Laços da Alegria age para tratar do bem estar mental e social dos pacientes de hospitais. Os voluntários vão de corações abertos para as visitações a fim de proporcionar boa companhia para os presentes nos locais visitados. Os voluntários fazem as visitas caracterizados e proporcionam abordagens diferenciadas levando-se em consideração a cultura regional. Tendo como exemplo as “piadas” ocorridas em um local, podem não ser bem recebidas em um outro. Assim, são tomados cuidados especiais em cada visitação.

As visitas ocorrem em grupos de cerca de 20 pessoas, as quais são subdivididas em grupos de doutores - são os mais experientes nas visitações -, apoio - são responsáveis pela interação inicial com os pacientes - e novatos - os que estão fazendo sua primeira visita. Atualmente a ONG Laços da Alegria proporciona suas visitas a 7 hospitais em todo o Distrito Federal. As visitas a hospitais ocorrem semanalmente e quinzenalmente às outras organizações. Por ser uma organização sem fins lucrativos, não são cobradas taxas para participar ou promover o projeto.


## Vantagens da utilização da LaçosAPI

* É open source
* Fácil de modificar e adaptar
* Fácil de instalar
* Feito com Docker e Docker Compose para deploy simples
* Builds automatizadas
* Análise comparativa entre a implementação híbrida e nativa no Android

## Instalação

A instalação é feita baseada na imagem oficial do Python para Docker, porém com algumas depedências instaladas, entre elas, o Django e o Django REST.

### Docker Compose

Para rodar a API basta ter o Docker e o Docker Compose instalados e então rodar os seguintes comandos:

```bash
# Clonar este repositório 
git clone https://github.com/fga-gpp-mds/2018.1-Lacos-da-Alegria-API.git

# Construir o projeto
sudo docker-compose -f local.yml build

# Criar as migrações
sudo docker-compose -f local.yml run --rm django python3 manage.py makemigrations

# Rodar as migrações
sudo docker-compose -f local.yml run --rm django python3 manage.py migrate

# Criar um super usuário
sudo docker-compose -f local.yml run --rm django python3 manage.py createsuperuser

# Testar o linting
sudo docker-compose -f local.yml run --rm django flake8

# Verificar os testes unitários
sudo docker-compose -f local.yml run --rm django py.test

# Rodar o servidor
sudo docker-compose -f local.yml up

# Para acessar, abra no navegador em:
localhost:8000/api
```



# Contribuindo

Contribuir para a aplicação é muito simples e fortemente encorajado! Então se você conhece um pouquinho sobre Python ou APIs REST você estará ajudando não só a equipe de desenvolvimento, como a Laços de Alegria de uma forma muito simples.

Todos os contribuidores, incluindo a equipe de desenvolvimento e os fundadores do projeto da aplicação móvel, contribuem usando o seguinte processo:

* Fork o projeto principal para sua conta (se você não for um contribuidor da equipe de desenvolvimento)
* Crie uma branch para features
* Realize suas alterações ou acréscimos ao projeto
* Crie um pull request para o projeto principal
* Testes e a cobertura dos testes serão checados automaticamente
* Um dos responsáveis pelo projeto irá revisar suas alterações e mesclará seu pull request

Para mais informações acesse a [documentação para contribuição]()
Caso precise de ajuda, crie uma issue, também seguindo o [padrão estabelecido]!

-------

## Contribuidores

Este projeto existe graças aos contribuidores. [Seja um deles!](/docs/contributing.md).

### Equipe de Gerência
|Membro                         |Email                           |Github                                              |
|-------------------------------|--------------------------------|----------------------------------------------------|
|Cauê Mateus Oliveira           |cauemateus@hotmail.com          |[caue96](https://github.com/caue96)                 |
|Julliana do Couto Almeida      |julliana.coutoalmeida@gmail.com |[jullianaa](https://github.com/Jullianaa)           |
|Lucas Oliveira                 |lucasoliveira2306@gmail.com     |[lucaaas](https://github.com/lucaaas)               |
|Luiz Guilherme Santos da Silva |do.guilherme@hotmail.com        |[luizguilherme5](https://github.com/luizguilherme5) |

### Equipe de Desenvolvimento
|Membro                         |Email                           |Github                                              |
|-------------------------------|--------------------------------|----------------------------------------------------|
|João Vítor Morandi             |joao.lemos4000@gmail.com        |[joaovitorml](https://github.com/joaovitorml)       |
|Luciano dos Santos Silva       |lucianosz.ls3@gmail.com         |[lucianosz7](https://github.com/lucianosz7)         |
|Rafael Makaha Gomes Ferreira   |rafael.makaha@gmail.com         |[rafaelmakaha](https://github.com/rafaelmakaha)     |
|Renan Schadt                   |renanschadt@gmail.com           |[renan601](https://github.com/renan601)             |
|Rômulo Vinícius de Souza       |romulovinicius10@gmail.com      |[RomuloSouza](https://github.com/RomuloSouza)       |
|Sara Silva                     |saracsas2@gmail.com             |[silvasara](https://github.com/silvasara)           |
