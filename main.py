import student

def get_filename():
    """
    DOCSTRING: Controlla se il file di classe è presente nella cartella. Se non è presente lo inizializza.
    OUTPUT: filename
    """
    class_name=input("In che classe ti trovi?")
    section_name=input("In che sezione ti trovi?").upper()

    filename=class_name+section_name+".txt"
    try:
        f=open(filename, "r")
        f.close()
    except:
        print("La classe non è ancora stata inizializzata")
        initialize(filename)
    return filename

def initialize(filename):
    n_students = int(input("Quanti studenti ci sono nella tua classe?"))
    
    print("Inserisci ora l'elenco degli alunni nel formato 'Cognome Nome'")
    students=[input() for _ in range(n_students)]
    students.sort()

    temp = int(input("Inserisci la velocità di interrogazioni in una scala da 1 a 10 (consigliato 7)"))
    speed = 1 - (temp-1)/10     #ad 1 associo 1, a 10 associo 0.1

    with open(filename, "w") as f:
        f.write(str(speed)+' '+str(n_students)+'\n')
        for student in students:
            f.write('0 '+student.strip().title()+'\n')

get_filename()