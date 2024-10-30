from src.reverse_string import reverse
import pytest

# Positive scenarios 

def test_reverse_letter_string():
    assert reverse("hello") == "olleh"

def test_reverse_numeric_string():
    assert reverse("01234") == "43210"
    
def test_reverse_alphanumeric_string():
    assert reverse("random123") == "321modnar"

def test_reverse_whitespace_string():
    assert reverse("   ") == "   "

def test_reverse_empty_string():
    assert reverse("") == ""

# Negative scenarios 

def test_reverse_none():
    with pytest.raises(TypeError):
        assert reverse(None)

def test_reverse_no_input():
    with pytest.raises(TypeError):
        assert reverse()