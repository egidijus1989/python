import random
n = int(input('n=...'))
sk = random.randint(-n, n)
sk2 = random.random()
sk1=random.randrange(1, n, 2)
raide = random.choice(['a', 'b', 'c'])

print(sk)
print(sk1)
print(raide)
print(int(sk2*100))