from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band, Musician, Guitarist, Drummer, Bassist
import pytest
def test_version():
    assert __version__ == '0.1.0'
aziz = Guitarist('Aziz') 
saleh = Drummer('Saleh')
emad = Bassist('Emad')    
tarbanin = Band('tarbanin')
tarbanin.add_members(aziz)
tarbanin.add_members(saleh)
tarbanin.add_members(emad)
def test_to_list():
    expected = [aziz,saleh,emad]
    actual = tarbanin.to_list()
    assert  actual == expected
def test_play_solo():
    expected = 'Saleh Play solo'
    actual = saleh.play_solo()
    assert actual == expected
def test_play_solos():
    expected = "Aziz Play solo\nSaleh Play solo\nEmad Play solo\n"
    actual = tarbanin.play_solos()
    assert actual == expected
def test_str():
    expected = "Guitarist <Aziz>"
    actual = aziz.__str__()
    assert actual == expected
def test_rper():
    expected = " 'Emad' "
    actual = emad.__repr__()
    assert actual == expected
def test_get_instrument():
    expected = "Drummer"
    actual = saleh.get_instrument()
    assert actual == expected