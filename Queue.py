import array

class Queue:
    def __init__(self, size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i',range(size_max))

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max

    def enqueue(self, new_input):
        if self.size == self.max:
            return False
        self.data[self.tail] = new_input
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0

        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.size >= 0 and self.size <= self.max
        if self.size == self.max:  # same as is_full(self)
            assert self.tail == 0
        if self.tail > self.head:
            assert (self.tail - self.head) == self.size
        if self.head > self.tail:
            assert (self.head - self.tail) == (self.max - self.size)
        if self.tail == self.head:
            assert (self.is_full() or self.is_empty())

        return

def test1():
    q = Queue(3)

    res = q.is_empty
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

    res = q.is_empty()
    if not res:
        print("test1.6 NOT ok")  # after enqueue() twice, then dequeue() twice, q should be empty
        return

    print("test 1 ok!")

    #self.assertEqual(True, False)

def test2():
    q = Queue(5)

    for i in range(q.max):
        q.enqueue(i)
    # tail should now be 0 since q is full
    if q.tail != 0:
        print("test 2.2 NOT ok - tail not reset to 0 after full enqueue")

    res = q.enqueue(100)
    if res:
        print("test2.1 NOT ok - enqueue() did not return false when trying to enqueue past max size")
        return

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    res = q.dequeue()
    if not (res is None):
        print("test 2.2 failed - dequeue did not return None after all items removed")
        return

    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    # head should now be 0
    if q.head != 0:
        print("test 2.3 failed - head did not reset to 0 after filling queue")
        return

    print("test 2 ok!")

def test3():
    q = Queue(5)

    if not q.is_empty():
        print("test 2.1 failed - q.empty did not return true when q was empty")
        return

    for i in range(q.max):
        q.enqueue(i)
    if not q.is_full():
        print("test 3.2 failed - q.full did not return true when q was full")
        return

    print("test 3 ok!")

test1()
test2()
test3()
