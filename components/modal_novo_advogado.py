import dash
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from app import app

# ========= Layout ========= #
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Adicionar Um Advogado')),
    
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                dbc.Label('[+] ADV OAB'),
                dbc.Input(id='oab_lawyer', placeholder='Apenas os números da OAB', type='number'),
            ], sm='12', md=6),
            dbc.Col([
                dbc.Label('[+] ADV CPF'),
                dbc.Input(id='cpf_lawyer', placeholder='Apenas os números do CPF', type='number'),
            ], sm='12', md=6),
        ]),
        
        dbc.Row([
            dbc.Col([
                dbc.Label('[+] ADV Nome'),
                dbc.Input(id='name_lawyer', placeholder='Nome Completo do advogado...', type='text')
            ]),
        ]),
        html.H5(['Essa é a nossa div de ERRO'], id='div_error2')
    ]),
    dbc.ModalFooter([
        dbc.Button('Cancelar', id='cancel_button_new_lawyer', color='danger'),
        dbc.Button('Salvar', id='save_button_new_lawyer', color='success'),
    ]), 
], id='modal_new_lawyers', size='lg', is_open=False)




# ======= Callbacks ======== #
# Callback para adicionar novos advogados

