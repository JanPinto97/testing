from solucio3 import *
from solucio4 import *
import unittest

# Jan Pintó 

class TestComprovarSolucio3A(unittest.TestCase):
    
    def test_1(self):
        '''
        Test per comprovar el funcionament de la funció trobar_min_max_rendiment() amb assertEqual.
        '''
        r = trobar_min_max_rendiment(1, 5, 3)
        self.assertEqual(r,(1,5))
        
    def test_2(self):
        '''
        Test per comprovar el funcionament de la funció comptar_estudiants() amb assertEqual.
        '''
        r = comptar_estudiants(notes_estudiants)
        self.assertEqual(r,4)
        
    def test_3(self):
        '''
        Test per comprovar el funcionament de la funció comptar_estudiants_matèria() amb assertEqual.
        '''
        r = comptar_estudiants_matèria(notes_estudiants, 'Matemàtiques')
        self.assertEqual(r,3)
    
class TestComprovarSolucio3B(unittest.TestCase):
    
    def test_1(self):
        '''
        Test per comprovar el funcionament de la funció trobar_min_max_rendiment() amb assertIn.
        '''
        r = trobar_min_max_rendiment(1, 5, 3)
        self.assertIn(r,((1,5),(2,4),(7,1)))
        
    def test_2(self):
        '''
        Test per comprovar el funcionament de la funció comptar_estudiants() amb assertIn.
        '''
        r = comptar_estudiants(notes_estudiants)
        self.assertIn(r,(1,2,4))
        
    def test_3(self):
        '''
        Test per comprovar el funcionament de la funció comptar_estudiants_matèria() amb assertIn.
        '''
        r = comptar_estudiants_matèria(notes_estudiants, 'Matemàtiques')
        self.assertIn(r,(8,3,1))
        
class TestComprovarSolucio4A(unittest.TestCase):
    
    def test_1(self):
        '''
        Test per comprovar el funcionament de la funció cercar_el() amb assertEqual.
        '''
        r = cercar_el(m_ex, 1)
        self.assertEqual(r,(True, None))
    
    def test_2(self):
        '''
        Test per comprovar el funcionament de la funció sumar_fila() amb assertEqual.
        '''
        r = sumar_fila(m_ex, 0)
        self.assertEqual(r,6)
        
    def test_3(self):
        '''
        Test per comprovar el funcionament de la funció sumar_matriu() amb assertEqual.
        '''
        r = sumar_matriu(m_ex)
        self.assertEqual(r,45)
        
    def test_4(self):
        '''
        Test per comprovar el funcionament de la funció transformar() amb assertEqual.
        '''
        r = transformar(m_ex,1,"+")
        self.assertEqual(r,None)
           
class TestComprovarSolucio4B(unittest.TestCase):   
        
    def test_1(self):
        '''
        Test per comprovar el funcionament de la funció cercar_el() amb assertTrue.
        '''
        r = cercar_el(m_ex, 1)
        self.assertTrue(r,(True, None))
    
    def test_2(self):
        '''
        Test per comprovar el funcionament de la funció sumar_fila() amb assertTrue.
        '''
        r = sumar_fila(m_ex, 0)
        self.assertTrue(r,6)
        
    def test_3(self):
        '''
        Test per comprovar el funcionament de la funció sumar_matriu() amb assertTrue.
        '''
        r = sumar_matriu(m_ex)
        self.assertTrue(r,45)
        
    def test_4(self):
        '''
        Test per comprovar el funcionament de la funció transformar() amb assertFalse.
        '''
        r = transformar(m_ex,1,"+")
        self.assertFalse(r,None)
        
# Executar els testos        
if __name__ == '__main__':
    unittest.main()