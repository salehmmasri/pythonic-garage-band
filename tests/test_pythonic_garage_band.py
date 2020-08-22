from pythonic_garage_band.pythonic_garage_band import Band
import pytest

@pytest.fixture
def prep_data():
    aziz = Band.Guitarist('aziz') # preparing data
    saleh = Band.Drummer('saleh')
    emad = Band.Bassist('eamad')
    return {'aziz':aziz,'saleh':saleh,'emad':emad}

def test_play_solo(prep_data):
    expected = "Play Guitar"
    actual = prep_data['aziz'].play_solo()
    assert actual == expected

def test_get_instrument(prep_data):
    expected = "Drummer"
    actual = prep_data['saleh'].get_instrument()
    assert actual == expected

def test_str(prep_data):
    expected = "Drummer <saleh>"
    actual = prep_data['saleh'].__str__()
    assert actual == expected