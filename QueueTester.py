import unittest
import Queue

class MyTestCase(unittest.TestCase):
    def test1(self):
        q = Queue(3)

        res = q.empty
        if not res:
            print("test1.1 NOT ok")  # q.empty() should return true immediately after creating q, since it is empty
            return

        res = q.enqueue(10)
        if not res:
            print("test1.2 NOT ok")  # q.enqueue should return true while there's room, and since this is the first enqueue operation, it should have room
            return

        res = q.enqueue(11)
        if not res:
            print("test1.3 NOT ok")  # q.enqueue should still return true since this is the second enqueue operation, and 2 < 3 (the max size as defined above)
            return

        x = q.dequeue()
        if x != 10:
            print("test1.4 NOT ok")  # 10 was the first enqueued variable, so the first dequeue() should return it
            return

        x = q.dequeue()
        if x != 11:
            print("test1.5 NOT ok")  # 11 was the second enqueue() variable, so the second dequeue() sould return it
            return

        res = q.empty()
        if not res:
            print("test1.6 NOT ok")  # after enqueue() twice, then dequeue() twice, q should be empty
            return

        print("test1 ok!")

        #self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
