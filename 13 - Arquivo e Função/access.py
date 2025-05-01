import funcoes as f

with open("access.log", "r") as acessos:
    registros = acessos.readlines()

print(len(f.ips(registros)))
print(f.dia_maior_ataque(registros))
print(f.dia_menor_ataque(registros))