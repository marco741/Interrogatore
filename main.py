from student import Student
from random import randint

def get_filename():
    """
    DOCSTRING: Controlla se il file di classe è presente nella cartella. Se non è presente lo inizializza.
    OUTPUT: filename
    """
    class_name=input("In che classe ti trovi?\n> ")
    section_name=input("In che sezione ti trovi?\n> ").upper()

    filename=class_name+section_name+".csv"
    try:
        f=open(filename, "r")
        f.close()
    except:
        print("La classe non è ancora stata inizializzata")
        initialize(filename)
    return filename

def initialize(filename):
    """
    INPUT: filename
    DOCSTRING: Richiede numero di studenti, velocità e Nome (e cognome) di ogni studente
    """
    n_students = int(input("Quanti studenti ci sono nella tua classe?\n> "))
    
    print("Inserisci ora l'elenco degli alunni nel formato 'Cognome Nome'")
    students=[input(f"{i+1}> ") for i in range(n_students)]
    students.sort()

    temp = int(input("Inserisci la velocità di interrogazioni in una scala da 1 a 10 (consigliato 7):\n> "))
    speed = 1 - (temp-1)/10     #ad 1 associo 1, a 10 associo 0.1

    with open(filename, "w") as f:
        f.write(str(speed)+'\n')
        for student in students:
            f.write('0;'+student.strip().title()+'\n')

def total_weight(students):
    """
    INPUT: Lista di studenti
    DOCSTRING: Calcola i pesi di ogni studente e li assegna al parametro .weight
    OUTPUT: total_weight (relativo solo ai presenti)
    """
    total_weight = 0
    for student in students:
        student.weight_estimate(speed)
        total_weight += student.weight * student.present
    return total_weight 
        
def students_list(filename):
    """
    INPUT: filename
    DOCSTRING: Acquisisce da file numero di studenti, velocità e nome (e cognome) di ogni studente
                Modifica speed
    OUTPUT: students
    """
    students=[]
    global speed
    with open(filename, "r") as f:
        speed = float(f.readline())
        for line in f:
            splitted_line = line.split(';')
            students.append(Student(splitted_line[1].strip(), int(splitted_line[0])))
    
    return students

def students_print(students):
    """
    INPUT: students
    DOCSTRING: Stampa una matrice con tutti gli studenti
    """
    tw=total_weight(students)
    for i,student in enumerate(students):
        print("# {0:<2}{1}{2:2.2f} %  {3}".format(i+1, student, student.percentage(tw), speed))

def call(students):
    """
    INPUT: students
    DOCSTRING: Estrae a sorte uno studente ed incrementa di 1 il suo numero di interrogazioni ricevute
    """
    random_number = randint(1, total_weight(students) )
    for student in students:
        if students.present and random_number > student.weight:
            random_number -= student.weight
        else:
            print(f"{student.name} è stato interrogato")
            student.extracted()

filename = get_filename()
students = students_list(filename)
students_print(students)

