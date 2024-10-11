from flask import Flask, render_template, request, redirect, session, flash, url_for, jsonify
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

app = Flask(__name__)

# Configurações do MinIO
MINIO_ENDPOINT = 'localhost:9000'  # Altere conforme necessário
MINIO_ACCESS_KEY = 'minioadmin'
MINIO_SECRET_KEY = 'minioadmin'
MINIO_BUCKET_NAME = 'meu-bucket'

# Inicializa o cliente do S3
s3_client = boto3.client(
    's3',
    endpoint_url=f'http://{MINIO_ENDPOINT}',
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY
)

# Cria o bucket se não existir
try:
    s3_client.create_bucket(Bucket=MINIO_BUCKET_NAME)
except ClientError as e:
    if e.response['Error']['Code'] != 'BucketAlreadyOwnedByYou':
        print(f'Erro ao criar o bucket: {e}')

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

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        s3_client.upload_fileobj(file, MINIO_BUCKET_NAME, file.filename)
        return jsonify({'message': f'File {file.filename} uploaded successfully'}), 200
    except NoCredentialsError:
        return jsonify({'error': 'Credentials not available'}), 403
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
