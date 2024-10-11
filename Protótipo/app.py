from flask import Flask, render_template, request, redirect, session, flash, url_for, jsonify
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escolhaRito')
def escolhaRito():
    return render_template('escolhaRito.html')

@app.route('/loginADM')
def loginADM():
    return render_template('loginADM.html')

@app.route('/loginTI')
def loginTI():
    return render_template('loginTI.html')

@app.route('/penhora')
def penhora():
    return render_template('penhora.html')

@app.route('/prisao')
def prisao():
    return render_template('prisao.html')

@app.route('/registroADM')
def registroADM():
    return render_template('registroADM.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@app.route('/PG')
def PG():
    return render_template('PG.html')


if __name__ == '__main__':
    app.run(debug=True)
