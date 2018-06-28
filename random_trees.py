
class chain():
    def __init__(self, size):
        self.size = size
        self.probs = [1]*(size-1)
        self.exps = [0]*size
        self.vars = [0]*size

        self.exps[-1] = 1

    def set_probs(self, probs):
        if len(probs) != len(self.probs):
            raise "length of probs array is not legal"

        self.probs = probs

    def calc_exps(self):
        # calculate the probs from the end to the beginning
        for i in range(len(self.probs)-1, -1, -1):
            self.exps[i] = self.probs[i]*self.exps[i+1] + 1

    def calc_vars(self):
        for i in range(len(self.probs)-1, -1, -1):
            p_i = self.probs[i]
            self.vars[i] = p_i*self.vars[i+1] + (1-p_i)*p_i*self.exps[i+1]


class dag_tree():
    def __init__(self, height):
        self.height = height
        self.size = 2**height
        self.probs = [1] * (self.size - 1)
        self.exps = [0] * self.size
        self.vars = [0] * self.size

if __name__ == "__main__":
    n = 4
    c = chain(n)
    probs = [1 - 1./(n) for i in range(n-1)]
    c.set_probs(probs)
    c.calc_exps()
    c.calc_vars()
    print c.exps
    print c.vars
