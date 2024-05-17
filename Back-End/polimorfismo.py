class Animal:
    def emitir_som(self):
        return 'Qualquer som'
    
class Cachorro(Animal):
    def emitir_som(self):
        return 'auauauauauauau'
    
cachorro = Cachorro()
print(cachorro.emitir_som())

class Gato(Animal):
    def emitir_som(self):
        return 'miau'
    
gato = Gato()
print(gato.emitir_som())
        
