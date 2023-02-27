import unittest

def convertion(x):
    return (x-32)*5/9

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(convertion(32), 0)

if __name__ == '__main__':
    unittest.main()
