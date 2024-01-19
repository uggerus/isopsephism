import pytest
import isopsephism

def test_from_greek_to_num():
    assert isopsephism.greek_isopsephy.convert_word_to_num("ΚΟΥΡΑΙ") == 601
