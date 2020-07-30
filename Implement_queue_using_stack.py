'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
'''


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.storage = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.size += 1
        self.storage.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        else:
            self.size -= 1
            return self.storage.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            return None
        return self.storage[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.size == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
