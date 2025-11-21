import pytest
from Sudoku import *
import random


def  test_modifier_case_valide():
    grille = [["_","_","_"],["_","_","_"],["_","_","_"]]
    grille_originale = [["_","_","_"],["_","_","_"],["_","_","_"]]

    modifier_case(grille, grille_originale, 1,1,5)


    assert grille[1][1] == 5


def  test_modifier_case_valide2():
    grille = [["_","_","_"],["_","3","_"],["_","_","_"]]
    grille_originale = [["_","_","_"],["_","_","_"],["_","_","_"]]

    modifier_case(grille, grille_originale, 1,1,5)


    assert grille[1][1] == 5


def test_modifier_case_interdite():
    grille = [["_", "_", "_"], ["_", "3", "_"], ["_", "_", "_"]]
    grille_originale = [["_", "_", "_"], ["_", "3", "_"], ["_", "_", "_"]]

    modifier_case(grille, grille_originale, 1,1,7)

    assert grille[1][1] == "3"

def test_modifier_case_invalide():
    grille = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    grille_originale = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    modifier_case(grille, grille_originale, 0,0,15)

    assert grille[0][0] == "_"



def test_placement_chiffre_invalide():
    grille = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    grille_originale = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    placement_chiffres(grille, 0, 0, 15, grille_originale)

    assert grille[0][0] == "_"

def test_placement_chiffre_invalide2():
    grille = [["_", "_", "_"], ["_", "3", "_"], ["_", "_", "_"]]
    grille_solution = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    placement_chiffres(grille, 0, 0, 5, grille_solution)

    assert grille[0][0] == "_"


#GABRIEL

def test_aucune_erreur():

   grille = [
       ["1","2","3"],
       ["4","5","6"],
       ["7","8","9"]
   ]

   grille_solution = [
       ["1","2","3"],
       ["4","5","6"],
       ["7","8","9"]
   ]
   result = verifier_erreurs(grille, grille_solution)

   assert result == False


# GABRIEL

def test_aucun_doublon():
    grille = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    result = verifier_doublons(grille)

    assert result == False


def test_un_doublon_present():
    grille = [
        ["1", "2", "3"],
        ["1", "5", "6"],
        ["7", "8", "9"]
    ]

    result = verifier_doublons(grille)

    assert result == True


def test_indice_random():
    #arranger
    grille = [
        ["_"] * 9,
        ["_"] * 9,
        ["_"] * 9,
        ["_"] * 9,
        ["_"] * 9,
        ["_"] * 9,
        ["_"] * 9,
        ["_"] * 9,
        ["_"] * 9,
        ]

    grille_solution = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
    ]
    nb_indices = 0

    # demander indice:
    nb_indices = indice_random(grille, grille_solution, nb_indices)
    # assert compteur indice +1
    assert nb_indices == 1
    # vérification valeur
    cases_correctes = 0
    for i in range(9):
        for j in range(9):
            if grille[i][j] != "_":
                assert grille[i][j] == grille_solution[i][j]
                cases_correctes += 1

    assert cases_correctes == 1
