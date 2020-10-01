from flask import Flask, make_response, request

from file_renamer.rename_files import renomear_arquivos

app = Flask(__name__)


@app.route('/api/local-management/files/rename', methods=['GET'])
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
