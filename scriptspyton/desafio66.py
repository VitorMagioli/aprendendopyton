n = s = c = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1

print(f'Foram digitados {c} números.')
print(f'A soma foi {s}.')