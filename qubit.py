# ANAISA FORTI DA FONSECA
# 11811ECP012

import numpy as np


# altera funções trigonométricas para zerar senos e cossenos coerentes
npsin = np.sin
npcos = np.cos

def sin(angle):
    if(angle%np.pi == 0):
        return 0.0
    return npsin(angle)

def cos(angle):
    if((angle+np.pi/2)%np.pi == 0):
        return 0.0
    return npcos(angle)

np.sin = sin
np.cos = cos


class Qubit:
    def __init__(self):
        # theta e phi: esfera de Bloch
        # a e b: função de onda
        # default: |0)
        self.theta = 0.0
        self.phi   = 0.0
        self.a     = 1.0
        self.b     = 0.0+0.0j

    def wf(self):
        # função de onda em forma vetorial
        return np.array([[self.a],[self.b]])

    def __repr__(self):
        return str(self.wf())

    def set_bs(self, theta, phi):
        if(not(0.0 <= theta <= np.pi)):
            theta %= np.pi
        if(not(-np.pi <= phi <= np.pi)):
            phi = phi%(2*np.pi) - 2*np.pi
        self.theta = theta
        self.phi   = phi

    def set_pa(self, a, b):
        aux = np.abs(a)**2 + np.abs(b)**2
        a = np.sqrt(abs(a)**2/aux)
        b = np.sqrt(abs(b)**2/aux)
        ma, pa = np.abs(a), np.angle(a)
        mb, pb = np.abs(b), np.angle(b)
        self.a = ma
        self.b = mb*np.exp(1j*(pb-pa))

    # def validate(self):
    #     if(np.sqrt(np.abs(self.a)**2 + np.abs(self.b)**2) < 1):



if __name__ == "__main__":
    q = Qubit()
    print(q)
    q.set_bs(50*2*np.pi+3/2*np.pi, 50*2*np.pi+3/2*np.pi)
    q.set_pa(np.sqrt(2)/2, -1j*(np.sqrt(2)/2))
    print(q.a, q.b)
    print(np.sqrt(2)/2, -1j*np.sqrt(2)/2)