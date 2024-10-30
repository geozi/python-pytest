from src.sort_string import sort 
import pytest 

# Positive scenarios 

def test_sort_one_letter_string():
    assert sort('w') == 'w'

def test_sort_multi_letter_string():
    assert sort('cba') == 'abc'

def test_sort_numeric_string():
    assert sort('04213') == '01234'

def test_sort_alphanumeric_string():
    assert sort('random123') == '123admnor'
    
def test_sort_whitespace_string():
    assert sort('   ') == '   '

def test_sort_empty_string():
    assert sort('') == ''

# Negative scenarios

def test_sort_none():
    with pytest.raises(TypeError):
        assert sort(None)

def test_sort_number():
    with pytest.raises(TypeError):
        assert sort(12)
        