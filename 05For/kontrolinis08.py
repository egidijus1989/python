b = int(input('kiek prinoko braskiu pirma diena...'))
d = int(input('kiek braskiu siandien prinoko daugiau negu praejusia diena...'))
n = int(input('dienu skaicius...'))
sum = b

for i in range(1, n):
    b = b + d
    sum = sum + b
print(f'Per 3 dienas prinoko {sum} braskes')