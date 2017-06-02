from __future__ import division, absolute_import, print_function, unicode_literals



class Literal(object):
    def __init__(self, coeficient, power):
        self.coeficient = coeficient
        self.power = power

    def __str__(self):
        return str(self.coeficient) + "X^" + str(self.power)


class Polynomial(object):
    def __init__(self, coeff_pow_tuples):
        """
        Takes a list of Literals and sorts by power from greatest to least.
        """
        self.list = []
        # sort the list by powers desc
        coeff_pow_tuples.sort(key=lambda x: x.power, reverse=True)

        for literal in coeff_pow_tuples:
            self.list.append(literal)


    def __str__(self):
        return " + ".join([str(x) for x in self.list])

    def __add__(self, other):
        retval = []
        self_index = 0
        self_length = len(self.list)
        other_index = 0
        other_length = len(other.list)
        done = False
        while not done:
            if self_index == self_length and other_index == other_length:
                done = True
            elif self_index == self_length:
                retval.append(other.list[other_index])
                other_index += 1
            elif other_index == other_length:
                retval.append(self.list[self_index])
                self_index += 1
            elif self.list[self_index].power > other.list[other_index].power:
                retval.append(self.list[self_index])
                self_index += 1
            elif self.list[self_index].power < other.list[other_index].power:
                retval.append(other.list[other_index])
                other_index += 1
            else: # they are equal
                retval.append(Literal(self.list[self_index].coeficient + other.list[other_index].coeficient, 
                    self.list[self_index].power))
                self_index += 1
                other_index += 1
        p = Polynomial([])
        p.list = retval
        return p


    def __add__(self, other):
        self_iter = iter(self.list)
        other_iter = iter(other.list)









if __name__ == "__main__":
    l = Literal
    p1 = Polynomial([l(5,6), l(1,2), l(3,0)])
    print (p1)

    p2 = Polynomial([l(5,3), l(1,9), l(3,0)])
    print (p2)

    p3 = p1 + p2

    print (p3)








