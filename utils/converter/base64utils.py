import base64


def b64encode(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.b64encode(data).decode()


def b64decode(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.b64decode(data)
