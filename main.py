from student import Student
from random import randint
from os import system

def get_filename():
    """
    DOCSTRING: Controlla se il file di classe è presente nella cartella. Se non è presente lo inizializza.
    OUTPUT: filename
    """
    class_name=input("In che classe ti trovi?\n> ").upper()

    filename=class_name+".csv"
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

    with open(filename, "w") as f:  #Primo salvataggio su file
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
    return int(total_weight) 
        
def load_file(filename):
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

def save_file(filename):
    """
    INPUT: filename
    DOCSTRING: Salva su file velocità e nome (e cognome) di ogni studente
    """
    with open(filename, "w") as f:
        f.write(str(speed)+'\n')
        for student in students:
            f.write(str(student.interrogations)+';'+student.name+'\n')

def students_print(students):
    """
    INPUT: students
    DOCSTRING: Stampa una matrice con tutti gli studenti
    OUTPUT: Numero di studenti stampati
    """
    system("cls")
    print("{:-^70}".format(""))
    print("{:*^70}".format(" Classe "+filename[:-4]+" "))
    print("{:-^70}".format(""))
    print("   {:6}{:30}{:20}{:11}".format("No", "Cognome Nome", "Interrogazioni", "Probabilità"))
    tw=total_weight(students)
    n_printed=0
    for i, student in enumerate(students):
        if student.present:
            n_printed += 1
            print("#{0:>3}{1:5}{2}{3:<20}{4:>5.2f} %".format(i + 1, "", student, student.interrogations, student.percentage(tw)))
    return n_printed

def absent(students):
    """
    INPUT: students
    DOCSTRING: resetta il parametro "present" di tutti gli studenti a True e poi
                setta il parametro "present" degli studenti non presenti a False
    """
    for student in students:
        student.present=True
    student_id = 1
    while students_print(students) > 1 and student_id != 0:
        print("Inserisci il numero identificativo degli studenti assenti, 0 per terminare l'inserimento:")
        student_id =  int(input(">"))
        if student_id != 0:
            students[student_id-1].present = False
    print("Inserimento assenti completato con successo")

def call(students):
    """
    INPUT: students
    DOCSTRING: Estrae a sorte uno studente ed incrementa di 1 il suo numero di interrogazioni ricevute
    """
    students_print(students)
    random_number = randint(1, total_weight(students) )
    for student in students:
        if student.present :
            if random_number > student.weight:
                random_number -= student.weight
            else: break
    print(f"{student.name} è stato interrogato")
    student.extracted()
    input("Premi invio per continuare.")

def modify_speed(students):
    """
    INPUT: students
    DOCSTRING: Modifica la velocità di interrogazioni attuale
    """
    global speed
    temp = int(input("Inserisci la nuova velocità di interrogazioni in una scala da 1 a 10:\n> "))
    speed = 1 - (temp-1)/10     #ad 1 associo 1, a 10 associo 0.1
    
def reset_interrogations(students):
    """
    INPUT: students
    DOCSTRING: Reinizializza le interrogazioni di tutti gli studenti
    """
    for student in students:
        student.interrogations = 0
    

filename = get_filename()
students = load_file(filename)
#DA INTERNET
menu = {}
menu['1']="Interroga." 
menu['2']="Inserisci Assenti."
menu['3']="Modifica Velocità Interrogazioni."
menu['4']="Azzera Numero Interrogazioni"
menu['5']="Exit"
system("cls")
options = menu.keys()
selection = 0
while students_print(students) > 1: 
    print("{:-^70}".format(""))
    print("{:*^70}".format(" Menù "))
    print("{:-^70}".format(""))
    for entry in options: 
        print(entry, menu[entry])
    selection = input("Please Select:\n>")     
    system("cls")
    if selection in menu:
        print(menu[selection])
    if selection =='1': 
        call(students)
    elif selection == '2':
        absent(students) 
    elif selection == '3':
        modify_speed(students)
    elif selection == '4': 
        reset_interrogations(students)
    elif selection == '5': 
        break
    else: 
        print("Unknown Option Selected!") 
    save_file(filename)
###############################################

##SEMPRE DA INTERNET
#ans = True
#while ans:
#    print ("""
#    1.Add a Student
#    2.Delete a Student
#    3.Look Up Student Record
#    4.Exit/Quit
#    """)
#    ans=input("What would you like to do?")
#    system("cls")
#    if ans=="1": 
#        print("\n Student Added") 
#    elif ans=="2":
#        print("\n Student Deleted") 
#    elif ans=="3":
#        print("\n Student Record Found") 
#    elif ans=="4":
#        print("\n Goodbye") 
#        break
#    elif ans !="":
#        print("\n Not Valid Choice Try again") 
################################################