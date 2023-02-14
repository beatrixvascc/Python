import unittest

import change


class Test_uppercase(unittest.TestCase):
    def testUpper(self):
        word = "love"
        result=change.changeWord(word)
        self.assertEqual(result,"LOVE")
        
if __name__=="__main__":
    unittest.main()      