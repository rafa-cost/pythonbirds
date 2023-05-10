class Pessoa:
#"uma quantidade variavel de filhos => '*filhos'"
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)#aqui no caso seria uma lista
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')#aqui esta passando renzo como filho, por conta da função acima o __init__
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)