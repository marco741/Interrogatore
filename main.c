#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <windows.h>
#define DIM 40
#define LUNG 15
#define PESO 1000
#define GRAF 10

void initialize(char vet[DIM][DIM], int*, float*);
void stampaAlunni(char vet[DIM][DIM], int, float, char [LUNG], int calls[DIM]);
void capitalize(char a[]);
char classe(char nomefile[LUNG]);

int leggiFile(char vet[DIM][DIM], int calls[DIM], char nomefile[LUNG], int*, float*);
int calcolaPesi(float chance[DIM], int pesi[DIM], int calls[DIM], int, float, int assenti[DIM], int nassenti);
void stampaVideo(float chance [DIM], char vet[DIM][DIM], int calls[DIM], char nomefile[LUNG], int, float, int assenti[DIM], int nassenti);
int estrai(char vet[DIM][DIM], int pesi[DIM], int totPesi, int calls[DIM], int assenti[DIM], int *nassenti, int nalunni);
int inserisciAssenti(int assenti[DIM], int nalunni);
int checkAssenza(int i, int assenti[DIM], int nassenti);
float modificaSpeed();
int opzioni();
void inizializzaVettore(int calls[DIM]);

int main() {
    char vet[DIM][DIM], nomefile[LUNG], yesnot, test;
    int nalunni, totPesi, pesi[DIM], assenti[DIM] = {-1}, nassenti = 0;
    short uscita, domande = 1;
    float speed, chance[DIM];
    int calls[DIM] = {0};


    yesnot = classe(nomefile);
    if (yesnot != 'n') {
        initialize(vet, &nalunni, &speed);
        stampaAlunni(vet, nalunni, speed, nomefile, calls);
        puts("L'inserimento e' terminato con successo!");
        Sleep(2000);
        domande = 0;
    }

    if (uscita = leggiFile(vet, calls, nomefile, &nalunni, &speed))
        return (EXIT_FAILURE);

    totPesi = calcolaPesi(chance, pesi, calls, nalunni, speed, assenti, nassenti);
    stampaVideo(chance, vet, calls, nomefile, nalunni, speed, assenti, nassenti);

    if (yesnot == 'n') {
        do {

            domande = opzioni();
            stampaVideo(chance, vet, calls, nomefile, nalunni, speed, assenti, nassenti);

            switch (domande) {
                case 3:
                    inizializzaVettore(calls);
                    calcolaPesi(chance, pesi, calls, nalunni, speed, assenti, nassenti);
                    stampaVideo(chance, vet, calls, nomefile, nalunni, speed, assenti, nassenti);
                    break;

                case 2:
                    speed = modificaSpeed();
                    calcolaPesi(chance, pesi, calls, nalunni, speed, assenti, nassenti);
                    stampaVideo(chance, vet, calls, nomefile, nalunni, speed, assenti, nassenti);
            }
        } while (domande == 3 || domande == 2);
    }
    nassenti = inserisciAssenti(assenti, nalunni);
    do {
        totPesi = calcolaPesi(chance, pesi, calls, nalunni, speed, assenti, nassenti);
        stampaVideo(chance, vet, calls, nomefile, nalunni, speed, assenti, nassenti);
        if (estrai(vet, pesi, totPesi, calls, assenti, &nassenti, nalunni)) {

            puts("Hai gia' interrogato tutta la classe.\nPremere invio per terminare l'esecuzione.");
            while (getchar() != '\n');
            return (EXIT_FAILURE);
        }

        stampaAlunni(vet, nalunni, speed, nomefile, calls);

        do {
            puts("Vuoi proseguire con le interrogazioni? (s/n)");
            if ((test = getchar()) != 'y' && test != 'n' && test != 's')
                puts("Attenzione, le risposte accettabili sono solo \'s\' o \'n\'.\n");
            while (getchar() != '\n');
        } while (test != 'y' && test != 'n' && test != 's');
    } while (test != 'n');
    puts("Terminazione.");
    puts("Premere invio per concludere l'esecuzione.");
    while (getchar() != '\n');
    return EXIT_SUCCESS;
}

