class Student:
    def __init__(self, surname, name, interrogations, present=True):
        self.name = name
        self.surname = surname
        self.interrogations = interrogations
        self.present = present
    
    def weight_estimate(self, k, v):

        return k * v**self.interrogations
    
    def __str__(self):
        return "{0:30} {1}".format(self.surname+' '+self.name, self.interrogations)
        #printf("#%3d\t%-30s%d\t\t%s\t%5.4f%%\n", i + 1, vet[i], calls[i], spazi, chance[i]);
        