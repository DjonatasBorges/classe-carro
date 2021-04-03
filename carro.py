class Carro:
    rodas, pneus = 4, 4
    lanternas, retrovisores = 2, 2

    def __init__(self, marca, modelo, ano, qtd_de_portas, cor, desligado=True, ligado=False, velocidade=0, direcao='N'):
        self.direcao = direcao
        self.velocidade = velocidade
        self.desligado = desligado
        self.ligado = ligado
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.qtd_de_portas = qtd_de_portas
        self.cor = cor

    def ligar(self):
        if self.desligado:
            print(f'O {self.marca} {self.modelo} acabou de ligar')
            self.ligado = True
            self.desligado = False
        else:
            print(f'O {self.marca} {self.modelo} já está ligado')

    def desligar(self):
        if self.ligado and self.velocidade <= 0:
            print(f'O {self.marca} {self.modelo} acabou de desligar')
            self.desligado = True
            self.ligado = False
        elif self.ligado and self.velocidade >= 1:
            print(f'O {self.marca} {self.modelo} não pode desligar porque esta andando. Pare-o Primeiro.')
        else:
            print(f'O {self.marca} {self.modelo} já está desligado')

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f'O {self.marca} {self.modelo} esta na velocidade de {self.velocidade} km/h')
        else:
            print(f'O {self.marca} {self.modelo} não pode acelerar porque está desligado.')

    def frear(self):
        if self.velocidade >= 6:
            self.velocidade -= 5
            print(f'O {self.marca} {self.modelo} passou para a  velocidade de {self.velocidade} km/h')
        else:
            print(f'O {self.marca} {self.modelo} está parado.')
            self.velocidade = 0

    def virar_direita(self):
        if self.ligado and self.velocidade >= 1:
            if self.direcao in 'Nn':
                print(f'Você estava na direção Norte, agora estará na direção Leste.')
                self.direcao = 'L'
            elif self.direcao in 'Ll':
                print(f'Você estava na direção Leste, agora estará na direção Sul.')
                self.direcao = 'S'
            elif self.direcao in 'Ss':
                print(f'Você estava na direção Sul, agora estará na direção Oeste.')
                self.direcao = 'O'
            else:
                print(f'Você estava na direção Oeste, agora estará na direção Norte.')
                self.direcao = 'N'
        else:
            print(f'O carro não pode virar porque está parado.')

    def virar_esquerda(self):
        if self.ligado and self.velocidade >= 1:
            if self.direcao in 'Nn':
                print(f'Você estava na direção Norte, agora estará na direção Oeste.')
                self.direcao = 'O'
            elif self.direcao in 'Oo':
                print(f'Você estava na direção Oeste, agora estará na direção Sul.')
                self.direcao = 'S'
            elif self.direcao in 'Ss':
                print(f'Você estava na direção Sul, agora estará na direção Leste.')
                self.direcao = 'L'
            else:
                print(f'Você estava na direção Leste, agora estará na direção Norte.')
                self.direcao = 'N'
        else:
            print(f'O carro não pode virar porque está parado.')

    def parar(self):
        if self.velocidade <= 0:
            print(f'O {self.marca} {self.modelo} já está parado.')
        else:
            print(f'O {self.marca} {self.modelo} acabou de parar.')
            self.velocidade = 0


c1 = Carro('Fiat', 'Palio', 2010, 4, 'Prata')
c1.ligar()
c1.acelerar(9)
c1.acelerar(5)
c1.frear()
c1.frear()
c1.frear()
c1.acelerar(20)
c1.virar_direita()
c1.virar_direita()
c1.virar_direita()
c1.virar_direita()
c1.virar_esquerda()
c1.virar_esquerda()
c1.virar_esquerda()
c1.virar_esquerda()
c1.desligar()
c1.parar()
c1.desligar()
c1.acelerar(5)
