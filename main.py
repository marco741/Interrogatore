from student import Student

def get_filename():
    """
    DOCSTRING: Controlla se il file di classe è presente nella cartella. Se non è presente lo inizializza.
    OUTPUT: filename
    """
    class_name=input("In che classe ti trovi?")
    section_name=input("In che sezione ti trovi?").upper()

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
    n_students = int(input("Quanti studenti ci sono nella tua classe?"))
    
    print("Inserisci ora l'elenco degli alunni nel formato 'Cognome Nome'")
    students=[input() for _ in range(n_students)]
    students.sort()

    temp = int(input("Inserisci la velocità di interrogazioni in una scala da 1 a 10 (consigliato 7)"))
    speed = 1 - (temp-1)/10     #ad 1 associo 1, a 10 associo 0.1

    with open(filename, "w") as f:
        f.write(str(speed)+'\n')
        for student in students:
            f.write('0;'+student.strip().title()+'\n')

def weights_estimate(students, speed):
    """
    INPUT: Lista di studenti, speed
    DOCSTRING: Calcola i pesi di ogni studente e li assegna al parametro .weight
    OUTPUT: total_weight (relativo solo ai presenti)
    """
    total_weight = 0
    for student in students:
        student.weight = student.weight_estimate(speed)
        total_weight += student.weight * student.present
    return total_weight 
        
def students_list(filename):
    """
    INPUT: filename
    DOCSTRING: Acquisisce da file numero di studenti, velocità e nome (e cognome) di ogni studente
    OUTPUT: (students_list, speed) #tuple
    """
    students=[]
    speed = float()
    with open(filename, "r") as f:
        speed = float(f.readline())
        for line in f:
            splitted_line = line.split(';')
            students.append(Student(splitted_line[1].strip(), int(splitted_line[0])))
    
    return students, speed



filename = get_filename()
students, speed = students_list(filename)
total_weight = weights_estimate(students, speed)

for student in students:
    print("{0}{1:-10}%".format(student, student.percentage(total_weight)))
