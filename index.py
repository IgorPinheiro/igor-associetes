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
    

    # Layout
    dbc.Row([                                                     # Cria uma linha (Row) usando o sistema de grid do Bootstrap
        dbc.Col([                                                # Cria uma coluna (Col) dentro da linha; útil para layout responsivo
            sidebar.layout                                       # Adiciona o layout da barra lateral dentro dessa coluna
        ], md=2)                                                 # Define o tamanho da coluna para ocupar 2/12 das colunas do grid em telas médias ou maiores
    ])                                                           # Fecha a declaração da linha

], fluid=True)



# ======= Callbacks ======== #
# URL callback to update page content


# Dcc.Store back to file


if __name__ == '__main__':
    app.run(debug=True)
