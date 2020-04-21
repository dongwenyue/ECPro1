'''
@author: wsy
'''
try:
    from .cryptography import x509
    from .cryptography.hazmat.backends import default_backend
    from .cryptography.hazmat._oid import ObjectIdentifier
    from .cryptography.x509.oid import ExtensionOID
except:
    from cryptography import x509
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat._oid import ObjectIdentifier
    from cryptography.x509.oid import ExtensionOID

import base64


class bjca_x509(object):
    _cert = None

    def __init__(self, base64cert):
        try:
            cert = base64.b64decode(base64cert)
        except:
            raise BaseException('Not base64 cert detected')

        self._cert = x509.load_der_x509_certificate(cert, default_backend())

    def getSerialNumber(self):
        if self._cert:
            return self._cert.serial_number
        else:
            raise BaseException('no cert loaded')

    def getExpiredDate(self):
        if self._cert:
            return self._cert.not_valid_after
        else:
            raise BaseException('no cert loaded')

    def getAlgo(self):
        if self._cert:
            return (self._cert.signature_algorithm_oid._name).replace('Encryption', '')
        else:
            raise BaseException('no cert loaded')

    def getBits(self):
        if self._cert:
            return self._cert.public_key().key_size
        else:
            raise BaseException('no cert loaded')

    def getExtensions(self, oid):
        if not self._cert: raise BaseException('no cert loaded')
        _extension = self._cert.extensions.get_extension_for_oid(ObjectIdentifier(oid))
        return _extension.value.value

    def getSubject(self):
        if self._cert:
            subjects = [self._cert.subject._attributes[0]._attributes[0].value,
                        self._cert.subject._attributes[1]._attributes[0].value]
            if 'cn' in subjects: subjects.remove('cn')
            if 'CN' in subjects: subjects.remove('CN')
            return subjects[0]
        else:
            raise BaseException('no cert loaded')
