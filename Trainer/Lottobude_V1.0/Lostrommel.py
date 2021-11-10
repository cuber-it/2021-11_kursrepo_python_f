import random

class Lostrommel:
    def ziehung(self):
        return random.sample(range(1,50), 6)

if __name__ == "__main__":
    l = Lostrommel()
    print(l.ziehung())