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
    @staticmethod
#isso é um decorator do tipo metodo estatico, em geral eles ficam em cima de funções e metodos, depois de inserido o decorater, vc vai definir o
# metodo como normalmente vc faria , utilizando a palavra reservada def e dando um nome para o metodo, vamos chamar de 'metodo estatico',
# quando eu utilizo um metodo estatico : ele funciona simplesmente como uma função atrelado a classe Pessoa(neste codigo) , e por isso ele
# independe do objeto , então vc não precisa receber nenhum atributo. E nesse caso sua logica aqui , deve fazer algum calculo, que independa
# tanto da classe quanto do objeto. O que diferencia do metodo de classe que quando executamos "print(Pessoa.cumprimentar(luciano))", fomos
#obrigados a passar o objeto "luciano".Ja no metodo estatico não precisa. Pq se o atributo não for encontrado no objeto o python vai procurar
# na classe.
    def metodo_estatico():
        return 42

    @classmethod # isso é um decorathor de metodo de classe , nesse caso vc vai querer ter acesso a classe que esta executando este metodo
    # e quando crio essa classe, que eu vou chamar aqui de nome e atributos de classe, o pycharm ja coloca o 'cls' como parametro, justamente
    # alusão as consoantes da palavra class. Este cls faz alusão a classe que esta executando pessoa. Vc deve usar o @classmethod cls, quando vc
    # quer acessar dados da propria classe. Aqui nos nos vamos formatar e retornar uma string, vamos colocar o nome da classe 'cls' e vamos
    #acessar o atributo olhos da classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'
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
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())






