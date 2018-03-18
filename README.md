# Practica 2 VDPR

## Integrantes del equipo

Javier Guillamón Pardo  
Borja Sanchidrián Monge  
Álvaro López-Jurado Reynolds  
Marino Pérez Segura  
Miguel Ingelmo Barrada  

## Enunciado

Necesito una librería/script que, dado un texto de longitud variable (y en cualquier codificación) me devuelva como salida una lista de palabras y el número de veces que aparecen en el texto, ordenadas por este número.

No quiero que aparezcan símbolos de puntuación ni stopwords

Las palabras en Mayúsculas y minúsculas son iguales

        (Hola == hola == hOLA)

Tiene que tener un coverage mayor de 65%

## Como funciona

Puedes instalar las dependencias usando:

```bash
make bootstrap
```

Y  ejecutar los test con:

```bash
make test
```

Puedes ejecutar el programa utilizando el comando:

```bash
python main.py <text>

python main.py En un lugar de la mancha de cuyo nombre no quiero...

```

## Otros comandos
```bash
source venv/bin/activate
```

```bash
venv/bin/coverage run main.py
```

```bash
venv/bin/coverage report
```

```bash
venv/bin/coverage html
```
