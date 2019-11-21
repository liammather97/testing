import pytest
from python_exercises import anti_vowel

def test_anti_vowel_vowel():
    assert anti_vowel.anti_vowel("aeiouAEIOU")==""

def test_anti_vowel_cons():
    assert anti_vowel.anti_vowel("BCDFGHJKLMNPQRSTVXZ")=="BCDFGHJKLMNPQRSTVXZ"

def test_anti_vowel_word():
    assert anti_vowel.anti_vowel("random")=="rndm"
