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
                    'PATRICK', style=({'color': 'yellow'})
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
    ], style={'padding-top': '50px', 'margin-bottom': '30%'}, className='text-center'),
    html.Hr(),
    
    dbc.Row([
        dbc.Col([
            dbc.Nav([
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), '\tINÍCIO'], href='/home', active=True, style={'text-align': 'left'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-plus-circle dbc'), '\tPROCESSOS'], id='process_button', href='/home', active=True, style={'text-align': 'left'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-user-plus dbc'), '\tADVOGADOS'],id='lawyers_button', href='/home', active=True, style={'text-align': 'left'})),
            ], vertical="lg", pills=True, fill=True)
        ])
    ])
    
], style={'height': '100vh', 'padding': '0px', 'position': 'sticky', 'top': 0, 'background-color': '#232423'})
    


# ======= Callbacks ======== #
# Abrir Modal New Lawyer
@app.callback(
    Output('modal_new_lawyers', 'is_open'),
    Input('lawyer_new', 'n_clicks'),
    Input('cancel_button_new_lawyer', 'n_clicks'),
    State('modal_new_lawyers', 'is_open')
)
def toggle_modal_new_lawyer(n_open, n_cancel, is_open):
    if n_open or n_cancel:
        return not is_open
    return is_open

# Abrir Modal Lawyers
@app.callback(
    Output('modal_lawyer', 'is_open'),
    Input('lawyers_button', 'n_clicks'),
    Input('quit_button', 'n_clicks'),
    Input('lawyer_new', 'n_clicks'),
    State('modal_lawyer', 'is_open')
)
def toggle_modal_lawyer(click_lawyers_button, click_quit_button, click_lawyer_new, is_open):
    if click_lawyers_button or click_quit_button or click_lawyer_new:
        return not is_open
    return is_open