#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Le factoriel n'est pas défini pour les nombres négatifs")

    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <nombre>")
else:
    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except ValueError as e:
        print("Erreur :", e)
