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
        html.H5(id='div_error2')
    ]),
    dbc.ModalFooter([
        dbc.Button('Cancelar', id='cancel_button_new_lawyer', color='danger'),
        dbc.Button('Salvar', id='save_button_new_lawyer', color='success'),
    ]), 
], id='modal_new_lawyers', size='lg', is_open=False)




# ======= Callbacks ======== #
# Callback para adicionar novos advogados
@app.callback(
    Output('store_adv', 'data'),
    Output('div_error2', 'children'),
    Output('div_error2', 'style'),
    Input('save_button_new_lawyer', 'n_clicks'),
    State('store_adv', 'data'),
    State('name_lawyer', 'value'),
    State('oab_lawyer', 'value'),
    State('cpf_lawyer', 'value'),   
)
def new_lawyer(n_save, dataset, name, oab, cpf):
    erro = []
    style= {}
    error_style = {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
    success_style = {'margin-bottom': '15px', 'color': 'green', 'text-shadow': '2px 2px 8px #000000'}
    
    if n_save:
        
        if None in [name, oab, cpf]:
            return dataset, ['Todos os campos são obrigatórios para registro!'], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
        
        # Coleta o dataset e transforma em Data Frame e trata se vir vazio
        COLUMNS = ['name', 'oab', 'cpf']
        df_new_lawyer = pd.DataFrame(dataset or [], columns=COLUMNS)
        print(df_new_lawyer.values)
        # Validação dos Campos
        if (
            not df_new_lawyer.empty
            and 'name' in df_new_lawyer.columns
            and name.strip().lower() in df_new_lawyer['name'].str.lower().values
        ):
            return dataset, [f'Nome {name} já cadastrada'], error_style

        if (
            not df_new_lawyer.empty
            and 'oab' in df_new_lawyer.columns
            and oab in df_new_lawyer['oab'].values
        ):
            return dataset, [f'OAB {oab} já cadastrado'], error_style

        if (
            not df_new_lawyer.empty
            and 'cpf' in df_new_lawyer.columns
            and cpf in df_new_lawyer['cpf'].values
        ):
            return dataset, [f'Nome {cpf} já cadastrado'], error_style
        
        # Inserção normal: df_new_lawyer.loc[df_new_lawyer.shape[0]] = [name, oab, cpf]
        # Inserção performática:
        new_row = pd.DataFrame(
            [{'name': name, 'oab': oab,'cpf': cpf}]
        )
        
        df_new_lawyer = pd.concat(
            [df_new_lawyer, new_row],
            ignore_index=True
        )
        
        dataset = df_new_lawyer.to_dict('records')
       
        # Retorna para o Store
        return dataset, [f' [+] - Advogado OAB: {oab} cadastrado com sucesso'], success_style
    
    return dataset, erro, style
    
    
        