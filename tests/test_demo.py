import unittest
from util4tests import run_single_test, log
import os

from pyodv import ODV_Struct  
 
class TestStringMethods(unittest.TestCase):
    # def test_upper(self):
    #     log.info("testing str.upper()")
    #     self.assertEqual('foo'.upper(), 'FOO')
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    def test_modelError(self):
        test_files = './tests/test_files/'
        all_valid = True
        for filename in os.listdir(test_files):
            f = os.path.join(test_files, filename)
            # checking if it is a file
            if os.path.isfile(f):
                struct = None
                isValid = False
                try:
                    struct = ODV_Struct(f)
                    isValid = struct.valid_output()
                    all_valid = all_valid and isValid
                except Exception as err:
                    log.warning(err)

        self.assertTrue(all_valid)


if __name__ == "__main__":
    run_single_test(__file__)
