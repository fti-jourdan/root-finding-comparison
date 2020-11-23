from .base import Formula
import time

class Secant(Formula):
    def __init__(self):
        self._errors = []
        self._xrs = []

    def generate_next(self, x0, x1):
        fx1 = self.f(x1)
        return x1 - (fx1 * (x1-x0)) / (fx1 - self.f(x0))

    def compute(self, xi, xu, es):
        self.reset()
        start = time.time_ns()

        iter = 1


        x0, x1 = xi, xu
        ea = 100
        while ea > es:
            xi = self.generate_next(x0, x1)

            if iter > 1:
                ea = self.generate_error(xi, x1)

            self.append_xrs(xi)
            self.append_errors(ea)

            x0, x1 = x1, xi
            iter += 1
        self.set_total_iter(iter)
        self.set_exe_time(time.time_ns()-start)