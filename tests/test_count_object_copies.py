import pytest 
from src.count_object_copies import User
 
def setup_function(function):
    User.count = 0
    
# Positive scenarios

def test_count_with_zero_objects():
    assert User.count == 0

def test_count_with_three_objects():
    u1 = User("Emma", "Foster", 31)
    u2 = User("Charlie", "Wall", 25)
    u3 = User("Crystal", "McGuire", 35)
    
    assert User.count == 3

def test_count_with_first_parameter_none():
    u1 = User(None, "James", 42)
    
    assert User.count == 1

def test_count_with_second_parameter_none():
    u1 = User("Kody", None, 30)
    
    assert User.count == 1

def test_count_with_third_parameter_none():
    u1 = User("Evelynn", "Sherman", None)
    
    assert User.count == 1

def text_count_with_all_none_parameters():
    u1 = User(None, None, None)
    assert User.count == 1

# Negative scenarios 

def test_count_with_incomplete_object_1():
    with pytest.raises(TypeError):
        u1 = User()
        assert User.count == 1

def test_count_with_incomplete_object_2():
    with pytest.raises(TypeError):
        u1 = User("Josh")
        assert User.count == 1

def test_count_with_incomplete_object_3():
    with pytest.raises(TypeError):
        u1 = User("Royce", "Ellis")
        assert User.count == 1

def test_count_with_incomplete_object_4():
    with pytest.raises(TypeError):
        u1 = User(22)
        assert User.count == 1