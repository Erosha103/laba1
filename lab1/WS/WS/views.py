
from django.shortcuts import render
from Crypto.Cipher import AES

def encrypt_cfb(plaintext, key, iv):
    cipher = AES.new(key.encode(), AES.MODE_CFB, iv.encode(), segment_size=128)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext.hex()

def encrypt(request):
    if request.method == 'POST':
        plaintext = request.POST['plaintext']
        key = request.POST['key']
        iv = request.POST['iv']
        ciphertext = encrypt_cfb(plaintext, key, iv)

    else:
        ciphertext = {}
    return render(request, 'encrypt.html', ciphertext)
