# Protected by Irsyad Team 🔒
import zlib, base64, hashlib, sys, os
from Crypto.Cipher import AES

def anti_debug():
    if sys.gettrace():
        sys.exit()
    if "PYCHARM" in os.environ or "VSCODE" in os.environ:
        sys.exit()

def dynamic_key(secret, salt):
    return hashlib.sha256(secret.encode() + salt).digest()

def unpad(data):
    return data.rstrip(b"\0")

def aes_decrypt(data, key):
    raw = base64.b64decode(data)
    iv = raw[:16]
    enc = raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc))

anti_debug()

gmbmimzn = b'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'
exzsxblj = b'{\xd0\x1bAZ\xe2\xb8\x82*M\x91\xb2\xba~@$'

# 🔥 AUTO KEY (NO PASSWORD PROMPT)
_secret = "IrsyadTeam_PublicRelease_2026"
key = dynamic_key(_secret, exzsxblj)

exec(zlib.decompress(aes_decrypt(gmbmimzn, key)))
