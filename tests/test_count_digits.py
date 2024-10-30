from src.count_digits import count
import pytest

# Positive scenarios

def test_count_zero():
    assert count(0) == 1

def test_count_digit1():
    assert count(9) == 1

def test_count_digit2():
    assert count(12) == 2

def test_count_digit3():
    assert count(344) == 3

def test_count_digit4():
    assert count(1234) == 4

def test_count_digit5():
    assert count(23456) == 5
    
def test_count_digit7():
    assert count(2345612) == 7
    

# Negative scenarios 

def test_count_none():
    with pytest.raises(TypeError):
        count(None)

def test_count_empty_string():
    with pytest.raises(TypeError):
        count("")

def test_count_number_as_string():
    with pytest.raises(TypeError):
        count("123")
