from Crypto.PublicKey import RSA

new_key = RSA.generate(2048, e=65537)
public_key = new_key.publickey().exportKey("BOB")
private_key = new_key.exportKey("NOT_BOB")
print public_key
print private_key