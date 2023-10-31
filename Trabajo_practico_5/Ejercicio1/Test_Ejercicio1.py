import pytest
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

@pytest.mark.parametrize ("a, res", [
    (41699948,True),
    (45845782,True),
])
def test_valid_dni(a,res):
    assert funciones.valid_dni(a) == res

