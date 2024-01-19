import pytest
from isopsephism import isopsephy

def test_from_greek_to_num():
    assert isopsephism.isopsephy.convert_word_to_num("ΚΟΥΡΑΙ") == 601
