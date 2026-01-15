import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from dash import dash_table
from dash.dash_table.Format import Group

from app import app
from components import home

# ======== Layout ========= #
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Cadastar Novo Advogado')),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                html.Div(id='table_lawyer', className='dbc')
            ])
        ])
    ]),
    dbc.ModalFooter([
        dbc.Button('Sair', id='quit_button', color='danger'),
        dbc.Button('Novo', id='lawyer-new', color='secundary')
    ])
    
], id='modal_lawyer', size='lg', is_open=False)
            


# ====== Callbacks ======= #
# Tabela com os advogados da empresa
@app.callback(
Output('table_lawyer', 'children'),
Input('store_lawyer', 'data')
)
def table(data):
   
    df = pd.DataFrame(data)
    df = df.fillna('-')
    
    return dash_table.DataTable(
                id='datatable-lawyers',
                columns=[{"name": col, "id": col} for col in df.columns],
                data=df.to_dict('records'),
                page_size=10,
                page_current=0
            )