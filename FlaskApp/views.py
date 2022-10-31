"""
Routes and views for the flask application.
"""

import pandas as pd
import numpy as np

from datetime import datetime
from flask import render_template
from flask import request
from FlaskApp import app

@app.route('/')
def input():
    """Отображает форму ввода данных"""
    return render_template(
        'index.html',
        title='Ввод данных'
    )

    
   

