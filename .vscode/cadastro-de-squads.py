from mimetypes import init


class Pessoa: 
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone
    
    def exibir(self):
        print(f'->{self.nome} - {self.fone}')

class Squad: 
    def __init__(self, nome, techlead=None, devs=None):
        self.nome = nome
        self.devs = []
        self.techlead = techlead

    def incluir_techlead(self, techlead):
        self.techlead = techlead

    def incluir_dev(self, dev):
        self.devs.append(dev)

class Colaborador(Pessoa):
    def __init__(self, nome, fone, squad=None):
        super().__init__(nome, fone)
        self.squad = squad

class Dev(Colaborador):
    def __init__(self, nome, fone, cargo, squad=None):
        super().__init__(nome, fone, squad)
        self.cargo = cargo

        def incluir_squad(self, squad):
            self.squad = squad 

        def exibir(self):
            super().exibir()
            print(f'    Cargo de {self.cargo} na squad {self.squad.nome}\n')

while True:
    squads = []
    nome_squad = input('\nNome da squad: ')
    nome_techlead = input('Nome do Techlead da squad: ')
    fone_techlead = input('Telefone do techlead: ')

    squad = Squad(nome_squad)
    techlead = Colaborador(nome_techlead, fone_techlead)
    squad.incluir_techlead(techlead)
    techlead.incluir_squad(squad)

    squads.append(squad)

    nome_dev = input('\nNome do desenvolvedor: ')
    fone_dev = input('Tlefone do desenvolvedor: ')
    cargo_dev = input('Cargo do desenvolvedor: ')
    dev = Dev(nome_dev, fone_dev, cargo_dev)
    dev.incluir_squad(squad)
    squad.incluir_dev(dev)

    option = input('Deseja adicionar mais um dev[S/N]: ')
    if option in 'Nn':
        break 

    option = input('\nDeseja adicionar mais uma squad [S/N]: ')
    if option in 'Nn':
        break 

squads.append(squad)

for squad in squads:
    print(f'\n-------------------------------{squad.nome}-------------------------------')
    print(f'Techlead: {squad.techlead.nome}')
    print('\n----Devs do squad----')
    for dev in squad.devs:
        dev.exibir()
    print(f'\n-------------------------------{squad.nome}-------------------------------')

