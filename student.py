from config import *

class Student:
    def __init__(self, name, interrogations, weight = 0, present=True):
        self.name = name
        self.interrogations = interrogations
        self.present = present
        self.weight = weight
    
    def weight_estimate(self):
        """
        DOCSTRING: Calcola i pesi del singolo studente sfruttando 
        """
        self.weight = WEIGHT_CONST * speed**self.interrogations
    
    def percentage(self, total_weight):
        """
        INPUT: total_weight
        DOCSTRING: Calcola la probabilità di uno studente di essere estratto
        OUTPUT: percentage
        """
        return self.weight/total_weight * 100
    
    def __str__(self):
        return "{0:30} {1}".format(self.name, self.interrogations)
        #printf("#%3d\t%-30s%d\t\t%s\t%5.4f%%\n", i + 1, vet[i], calls[i], spazi, chance[i]);
        