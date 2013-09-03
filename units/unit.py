# coding=utf-8

class Unit(object):

    def __init__(self, s=0, kg=0, m=0, A=0, K=0, mol=0, cd=0):
        self.s = s # seconds
        self.kg = kg # kilogram
        self.m = m # meter
        self.A = A # ampere
        self.K = K # kelvin
        self.mol = mol # mole
        self.cd = cd # candela

    def as_dict(self):
        return {
            's': self.s,
            'kg': self.kg,
            'm': self.m,
            'A': self.A,
            'K': self.K,
            'mol': self.mol,
            'cd': self.cd,
        }

    def iterate_fields(self):
        return self.as_dict().iteritems()

    def iterate_nonzero_fields(self):
        for field, value in self.iterate_fields():
            if value:
                yield (field, value)

    def __mul__(self, other):
        if not isinstance(other, Unit):
            raise ValueError('Invalid multiplication against %s'
                % other.__class__)
        else:
            return Unit(
                s=self.s + other.s,
                kg=self.kg + other.kg,
                m=self.m + other.m,
                A=self.A + other.A,
                K=self.K + other.K,
                mol=self.mol + other.mol,
                cd=self.cd + other.cd,
            )

    def __div__(self, other):
        if not isinstance(other, Unit):
            raise ValueError('Invalid division against %s'
                % other.__class__)
        else:
            return Unit(
                s=self.s - other.s,
                kg=self.kg - other.kg,
                m=self.m - other.m,
                A=self.A - other.A,
                K=self.K - other.K,
                mol=self.mol - other.mol,
                cd=self.cd - other.cd,
            )

    def __imul__(self, other):
        if not isinstance(other, Unit):
            raise ValueError('Invalid multiplication against %s'
                % other.__class__)
        else:
            self.s += other.s
            self.kg += other.kg
            self.m += other.m
            self.A += other.A
            self.K += other.K
            self.mol += other.mol
            self.cd += other.cd
        return self

    def __idiv__(self, other):
        if not isinstance(other, Unit):
            raise ValueError('Invalid division against %s'
                % other.__class__)
        else:
            self.s -= other.s
            self.kg -= other.kg
            self.m -= other.m
            self.A -= other.A
            self.K -= other.K
            self.mol -= other.mol
            self.cd -= other.cd
        return self

    def __pow__(self, power, modulo=None):
        return Unit(
            s=self.s * power,
            kg=self.kg * power,
            m=self.m * power,
            A=self.A * power,
            K=self.K * power,
            mol=self.mol * power,
            cd=self.cd * power,
        )

    def __eq__(self, other):
        if not isinstance(other, Unit):
            raise ValueError('Invalid equality check against %s'
                % other.__class__)
        else:
            return self.as_dict() == other.as_dict()

    def __nonzero__(self):
        for dummy_field in self.iterate_nonzero_fields():
            return True
        return False

    def __str__(self):
        pos = []
        neg = []
        for field, value in self.iterate_nonzero_fields():
            if value > 0:
                target = pos
            else:
                target = neg

            if abs(value) > 1:
                target.append('%s^%s' % (field, abs(value)))
            else:
                target.append(field)

        # 1 / 1
        if not len(neg) and not len(pos):
            return '1'

        if not len(neg):
            if len(pos) > 1:
                # (x) / 1
                return '%s' % ' * '.join(pos)
            else:
                # x / 1
                return pos[0]

        if not len(pos):
            if len(neg) > 1:
                # 1 / (x)
                return '1 / (%s)' % ' * '.join(neg)
            else:
                # 1 / x
                return '1 / %s' % neg[0]

        if len(pos) == 1:
            if len(neg) == 1:
                # x / y
                return '%s / %s' % (pos[0], neg[0])
            else:
                # x / (y)
                return '%s / (%s)' % (pos[0], ' * '.join(neg))
        else:
            if len(neg) == 1:
                # (x) / y
                top = ' * '.join(pos)
                return '%s / %s' % (top, neg[0])
            else:
                # (x) / (y)
                top = ' * '.join(pos)
                bot = ' * '.join(neg)
                return '%s / (%s)' % (top, bot)

class NamedUnit(Unit):

    name = None
    init_map = {}
    init_base = None

    def __init__(self):
        super(NamedUnit, self).__init__(**self.init_map)

    def natural_string(self):
        return super(NamedUnit, self).__str__()

    def __str__(self):
        return self.name

class Second(NamedUnit):
    name = 's'
    init_map = {'s': 1}

class Meter(NamedUnit):
    name = 'm'
    init_map = {'m': 1}

class Kilogram(NamedUnit):
    name = 'kg'
    init_map = {'kg': 1}

class Ampere(NamedUnit):
    name = 'A'
    init_map = {'A': 1}

class Kelvin(NamedUnit):
    name = 'K'
    init_map = {'K': 1}

class Mole(NamedUnit):
    name = 'mol'
    init_map = {'mol': 1}

class Candela(NamedUnit):
    name = 'cd'
    init_map = {'cd': 1}

class Coulomb(NamedUnit):
    name = 'C'
    init_map = {'s': 1, 'A': 1}

class Hertz(NamedUnit):
    name = 'Hz'
    init_map = (Second() ** -1).as_dict()

class Newton(NamedUnit):
    name = 'N'
    init_map = (Meter() * Kilogram() * (Second() ** -2)).as_dict()

class Pascal(NamedUnit):
    name = 'Pa'
    init_map = (Newton() / (Meter() ** 2)).as_dict()

class Joule(NamedUnit):
    name = 'J'
    init_map = (Newton() * Meter()).as_dict()

class Watt(NamedUnit):
    name = 'W'
    init_map = (Joule() / Second()).as_dict()

class Volt(NamedUnit):
    name = 'V'
    init_map = (Watt() / Ampere()).as_dict()

class Farad(NamedUnit):
    name = 'F'
    init_map = (Coulomb() / Volt()).as_dict()

class Ohm(NamedUnit):
    name = 'Ω'
    init_map = (Volt() / Ampere()).as_dict()

class Siemens(NamedUnit):
    name = 'S'
    init_map = (Ampere() / Volt()).as_dict()

class Weber(NamedUnit):
    name = 'Wb'
    init_map = (Volt() * Second()).as_dict()

class Tesla(NamedUnit):
    name = 'T'
    init_map = (Weber() / (Meter() ** 2)).as_dict()

class Henry(NamedUnit):
    name = 'H'
    init_map = (Weber() / Ampere()).as_dict()

UNITS = (Second, Meter, Kilogram, Ampere, Kelvin, Mole, Candela, Hertz,
        Newton, Pascal, Joule, Watt, Coulomb, Volt, Farad, Ohm, Siemens, Weber,
        Tesla, Henry)

if __name__ == '__main__':
    for klass in UNITS:
        instance = klass()
        print klass.__name__, '::', instance.natural_string()


