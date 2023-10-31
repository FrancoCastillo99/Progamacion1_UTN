import pytest
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

@pytest.mark.parametrize("a, b, res",[
    (20,10,15),
    (25,35,30),
])
def test_average_temperature(a,b,res):
    assert funciones.average_temperature(a,b) == res