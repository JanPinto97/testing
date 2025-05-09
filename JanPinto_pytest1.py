from prova_escrita_05 import *
import pytest

# Comanda per pasar varis comprovacions amb dades diferents   
@pytest.mark.parametrize("categoria, r_esperat",[("novel·la",['El Quixot', 'Crim i Càstig']),("fantasia",['El Senyor dels Anells'])])
def test_llibres_categoria(categoria, r_esperat):
    """
    Funció test per comprovar la funció llibres_per_categoria() x nombre de vegades
    """
    r = llibres_per_categoria(biblioteca,categoria)
    assert r == r_esperat

# Comanda per pasar varis comprovacions amb dades diferents   
@pytest.mark.parametrize("llibre, r_esperat",[("1984",False),("El Senyor dels Anells",False)])    
def test_esta_disponible(llibre, r_esperat):
    """
    Funció test per comprovar la funció esta_disponible() x nombre de vegades
    """
    r = esta_disponible(biblioteca,llibre)
    assert r == r_esperat

# Comanda per pasar varis comprovacions amb dades diferents       
@pytest.mark.parametrize("usuari, r_esperat",[("Pere",True),("Joan",False)])    
def test_usuari_te_prestecs(usuari, r_esperat):
    """
    Funció test per comprovar la funció usuari_te_prestecs() x nombre de vegades
    """
    r = usuari_te_prestecs(biblioteca,usuari)
    assert r == 5

# Comanda per pasar varis comprovacions amb dades diferents   
@pytest.mark.parametrize("llibre, r_esperat",[("El Senyor dels Anells",67),("1984",53)])    
def test_dies_prestec_total(llibre, r_esperat):
    """
    Funció test per comprovar la funció dies_prestec_total() x nombre de vegades
    """
    r = dies_prestec_total(biblioteca,llibre)
    assert r == " "
    
# Jan Pintó