import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_keypair():
    p = random_prime(100, 200)
    q = random_prime(200, 300)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while not is_prime(e) or phi % e == 0:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def random_prime(start, end):
    prime = random.randint(start, end)
    while not is_prime(prime):
        prime = random.randint(start, end)
    return prime

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1

def encrypt(message, public_key):
    e, n = public_key
    cipher_text = pow(message, e, n)
    return cipher_text

def decrypt(cipher_text, private_key):
    d, n = private_key
    message = pow(cipher_text, d, n)
    return message

# Пример использования:

# Шаг 1: Генерация ключей
public_key, private_key = generate_keypair()
print("Открытый ключ:", public_key)
print("Закрытый ключ:", private_key)

# Шаг 2: Шифрование
message = 2155
cipher_text = encrypt(message, public_key)
print("Зашифрованное сообщение:", cipher_text)

# Шаг 3: Расшифровка
decrypted_message = decrypt(cipher_text, private_key)
print("Расшифрованное сообщение:", decrypted_message)
