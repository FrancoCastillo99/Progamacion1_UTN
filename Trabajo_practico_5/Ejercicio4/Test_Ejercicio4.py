import pytest
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

@pytest.mark.parametrize("a, b, res",[
    (20,4,True),
    (25,5,True),
])
def test_is_multiple(a,b,res):
    assert funciones.is_multiple(a,b) == res