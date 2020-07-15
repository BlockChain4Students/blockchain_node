from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme


def generate_key_pair(node_id):

    key = RSA.generate(2048)
    file_priv = "crypto/" + str(node_id) + "-private.pem"  # Find better way to do these names
    f = open(file_priv,'wb')
    f.write(key.export_key('PEM'))
    f.close()

    file_pub = "crypto/" + str(node_id) + "-public.pem"
    f = open(file_pub, 'wb')
    f.write(key.publickey().export_key('PEM'))
    f.close()


def sign_hash(h, node_id):
    file_priv = "crypto/" + str(node_id) + "-private.pem"
    f = open(file_priv, 'r')
    priv_key = RSA.import_key(f.read())  # Read private key from file
    signer = PKCS115_SigScheme(priv_key)
    signature = signer.sign(h)
    return signature


def verify_sig(hc, signature, node_id):
    file_pub = "crypto/" + str(node_id) + "-public.pem"
    f = open(file_pub, 'r')
    pub_key = RSA.import_key(f.read())  # Read public key from file
    signer = PKCS115_SigScheme(pub_key)
    signer.verify(hc, signature)
