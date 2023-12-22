import binascii

def assembly_patcher(file, old_hex, new_hex):
    with open(file, 'rb') as f:
        content = f.read()
    old_bytes = binascii.unhexlify(old_hex)
    new_bytes = binascii.unhexlify(new_hex)
    mod_content = content.replace(old_bytes, new_bytes)
    with open(file, 'wb') as f:
        f.write(mod_content)

assembly_patcher('Assembly-CSharp.dll', '398ee33f', '60e51840')
