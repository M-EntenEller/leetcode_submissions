// https://leetcode.com/problems/print-in-order

import time

class Foo:
    def __init__(self):
        self.state_lock = 0
        

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.state_lock = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        while self.state_lock != 1:
            time.sleep(0)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.state_lock = 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        while self.state_lock != 2:
            time.sleep(0)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()