class Nums:
    def __init__(self):
        self.number = 1

    def __next__(self):
        while True:
            num = self.number
            self.number += 1
            if self._is_prime(num) is True:
                return num

    def __iter__(self):
        return self

    def _is_prime(self, number):
        if number != 1:
            for x in range(2, number):
                if number % x == 0:
                    return False
            return True
        else:
            return False