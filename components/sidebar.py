import dash
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State, ALL
import dash_bootstrap_components as dbc

import json
import pandas as pd

from components import modal_novo_processo, modal_novo_advogado, modal_advogados
from app import app

# ========= Layout ========= #
layout = dbc.Container([
    modal_novo_processo.layout,
    modal_novo_advogado.layout,
    modal_advogados.layout,
    
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1(
                    'FRANÇA', style=({'color': 'yellow'})
                )
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.H1(
                    'ASSOCIATE', style=({'color': 'white'})
                )
            ])
        ]),
    ], style={'padding-top': '50px', 'margin-bottom': '100%'}, className='text-center'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            
        ])
    ])
    
])
    


# ======= Callbacks ======== #
# Abrir Modal New Lawyer


# Abrir Modal Lawyers
