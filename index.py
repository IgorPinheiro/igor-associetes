import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3

# import from folders
from app import *
from components import home, sidebar

# Criar estrutura para Store intermediária ==============



# =========  Layout  =========== #
app.layout = dbc.Container([
    # Store e Location 
    dcc.Location(id='url'),                        # Componente que gerencia a URL para navegação de páginas no Dash
    dcc.Store(id='store_intermediate', data={}),   # Armazena dados intermediários a serem compartilhados entre callbacks
    dcc.Store(id='store_adv', data={}),            # Armazena dados avançados para uso em callbacks ou páginas diferentes
    dcc.Store(id='sotore_proc', data={}),          # (Possível erro de digitação no nome) Armazena dados processados ao longo do app
    html.Div(id='div_phantom'),  # Esta div serve como placeholder invisível para armazenar estados ou servir de destino para callbacks sem exibir conteúdo na interface.
    

    # Layout
    dbc.Row([                                                     # Cria uma linha (Row) usando o sistema de grid do Bootstrap
        dbc.Col([                                                # Cria uma coluna (Col) dentro da linha; útil para layout responsivo
            sidebar.layout                                       # Adiciona o layout da barra lateral dentro dessa coluna
        ], md=2, style={'padding': '0px'}),                       # Define o tamanho da coluna para ocupar 2/12 das colunas do grid em telas médias ou maiores
        dbc.Col([  # Cria uma coluna (Col) ocupando 10/12 do grid em telas médias ou maiores
            dbc.Container(  # Cria um container do Bootstrap dentro da coluna para abrigar o conteúdo da página
                id='page-content',  # Define o id do container, que será utilizado para atualizar dinamicamente o conteúdo exibido
                fluid=True,  # Torna o container responsivo (largura total do seu elemento pai)
                style={'jeight': '100%', 'width': '100%', 'pedding-left': '14px'}  # Define o estilo do container (jeight e pedding-left provavelmente são erros de digitação)
            )
        ], md=10, style={'padding': '0px'})  # Define o estilo da coluna (remove o padding lateral)
    ])                                                           # Fecha a declaração da linha

], fluid=True)



# ======= Callbacks ======== #
# URL callback to update page content
# Este callback atualiza o conteúdo da página com base na URL atual
@app.callback(                                            # Define um callback do Dash
    Output('page-content', 'children'),                   # Saída: atualiza a propriedade 'children' do componente com id 'page-content'
    Input('url', 'pathname')                              # Entrada: escuta alterações na propriedade 'pathname' do componente com id 'url'
)
def render_page_content(pathname):                        # Função que determina o que mostrar com base no path da URL
    # Verifica qual página foi solicitada pela URL
    if pathname == '/home' or pathname == '/':           # Se o path for '/home' ou '/', ou seja, página inicial
        return home.layout                                # Retorna o layout da página inicial
    # Adicione outros caminhos de página conforme necessário
    return dbc.Container([
        html.H1(f"404: Página: {pathname} não encontrada"),
        ])         # Se o path não corresponder, exibe mensagem de erro 404


# Dcc.Store back to file


if __name__ == '__main__':
    app.run(debug=True)
