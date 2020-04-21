import chardet
import codecs


def encode(string, encoding):
    if isinstance(string, str):
        return string.encode(encoding)
    else:
        return string.decode('utf-8').encode(encoding)


def decode(string, encoding):
    if isinstance(string, str):
        return string
    else:
        return string.decode(encoding)


def isUTF8(string):
    if isinstance(string, str):
        return None
    if chardet.detect(string)['encoding'] == 'utf-8':
        return True
    else:
        return False


def isUnicode(string):
    if isinstance(string, str):
        return True
    else:
        return False


def readFile(filename, encoding='utf-8'):
    string = codecs.open(filename, 'r', encoding).read()
    return string


def isJavaException(obj):
    if 'exception' in str(obj.__class__).lower():
        return True
    else:
        return False
