import pytest
from Sudoku import *

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