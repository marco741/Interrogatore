
class Studente:
    def __init__(self, cognome, nome, n_interrogazioni, assente=False):
        self.nome = nome
        self.cognome = cognome
        self.n_interrogazioni = n_interrogazioni
        self.assente = assente
    
    def calcola_peso(self, k, v):

        return k * v**self.n_interrogazioni
    
    def __str__(self):
        return "{0:30} {1}".format(self.cognome+' '+self.nome, self.n_interrogazioni)
        #printf("#%3d\t%-30s%d\t\t%s\t%5.4f%%\n", i + 1, vet[i], calls[i], spazi, chance[i]);
