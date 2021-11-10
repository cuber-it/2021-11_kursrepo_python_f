import messgeraete

class Messung:
    def __init__(self, mg):
        self.mg = mg
        self.result = []
    
    def run(self, iter=1):
        if iter <= 0 or iter > 10:
            raise RuntimeError("Invalid iter-Value for measurement: ", iter)
        self.result = []
        for _ in range(0, iter): # _ ist dummy variable
            self.result.append(self.mg.do_measurement().get_values())
            self.mg.set_values()
        return self

if __name__ == "__main__":
    m = Messung(messgeraete.MG_R())
    assert len(m.run().result) == 1
    assert len(m.run(3).result) == 3
    m.run(100)