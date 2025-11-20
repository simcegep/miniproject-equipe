import pytest
from Sudoku import *
import random


def  test_modifier_case_valide():
    grille = [["_","_","_"],["_","_","_"],["_","_","_"]]
    grille_originale = [["_","_","_"],["_","_","_"],["_","_","_"]]

    result = modifier_case(grille, grille_originale, 1,1,5)
    result_attendu = grille[1][1] == "5"

    assert result == result_attendu


def  test_modifier_case_valide2():
    grille = [["_","_","_"],["_","3","_"],["_","_","_"]]
    grille_originale = [["_","_","_"],["_","_","_"],["_","_","_"]]

    result = modifier_case(grille, grille_originale, 1,1,5)
    result_attendu = grille[1][1] == "5"

    assert result == result_attendu


def test_modifier_case_interdite():
    grille = [["_", "_", "_"], ["_", "3", "_"], ["_", "_", "_"]]
    grille_originale = [["_", "_", "_"], ["_", "3", "_"], ["_", "_", "_"]]

    result = modifier_case(grille, grille_originale, 1,1,7)
    result_attendu = grille[1][1] == "3"

    assert result == result_attendu

def test_modifier_case_invalide():
    grille = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    grille_originale = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    result = modifier_case(grille, grille_originale, 0,0,15)
    result_attendu = grille[0][0] == "_"

    assert result == result_attendu

# Les test unitaire des fonction placement_chiffre et modifier_case sont pratuiquement pareil,
# la différance des deux fonction est que l'une est de placer le chiffre dans la grille et l'autre
#permet de changer un chiffre qui n'était pas valide.

def test_placement_chiffre_valide():
    grille = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    grille_originale = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    result = placement_chiffres(grille, grille_originale, 1, 2, 4)
    result_attendu = grille[1][2] == "4"

    assert result == result_attendu


def test_placement_chiffre_invalide():
    grille = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    grille_originale = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    result = placement_chiffres(grille, grille_originale, 0, 0, 15)
    result_attendu = grille[0][0] == "_"

    assert result == result_attendu


def test_placement_chiffre_invalide2():
    grille = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    grille_originale = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    result = placement_chiffres(grille, grille_originale, 0, 0, 15)
    result_attendu = grille[0][0] == "_"

    assert result == result_attendu


#GABRIEL

def test_aucune_erreur():
    # arrange
    valeur = 5
    mini = 1
    maxi = 9

    # act
    result = verifier_erreur(valeur, mini, maxi)

    # assert
    result_attendu = False  # pas d’erreur
    assert result == result_attendu


def test_valeur_trop_petite():
    # arrange
    valeur = 0
    mini = 1
    maxi = 9

    # act
    result = verifier_erreur(valeur, mini, maxi)

    # assert
    result_attendu = True   # erreur détectée
    assert result == result_attendu


def test_valeur_trop_grande():
    # arrange
    valeur = 20
    mini = 1
    maxi = 9

    # act
    result = verifier_erreur(valeur, mini, maxi)

    # assert
    result_attendu = True   # erreur détectée
    assert result == result_attendu


# GABRIEL

def test_aucun_doublon():
    # arrange
    liste = [1, 2, 3, 4]

    # act
    result = verifier_doublons(liste)

    # assert
    result_attendu = False   # pas de doublon
    assert result == result_attendu


def test_un_doublon_present():
    # arrange
    liste = [1, 2, 2, 3]

    # act
    result = verifier_doublons(liste)

    # assert
    result_attendu = True    # doublon détecté
    assert result == result_attendu


def test_plusieurs_doublons():
    # arrange
    liste = [5, 5, 5]

    # act
    result = verifier_doublons(liste)

    # assert
    result_attendu = True
    assert result == result_attendu
# Simon 

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