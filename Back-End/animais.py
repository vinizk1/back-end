class Animal():
    qtd_patas = 4
    rabo = Falsepelo = True
    especie = ''

    class Cachorro(Animal):
        rabo = True
        especie = 'Canil Lupulo Familiriaes'
        raca = 'Pinscher'
        nome = 'Sérgio'
        porte = 'Pequeno'

        def latir():
            return 'AUAUAUAUAUUAUAUAUAUAUAUUAUA'
        
        def comer():
            return 'NAHMINHAMINHAMI'
        
        def dormir():
            return 'ZZZZZZZZZZZZZZZZZZZ'
        
