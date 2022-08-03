import unittest
from supernova.motto.motto import verifyMottoJiamengHuang



class TestVerifyMottoJiamengHuang(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass
    
    def test_verifyMottoJiamengHuang_right(self):
        right_motto = "Keep it simple and stupid"
        self.assertEqual(verifyMottoJiamengHuang(right_motto), True)
        
    def test_verifyMottoJiamengHuang_wrong(self):
        wrong_motto = "I'm a wrong motto"
        self.assertEqual(verifyMottoJiamengHuang(wrong_motto), False)
    
    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
