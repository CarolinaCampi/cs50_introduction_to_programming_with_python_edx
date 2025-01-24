class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError("The capccity should be a positive integer.")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("The capacity of the cookie jar has been exceeded.")
        self.size += n


    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies on the cookie jar.")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @size.setter
    def size(self, size):
        self._size = size

def main():
    cookie_jar = Jar(capacity=10)
    cookie_jar.deposit(10)
    print(cookie_jar)
    cookie_jar.withdraw(5)
    print(cookie_jar)

if __name__ == "__main__":
    main()