void initialize(char vet[][DIM], int *nalunni, float *speed) {
    int i, j, cont;
    char help[DIM], controllo;

    do {
        *nalunni = -1;
        puts("\nQuanti alunni ci sono nella tua classe?");
        scanf("%d", nalunni);
        if (*nalunni < 2 || *nalunni > DIM)
            puts("Attenzione, una classe puo' contenere solo un numero finito di alunni compreso tra 2 e 30.\n");
        while (getchar() != '\n');
    } while (*nalunni < 2 || *nalunni > DIM);

    do {

        puts("Inserisci ora l'elenco di alunni nel formato \"Cognome Nome\" (Senza virgolette):");
        for (i = 0; i < *nalunni; i++) {
            scanf("%29[^\n]", vet[i]);
            j = 0;
            cont = 0;
            while (j < DIM && cont == 0 && vet[i][j] != '\0')
                if ((vet[i][j] >= 48) && (vet[i][j] <= 57)) {
                    i--;
                    cont = 1;
                    puts("Un nome non puo' contenere numeri. Reinserire partendo dall'ultimo alunno.\n");
                } else
                    j++;
            if (j <= 1)
                i--;
            while (getchar() != '\n');
        }

        do {
            puts("Confermi il tuo inserimento? (s/n)");
            scanf("%c", &controllo);
            if (controllo != 'y' && controllo != 's' && controllo != 'n')
                puts("Attenzione, le risposte accettabili sono solo \'s\' o \'n\'.\n");
            while (getchar() != '\n');
        } while (controllo != 'y' && controllo != 's' && controllo != 'n');
    } while (controllo == 'n');


    do {
        *speed = -1;
        puts("Inserisci la velocita' di interrogazioni in una scala da 1 a 10 (consigliato 7):");
        scanf("%f", speed);
        if (*speed < 1 || *speed > 10)
            puts("Attenzione, la velocita' puo' solo essere rappresentata da un numero finito compreso tra 1 e 10.\n");
        while (getchar() != '\n');
    } while (*speed < 1 || *speed > 10);
    *speed = 1 - ((*speed - 1) / 10);


    for (i = 0; i<*nalunni - 1; i++)
        for (j = i + 1; j<*nalunni; j++)
            if (strcmp(vet[i], vet[j]) > 0) {
                strcpy(help, vet[i]);
                strcpy(vet[i], vet[j]);
                strcpy(vet[j], help);
            }
}

void stampaAlunni(char vet[][DIM], int nalunni, float speed, char nomefile[], int calls[]) {

    FILE *pf;
    int i;
    pf = fopen(nomefile, "w");
    fprintf(pf, "%.1f\t%d\n", speed, nalunni);
    for (i = 0; i < nalunni; i++) {
        fprintf(pf, "%d\t%s\n", calls[i], vet[i]);
    }

    fclose(pf);
}

void capitalize(char nomefile[]) {
    int i = 0;
    while ((nomefile[i]) != '\0') {
        nomefile[i] = (toupper(nomefile[i]));
        i++;
    }
}

char classe(char nomefile[LUNG]) {
    FILE *test;
    char yesnot = 'n', c;
    int classe, i;
    char sezione[10];

    do {

        do {
            puts("In che classe ti trovi? (Formato es: 3D)");
            do {
                scanf("%d", &classe);
                if (classe < 1 || classe > 5) {
                    puts("Attenzione, la classe puo' solo essere compresa tra 1 e 5.\n");
                    while (getchar() != '\n');
                }
            } while (classe < 1 || classe > 5);
            nomefile[0] = (classe + 48);
            nomefile[1] = '\0';

            scanf("%9s", sezione);
            if ((c = getchar()) != '\n') {
                while (getchar() != '\n');
                puts("Attenzione, la classe puo' essere costituita al massimo da 10 caratteri.\nReinserisci la classe dall'inizio.\n");
            }

            capitalize(sezione);
            for (i = 0; sezione[i] != '\0' && c == '\n'; i++)
                if (sezione[i] < 'A' || sezione[i] > 'Z') {
                    puts("Attenzione, la sezione non puo' contenere valori numerici.\nReinserisci la classe dall'inizio.\n");
                    c = 'a';
                }
        } while (sezione[i] != '\0' || c != '\n');

        strcat(nomefile, sezione);
        strcat(nomefile, ".txt");
        test = fopen(nomefile, "r");
        if (test == NULL) {
            puts("La classe non e' ancora stata inizializzata.");
            do {
                puts("Vuoi avviare il processo di inizializzazione? (s/n)");
                yesnot = getchar();
                if (yesnot != 'y' && yesnot != 's' && yesnot != 'n')
                    puts("Attenzione, le risposte accettabili sono solo \'s\' o \'n\'.\n");
                while (getchar() != '\n');
            } while (yesnot != 'y' && yesnot != 's' && yesnot != 'n');
        } else
            return yesnot;
    } while (yesnot == 'n');
    return yesnot;
}

