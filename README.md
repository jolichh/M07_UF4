# Pràctica 1: VIEWS I TEMPLATES

## Feina individual
1. Crear un projecte de DJANGO de nom TIC_BCN_inicials alumnat. 
    El nom de l’aplicació a on s’hi afegiran els templates i les views és centre.

    Es farà una aplicació per mostrar dades de l’alumnat de DAW2A i del seu professorat (dades reals).

    Dades a mostrar alumnat: nom, cognom1, cognom2, correu, curs, mòduls matriculats.
    Dades a mostrar prof.: nom, cognom1, cognom2, correu, curs, tutor(si s’escau),mòduls que imparteix.

    Path alumne: localhost:8000/centre/students
    Path professor: localhost:8000/centre/teachers

    Només la pàgina principal (del projecte) ha de renderitzar també un header. Aquest header sempre es mostrarà (independentment de si està mostrant dades de professorat o d’alumnat).

## Captures pantalla
[Video](https://drive.google.com/file/d/1jIkzvrFWLZFM-BKOpgkM8RROPbVAOziy/view?usp=drive_link)

Llistat alumnes
![centres/students](TIC_BCN_JJLC/img/alumnes.png)
Info alumne
![centres/students](TIC_BCN_JJLC/img/alumn.png)
Llistat professors
![centres/students](TIC_BCN_JJLC/img/profess.png)
Info professor
![centres/students](TIC_BCN_JJLC/img/profe.png)

# Pràctica 2: models
Afegir la part del model a la pràctica 1 connectant amb un PostgreSQL. Es crea la BBDD desde Django, amb Models (NO a pgAdmin4).

A la base de dades ha d’haver 1 taula amb 6 (mínim id i rol) camps (sense comptar el id ja que es crea automàticament).

## Captura pantalla
comandes: python manage.py makemgrations | python manage.py migrate
![Migracio](TIC_BCN_JJLC/img/migrate.png)
![Models](TIC_BCN_JJLC/img/models.png)