import math
import secrets
from sympy import randprime, isprime

# --- pick primes in [100, 1000] ---
p = randprime(100, 1000)
q = randprime(100, 1000)
while q == p:
    q = randprime(100, 1000)

N = p * q
M = (p - 1) * (q - 1)

# random e in [3, M] with gcd(e, M)=1


def rand_coprime(limit, m):
    while True:
        k = secrets.randbelow(limit - 2) + 3  # 3..limit
        if math.gcd(k, m) == 1:
            return k

# random x in [2, N] with gcd(x, N)=1


def rand_coprime_to_N(N):
    while True:
        x = secrets.randbelow(N - 1) + 2  # 2..N
        if math.gcd(x, N) == 1:
            return x


e = rand_coprime(M, M)
x = rand_coprime_to_N(N)

# generate 200 bits via LSBs of RSA powering
bits = []
y = x
for _ in range(200):
    bits.append(str(y & 1))
    y = pow(y, e, N)

bit_string = "".join(bits)

print(f"p={p}\nq={q}\ne={e}\nN={N}\nM={M}")
for i in range(0, 200, 50):
    print(bit_string[i:i+50])
