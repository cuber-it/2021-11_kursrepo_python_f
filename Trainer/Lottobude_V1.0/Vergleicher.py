class Vergleicher:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b
        self.intersection = None
        self.left_only = None
        self.right_only = None

    def compare(self):
        set_a = set(self.list_a)
        set_b = set(self.list_b)

        self.intersection = tuple(set_a.intersection(set_b))  # Schnittmenge in a und b
        self.left_only = tuple(set_a.difference(set_b))       # Differenz, in a nicht in b
        self.right_only = tuple(set_b.difference(set_a))      # Differenz, in b nicht in a

        #return self.left_only, self.intersection, self.right_only
        return self


if __name__ == "__main__":
    v = Vergleicher([1,2,3,4], [3,4,5,6])
    print(len(v.compare().intersection) == 6)
