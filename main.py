from flask import Flask, make_response, request

from aws_s3.aws_s3 import download_file, check_object, upload_file, list_objects
from file_renamer.rename_files import renomear_arquivos

app = Flask(__name__)


@app.route('/files/rename', methods=['GET'])
def local_file_rename():
    headers = {"Content-Type": "application/json"}

    req_content = request.json

    return make_response(
        renomear_arquivos(
            req_content['directory'],
            req_content['old_filenames'],
            req_content['new_filenames']
        ),
        200,
        headers
    )


@app.route('/files/download', methods=['GET'])
def download_aws_file():
    headers = {"Content-Type": "application/json"}

    req_content = request.json

    if check_object(req_content['file_key']):
        return make_response(
            download_file(req_content['file_key'],
                          req_content['directory']
                          ),
            200,
            headers
        )

    return make_response(
        'Arquivo inexistente',
        404,
        headers
    )


@app.route('/files/upload', methods=['POST'])
def upload_to_aws():
    headers = {"Content-Type": "application/json"}

    return make_response(
        upload_file(request.form['file_key'], request.files['file']),
        200,
        headers
    )


@app.route('/files/list', methods=['GET'])
def list_bucket_objects():
    headers = {"Content-Type": "application/json"}

    return make_response(
        list_objects(),
        200,
        headers
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
