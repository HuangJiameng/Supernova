import unittest
from supernova.motto.motto import verifyMottoAg



class TestVerifyMottoAg(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass
    
    def test_verifyMottoAg_right(self):
        right_motto = "Keep it simple and stupid"
        self.assertEqual(verifyMottoAg(right_motto), True)
        
    def test_verifyMottoAg_wrong(self):
        wrong_motto = "I'm a wrong motto"
        self.assertEqual(verifyMottoAg(wrong_motto), False)
    
    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
