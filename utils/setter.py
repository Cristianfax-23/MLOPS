import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(encrypted_data, key, iv):
    key_bytes = bytes.fromhex(key)
    iv_bytes = bytes.fromhex(iv)
    encrypted_bytes = base64.b64decode(encrypted_data)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
    return decrypted_bytes.decode('utf-8')

if __name__ == "__main__":

    encryption_key_hex_acces_id = os.getenv('ENCRYPTION_KEY_ACCES_ID')
    iv_acces_id = os.getenv('IV_ACCES_ID')
    encrypted_aws_access_key_id = os.getenv('CIPHERTEXT_ACCES_ID')

    encryption_key_hex_secret_id = os.getenv('ENCRYPTION_KEY_HEX_SECRET')
    iv_secret_id = os.getenv('IV_SECRET')
    encrypted_aws_secret_id = os.getenv('CIPHERTEXT_SECRET')

    print(f"ENCRYPTION_KEY_HEX_ACCES_ID: {encryption_key_hex_acces_id}")
    print(f"IV_ACCES_ID: {iv_acces_id}")
    print(f"CIPHERTEXT_ACCES_ID: {encrypted_aws_access_key_id}")

    aws_access_key_id = decrypt(encrypted_aws_access_key_id, encryption_key_hex_acces_id, iv_acces_id)
    aws_secret_id = decrypt(encrypted_aws_secret_id, encryption_key_hex_secret_id, iv_secret_id)

    with open('aws_access_key_id.txt', 'w') as f:
        f.write(aws_access_key_id)

    with open('aws_secret_key_id.txt', 'w') as f:
        f.write(aws_secret_id)