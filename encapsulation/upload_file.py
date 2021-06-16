import json
import requests


def upload_zip(filename, product_id, group_id, token, file_path, serverurl):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = requests.post(
        f'{serverurl}/storage/upload-tasks/zip',
        json={
            "filename": filename,
            "group_id": group_id,
            "product_id": product_id,
        },
        headers=headers)
    s = data.content.decode()
    body = json.loads(s)
    if body['message'] != 'Success':
        return body['message']
    else:
        token_data = data.json()
        token_data = token_data.get("data")
        oss_host = token_data.get('oss_host')

        host_url = 'http://{}'.format(oss_host)
        token_data['signature'] = token_data.pop('Signature')

        file_obj = open(file=file_path, mode='rb')
        files = {'file': (filename, file_obj)}
        try:
            data = requests.post(url=host_url, data=token_data, files=files)
            return data.content
        finally:
            file_obj.close()
