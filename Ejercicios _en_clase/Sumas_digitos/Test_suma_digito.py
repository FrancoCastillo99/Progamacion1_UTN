import pytest
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

@pytest.mark.parametrize ("a, res", [
    (174,12),
    (458,17),
])
def test_add_digit(a,res):
    assert funciones.add_digit(a) == res

@pytest.mark.parametrize("a, res",[
    ([145,255],400),
    ([100,450],550),
])
def test_summation(a,res):
    assert funciones.summation(a) == res