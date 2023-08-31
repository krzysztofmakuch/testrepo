import pytest
#from ...gromacs_tools.rdf_change_in_time import g_rdf_change_during_simulation
#from ....rdf_change_in_time import g_rdf_change_during_simulation
from ...rdf_change_in_time import g_rdf_change_during_simulation


def test_positive_remove_xvg():
    assert g_rdf_change_during_simulation.remove_xvg('alama.xvg') == 'alama', 'positive pass'


def test_negative_remove_xvg():
    assert g_rdf_change_during_simulation.remove_xvg('alama.txt') == 'alama.txt'


def test_noextension_remove_xvg():
    assert g_rdf_change_during_simulation.remove_xvg('alama') == 'alama'


#changed this behavior handling in the code
"""def test_tooshort_remove_xvg():
    with pytest.raises(IndexError):
        g_rdf_change_during_simulation.remove_xvg('m')"""


def test_onlyextension_remove_xvg():
    assert g_rdf_change_during_simulation.remove_xvg('.xvg') == ''