int leggiFile(char vet[][DIM], int calls[], char nomefile[], int *nalunni, float *speed) {
    FILE *pf;
    int i, j;

    pf = fopen(nomefile, "r");
    if (pf == NULL) {
        puts("Errore nell'apertura del file");
        return 1;
    }
    fscanf(pf, "%f\t%d\n", speed, nalunni);

    for (i = 0; i < *nalunni; i++) {
        j = 0;
        fscanf(pf, "%d\t", &calls[i]);
        while ((vet[i][j] = fgetc(pf)) != '\n')
            j++;
        vet[i][j] = '\0';
    }
    fclose(pf);
    return 0;
}

void stampaVideo(float chance[DIM], char vet[][DIM], int calls[DIM], char nomefile[LUNG], int nalunni, float speed, int assenti[DIM], int nassenti) {
    int i, lunghezza;
    char asterischi[GRAF];
    char trattini[DIM] = {'-'};
    char spazi[DIM] = {' '};

    for (i = 0; i < GRAF; i++)
        asterischi[i] = '*';
    lunghezza = 15 - strlen(nomefile);
    asterischi[lunghezza / 2] = '\0';
    spazi[lunghezza] = '\0';

    system("clear");
    puts("--------------------------------------------------------------------");
    if (lunghezza % 2 == 1)
        printf("***********************%s Classe ", asterischi);
    else
        printf("**********************%s Classe ", asterischi);
    for (i = 0; nomefile[i] != '.'; i++)
        putchar(nomefile[i]);
    asterischi[lunghezza] = '\0';
    printf(" **************************%s", asterischi);

    puts("");
    speed = 11 - (speed * 10);
    if (speed == 10)
        puts("************************ Velocita' 10/10 ***************************");
    else
        printf("************************ Velocita' %.0f/10 ****************************\n", speed);
    puts("--------------------------------------------------------------------");
    printf("   No\tCognome Nome                 %sInterrogazioni\tProbabilita'\n", spazi);
    for (i = 0; i < nalunni; i++)
        if (nassenti != 0) {
            if (checkAssenza(i, assenti, nassenti))
                printf("#%3d\t%-30s%d\t\t%s\t%5.4f%%\n", i + 1, vet[i], calls[i], spazi, chance[i]);
        } else
            printf("#%3d\t%-30s%d\t\t%s\t%5.4f%%\n", i + 1, vet[i], calls[i], spazi, chance[i]);

    puts("\n"); //ho messo 2 righe di spazio. Non e' un errore.
}

int calcolaPesi(float chance[DIM], int pesi[DIM], int calls[DIM], int nalunni, float speed, int assenti[], int nassenti) {
    int i, totPesi = 0, x;
    for (i = 0; i < nalunni; i++)
        if (nassenti) {
            if (checkAssenza(i, assenti, nassenti)) {
                x = PESO * (pow(speed, calls[i]));
                pesi[i] = x;
                totPesi += pesi[i];
            }
        } else {
            x = PESO * (pow(speed, calls[i]));
            pesi[i] = x;
            totPesi += pesi[i];
        }

    for (i = 0; i < nalunni; i++)
        if (nassenti != 0) {
            if (checkAssenza(i, assenti, nassenti))
                chance[i] = ((float) pesi[i] / totPesi)*100;
        } else
            chance[i] = ((float) pesi[i] / totPesi)*100;
    return totPesi;
}

int estrai(char vet[][DIM], int pesi[], int totPesi, int calls[], int assenti[], int *nassenti, int nalunni) {
    srand(time(NULL));
    int random, i, controllo = 0, help, k, j;
    i = 0;
    if (*nassenti != nalunni) {


        puts("Premi invio per estrarre l'interrogato.\n");
        while (getchar() != '\n');
        random = (rand() % totPesi) + 1;
        while (controllo == 0) {
            if (checkAssenza(i, assenti, *nassenti)) {
                if (random > pesi[i]) {
                    random -= pesi[i];
                    i++;
                } else controllo = 1;
            } else i++;
        }
        printf("L'interrogato e' %s\n", vet[i]);
        calls[i]++;
        assenti[*nassenti] = i;
        *nassenti = *nassenti + 1;


        for (i = 0; i < *nassenti - 1; i++)
            for (j = i + 1; j < *nassenti; j++)
                if (assenti[i] < assenti[j]) {
                    help = assenti[i];
                    assenti[i] = assenti[j];
                    assenti[j] = help;

                }
        return 0;
    } else
        return 1;


}

