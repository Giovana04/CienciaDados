#ex1
from typing import Counter
from numpy import median
from math import dist


nome = "gigis"
idade = 21
altura = 1.68
cidade = "sp"

print(f"{nome}, {idade} anos, {altura}m - {cidade}")


#ex2
l = [1,2,3,4,5]
l.append(6)
l.append(7)
l.pop(3)
l.sort()
print(l)

#ex3
l.insert(3, 4)
media = (median(l))
print(media)

#ex4
impares = [x*2-1 for x in range(11)]
print(impares)

#ex5
contatos = {
    "pedro": 1111111111,
    "julia" : 222222222222,
    "bea" : 3333333333
}
for c in contatos.items(): 
    print(c)
    
#ex6
c1 = (10,3)
c2 = (1,20)
dis = dist(c1,c2)
print(dis)

#ex7
frase = "asduiiu iuydw456 iuytdfghj"
print(Counter(frase))

#ex8
def estatistica(n):
    dif = {
        "media": sum(n)/len(n),
        "max": max(n),
        "min": min(n)
    } 
    return dif

n = [int(x) for x in input("digite numeros separados por espaço: ").split()]

#ex9
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade 
            return f"venda feita na quantidade {quantidade}, restam {self.estoque}"
    
    def repor(self, quantidade):
        self.estoque += quantidade
        return f"reposição feita na quantidade {quantidade}, estoque atual {self.estoque}"
    
    def exibir(self):
        return f"produto: {self.nome}, preço: {self.preco}, estoque {self.estoque}"

p1 = Produto("caneta", 2.5, 100)
print(p1.exibir())
print(p1.vender(10))
print(p1.repor(20))
print(p1.exibir())

class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir(self):
        return f"veiculo: {self.marca} {self.modelo}, ano: {self.ano}"
    
class carro(veiculo):
    def __init__(self, marca, modelo, ano, tipoHabitacao):
        super().__init__(marca, modelo, ano)
        self.tipoHabitacao = tipoHabitacao
        
    def exibir(self):
        return f"carro: {self.marca} {self.modelo}, ano: {self.ano}, tipo de habitacao: {self.tipoHabitacao}"
    
class moto(veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo
        
    def exibir(self):
        return f"moto: {self.marca} {self.modelo}, ano: {self.ano}, tipo: {self.tipo}"
        
c1 = carro("ford", "ka", 2020, "hatch")
m1 = moto("honda", "cb500", 2019, "esportiva")
print(c1.exibir())
print(m1.exibir())