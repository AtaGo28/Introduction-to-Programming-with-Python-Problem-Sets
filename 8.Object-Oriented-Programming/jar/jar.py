class Jar:
    def __init__(self, capacity=12, size=0):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = size
        
        
    def __str__(self):
        return self.size * "🍪"


    def deposit(self, n):
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError
        self._size += n


    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
    
def main():
    jar = Jar()
    jar.deposit(3)
    print(jar)
    print(jar.capacity)
    print(jar.size)
    jar.withdraw(3)
    print(jar)
    print(jar.capacity)
    print(jar.size)
        
if __name__ == "__main__":
    main()