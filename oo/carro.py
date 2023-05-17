'''Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

    Motor
    Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

    Atributo de dado velocidade
    Método acelerar, que deverá incremetar a velocidade de uma unidade
    Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

    Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
    Método girar_a_direita
    Método girar_a_esquerda


       N
    O     L
       S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
'''

class Carro: #classe carro, bem dizer esta classe não teria funcionalidade, mas por conta dos ultimos testes do enunciado, tivemos que fazer
    #mas bem dizer não tem funcionalidade, a não ser para imprimir os ultimos testes de classe Carro. Aqui a gente mesclou as outras 2 classes
    #direcao e motor , com a classe carro
    def __init__(self, direcao, motor): #aqui os metodo dander init
        self.motor = motor #aqui os parametros
        self.direcao = direcao
    def calcular_velocidade(self): # metodo calcular velocidade
        return self.motor.velocidade
    def acelerar(self):
        self.motor.acelerar()
    def frear(self):
        self.motor.frear()
    def calcular_direcao(self):
        return self.direcao.valor
    def girar_a_direita(self):
        self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'
class Direcao:
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE} #em vez de colocar if , else ou elif, fizemos o dicionario,
    #esse dicionario indica que , depois de norte é lesta, depois de leste é sul e dai por diante, a ordem que sera impressa na função girar
    # a direita. E a mesma coisa para a lista abaixo e a função tambem.
    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}
    def __init__(self):
        self.valor = NORTE # valor igual a norte, ou seja começara em norte e depois sera alterado pelas funções girar a direita
        # e girar a esquerda.
    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]
class Motor:
    def __init__(self):
        self. velocidade = 0 #velocidade começa a partir de zero
    def acelerar(self):
        self.velocidade += 1 # e sempre acrescenta uma unidade , quando executar a função
    def frear(self):
        self.velocidade -= 2 # quando executar o metodo frear , sempre ira tirar 2 unidades de atributo velocidade
        self.velocidade = max(0, self.velocidade) #esse código faz com que a velocidade não fique com um valor negativo na hora de frear, o valor
        #minimo que velocidade pode ficar é 0.

if __name__ == '__main__': # fazemos este codigo para executar os metodos
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    motor.acelerar()
    motor.acelerar()
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    direcao = Direcao()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)

    carro = Carro(direcao, motor)
    print(carro.calcular_velocidade())

    carro.acelerar()
    print(carro.calcular_velocidade())

    carro.acelerar()
    print(carro.calcular_velocidade())

    carro.frear()
    print(carro.calcular_velocidade())

    print(carro.calcular_direcao())

    carro.girar_a_direita()
    print(carro.calcular_direcao())

    carro.girar_a_esquerda()
    print(carro.calcular_direcao())

    carro.girar_a_esquerda()
    print(carro.calcular_direcao())
















