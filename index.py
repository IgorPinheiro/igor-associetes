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
    dcc.Location(id='url'),
    dcc.Store(id='store_intermediate', data={}),
    dcc.Store(id='store_adv', data={}),
    dcc.Store(id='sotore_proc', data={}),
    

    # Layout
    

], fluid=True)



# ======= Callbacks ======== #
# URL callback to update page content


# Dcc.Store back to file


if __name__ == '__main__':
    app.run(debug=True)