int inserisciAssenti(int assenti[], int nalunni) {
    int i, j, help, nassenti, cont_inserimento = 1;
    char controllo, a;

    do {
        do {
            nassenti = -1;
            puts("Quanti sono gli assenti?");
            scanf("%d", &nassenti);
            if (nassenti < 0 || nassenti >= nalunni)
                printf("Attenzione, all'appello di questa classe puo' mancare solo un numero finito di alunni compreso tra 0 e %d.\n\n", nalunni - 1);
            while (getchar() != '\n');
        } while (nassenti < 0 || nassenti >= nalunni);
        do {
            puts("Confermi la tua scelta? (s/n)");
            scanf("%c", &controllo);
            if (controllo != 's' && controllo != 'n' && controllo != 'y')
                puts("Attenzione, le risposte accettabili sono solo \'s\' o \'n\'.\n");
            while (getchar() != '\n');
        } while (controllo != 's' && controllo != 'n' && controllo != 'y');
    } while (controllo == 'n');
    if (nassenti) {
        do {
            puts("Inserisci ora il numero identificativo dei ragazzi assenti uno alla volta (#  No):");
            for (i = 0; i < nassenti; i++) {
                do {
                    cont_inserimento = 0;
                    scanf("%d", &assenti[i]);
                    if (assenti[i] < 1 || assenti[i] > nalunni)
                        printf("Attenzione, il numero identificativo dei ragazzi assenti puo' solo essere un numero intero compreso tra 1 e %d. Riprova.\n\n", nalunni);
                    if (i)
                        if (!checkAssenza(assenti[i] - 1, assenti, i)) {
                            cont_inserimento = 1;
                            puts("Non puoi inserire ancora lo stesso identificativo, riprendi dall'ultimo identificativo errato.\n");
                        }

                    while (a = getchar() != '\n' && (a < 48 || a > 57));
                } while ((assenti[i] < 1 || assenti[i] > nalunni) || cont_inserimento);
                assenti[i]--;

            }
            do {
                puts("Confermi la tua scelta? (s/n)");
                scanf("%c", &controllo);
                if (controllo != 's' && controllo != 'n' && controllo != 'y')
                    puts("Attenzione, le risposte accettabili sono solo \'s\' o \'n\'.\n");
                while (getchar() != '\n');
            } while (controllo != 's' && controllo != 'n' && controllo != 'y');

        } while (controllo == 'n');

        for (i = 0; i < nassenti - 1; i++)
            for (j = i + 1; j < nassenti; j++)
                if (assenti[i] < assenti[j]) {
                    help = assenti[i];
                    assenti[i] = assenti[j];
                    assenti[j] = help;

                }
    }

    return nassenti;

}

int checkAssenza(int i, int assenti[DIM], int nassenti) {
    int j, cont = 1;
    for (j = 0; j < nassenti && cont == 1; j++)
        if (i == assenti[j])
            cont = 0;





    return cont;
}

float modificaSpeed() {
    float speed;
    char controllo;

    do {
        speed = -1;
        puts("Inserisci la velocita' di interrogazioni in una scala da 1 a 10 (consigliato 7):");
        scanf("%f", &speed);
        if (speed < 1 || speed > 10)
            puts("Attenzione, la velocita' puo' solo essere rappresentata da un numero finito compreso tra 1 e 10.\n");
        while (getchar() != '\n');
    } while (speed < 1 || speed > 10);
    return 1 - ((speed - 1) / 10);

}

int opzioni() {
    int richiesta;
    char controllo = 's';

    do {

        do {

            puts("Inserisci 1 se vuoi dare inizio ad una giornata di interrogazioni.");
            puts("Inserisci 2 se vuoi modificare la velocita' per concludere il ciclo di interrogazioni piu' velocemente/lentamente.");
            puts("Inserisci 3 se vuoi reinizializzare il numero di interrogazioni di ogni studente");
            scanf("%d", &richiesta);
            if (richiesta != 1 && richiesta != 2 && richiesta != 3)
                puts("Attenzione, le alternative possibili sono solo \'1\', \'2\' e \'3\'.\n");
            while (getchar() != '\n');
        } while (richiesta != 1 && richiesta != 2 && richiesta != 3);


        if (richiesta == 3)
            do {
                puts("Sicuro della tua scelta? Il processo e' irreversibile. (s/n)");
                scanf("%c", &controllo);
                if (controllo != 'y' && controllo != 'n' && controllo != 's')
                    puts("Attenzione, le risposte accettabili sono solo \'s\' o \'n\'.\n");
                while (getchar() != '\n');
            } while (controllo != 'y' && controllo != 'n' && controllo != 's');
    } while (controllo == 'n');

    puts("");
    switch (richiesta) {
        case 1:
            return 1;

        case 2:
            return 2;

        case 3:
            return 3;

    }

}

void inizializzaVettore(int calls[]) {
    int i;
    for (i = 0; i < DIM; i++)
        calls[i] = 0;
}
