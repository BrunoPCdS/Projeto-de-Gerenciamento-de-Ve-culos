# Projeto de Gerenciamento de Veículos

Este projeto é um sistema simples para gerenciar veículos e marcas, incluindo operações CRUD (Criar, Ler, Atualizar, Deletar) e visualizações de dados.

## Funcionalidades

-   **Gerenciamento de Veículos**: Incluir, listar, alterar e excluir veículos.
-   **Gerenciamento de Marcas**: Incluir, listar e excluir marcas.
-   **Geração de Gráficos**: Visualização gráfica de dados de veículos e marcas.
-   **Visualização Web**: Uma interface web para visualizar todos os veículos cadastrados, incluindo suas fotos.

## Como Usar

### Instalação

1.  Certifique-se de ter Python instalado (versão 3.x).
2.  Clone este repositório.
3.  Instale as dependências:
    ```bash
    pip install -r requeriments.txt
    ```
4.  Certifique-se de que seu banco de dados PostgreSQL está configurado e as credenciais em `config.py` estão corretas.

### Execução

1.  Execute o script principal:
    ```bash
    python main.py
    ```
2.  Siga as opções do menu no terminal.

### Visualização Web

1.  No menu principal, selecione a opção para "Abrir visualização na Web".
2.  Um servidor web será iniciado e seu navegador padrão abrirá a página com a lista de veículos.

## Estrutura do Projeto

-   `main.py`: Ponto de entrada do programa, menu principal.
-   `config.py`: Configurações do banco de dados.
-   `app.py`: Aplicação Flask para visualização web.
-   `templates/index.html`: Modelo HTML para a página web de veículos.
-   `operacoes/`: Contém os módulos para operações CRUD e geração de gráficos.
    -   `marca/`: Operações relacionadas a marcas.
    -   `veiculo/`: Operações relacionadas a veículos.
-   `requeriments.txt`: Lista de dependências do projeto.



### Menu Principal

<img src="imgs\menu1.png" alt="Menu Principal" width="600px"/>

### Tabelas (Listagem de Veículos/Marcas)

#### Tabela de Veículos
<img src="imgs\menu2.png" alt="Tabela de Veículos" width="600px"/>

#### Tabela de Marcas
<img src="imgs\menu3.png" alt="Tabela de Marcas" width="600px"/>

### Página Web (Visualização de Veículos)

<img src="imgs\menu4.png" alt="Página Web de Veículos" width="600px"/>

### Gráficos

#### Gráfico de Veículos
<img src="imgs\menu5.png" alt="Gráfico de Veículos" width="600px"/>

#### Gráfico de Marcas
<img src="imgs\menu6.png" alt="Gráfico de Marcas" width="600px"/>
---
projeto by Bruno Corrêa
---

