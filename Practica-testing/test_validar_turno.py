from calculos import validar_turno, HorarioInvalidoError
import pytest	

def test_excepcion__turno():
    with pytest.raises(HorarioInvalidoError):
        validar_turno("lunes", "22:00")
        
def test_validar_turno_10_no_excepcion():
    resultado = validar_turno("lunes", "10:00")
    assert resultado == "todo correcto y agendado" 
