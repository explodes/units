from units.unit import Unit


class Measurement(object):

    def __init__(self, magnitude, unit):
        self.magnitude = magnitude
        self.unit = unit

    def __mul__(self, other):
        if isinstance(other, Unit):
            unit = self.unit * other
            magnitude = self.magnitude
        elif isinstance(other, Measurement):
            unit = self.unit * other.unit
            magnitude = self.magnitude * other.magnitude
        elif isinstance(other, (long, int, float)):
            unit = self.unit
            magnitude = self.magnitude * other
            return Measurement(magnitude, unit)
        else:
            raise ValueError('Invalid multiplication against %s' %
                other.__class__)
        return Measurement(magnitude, unit)

    def __div__(self, other):
        if isinstance(other, Unit):
            unit = self.unit / other
            magnitude = self.magnitude
        elif isinstance(other, Measurement):
            unit = self.unit / other.unit
            magnitude = self.magnitude / other.magnitude
        elif isinstance(other, (long, int, float)):
            unit = self.unit
            magnitude = self.magnitude / other
            return Measurement(magnitude, unit)
        else:
            raise ValueError('Invalid division against %s' %
                other.__class__)
        return Measurement(magnitude, unit)

    def __imul__(self, other):
        if isinstance(other, Unit):
            self.unit *= other
        elif isinstance(other, Measurement):
            self.unit *= other.unit
            self.magnitude *= other.magnitude
        else:
            raise ValueError('Invalid multiplication against %s' %
                other.__class__)
        return self

    def __idiv__(self, other):
        if isinstance(other, Unit):
            self.unit /= other
        elif isinstance(other, Measurement):
            self.unit /= other.unit
            self.magnitude /= other.magnitude
        else:
            raise ValueError('Invalid division against %s' %
                other.__class__)
        return self

    def __add__(self, other):
        if isinstance(other, Measurement):
            if not self.unit == other.unit:
                raise ValueError('Cannot add different units')
            unit = self.unit
            magnitude = self.magnitude + other.magnitude
            return Measurement(magnitude, unit)
        else:
            raise ValueError('Invalid addition against %s' %
                other.__class__)

    def __iadd__(self, other):
        if isinstance(other, Measurement):
            if not self.unit == other.unit:
                raise ValueError('Cannot add different units')
            self.magnitude += other.magnitude
            return self
        else:
            raise ValueError('Invalid addition against %s' %
                other.__class__)

    def __sub__(self, other):
        if isinstance(other, Measurement):
            if not self.unit == other.unit:
                raise ValueError('Cannot subtract different units')
            unit = self.unit
            magnitude = self.magnitude - other.magnitude
            return Measurement(magnitude, unit)
        else:
            raise ValueError('Invalid subtraction against %s' %
                other.__class__)

    def __isub__(self, other):
        if isinstance(other, Measurement):
            if not self.unit == other.unit:
                raise ValueError('Cannot subtract different units')
            self.magnitude -= other.magnitude
            return self
        else:
            raise ValueError('Invalid subtraction against %s' %
                other.__class__)

    def __str__(self):
        if self.unit:
            return '%s %s' % (self.magnitude, self.unit)
        else:
            return '%s' % self.magnitude


if __name__ == '__main__':
    from units.unit import Newton

    fig = lambda f: Measurement(float(f), Newton())

    print '2N * 3N', '::', fig(2) * fig(3)
    print '2N / 3N', '::', fig(2) / fig(3)

    print '2N * 3', '::', fig(2) * 3.0
    print '2N / 3', '::', fig(2) / 3.0

    print '2N + 3N', '::', fig(2) + fig(3)
    print '2N - 3N', '::', fig(2) - fig(3)


    N2 = fig(2)
    N3 = fig(3)
    N2 *= N3
    print '2N *= 3N', '::', N2

    N2 = fig(2)
    N3 = fig(3)
    N2 /= N3
    print '2N /= 3N', '::', N2

    N2 = fig(2)
    N3 = fig(3)
    N2 += N3
    print '2N += 3N', '::', N2

    N2 = fig(2)
    N3 = fig(3)
    N2 -= N3
    print '2N -= 3N', '::', N2


