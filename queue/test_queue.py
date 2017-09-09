import unittest

from queue import Queue


class TestQueueMethods(unittest.TestCase):

    def setUp(self):
        self.q = Queue()
    
    def tearDown(self):
        pass

    def test_enqueue(self):
        self.q.enqueue(1) 
        self.assertEqual(str(self.q), '[1]')

    def test_dequeue(self):
        self.q.enqueue(1) 
        d = self.q.dequeue()
        self.assertEqual(d, 1)

if __name__ == '__main__':
    unittest.main()
