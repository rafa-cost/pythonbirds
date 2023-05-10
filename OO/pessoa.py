#reflexão, se o atributo for igual para todos os objetos , crie um atributo de classe (como aqui no exercicios "Olhos"). Agora se
# o atributo for variar o valor crie um atributo de instancia , ou seja dentro da função

class Pessoa:
    olhos = 2 # atributo de classe
    # "uma quantidade variavel de filhos => '*filhos'"
    def __init__(self, *filhos, nome=None, idade=35):  # abaixo acompanhados do self são os atributos
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)  # aqui no caso seria uma lista

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')  # aqui esta passando renzo como filho, por conta da função acima o __init__
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos# função del esta retirando o atributo 'filhos' de luciano
    luciano.olhos = 1 # aqui só altera o valor do atributo olhos apenas para objeto luciano.
    del luciano.olhos
    print(luciano.__dict__)#o dict é um dicionario , e ira mandar imprimir tudo que esta relacionado a variavel 'luciano' neste caso.
    print(renzo.__dict__)
    Pessoa.olhos = 3 # para alterar o valor do atributo olhos no geral temos que pegar a classe Pessoa. Pq ele é um atributo de classe
    print(Pessoa.olhos)
    print(luciano.olhos)#a gente pode acessar este atributo olhos tanto da classe Pessoa , quanto dos objetos luciano e renzo
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))# e quando imprimir os numeros de id serão todos iguais
