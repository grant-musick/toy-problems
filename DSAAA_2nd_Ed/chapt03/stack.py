from __future__ import division, absolute_import, print_function, unicode_literals

import unittest




class Stack(object):

    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return len(self._stack) == 0


class SymbolBalancer(Stack):
    __symbol_pairs = [('(',')'), ('{','}'), ('[',']')]
    __starter_to_finisher_map = dict(__symbol_pairs)
    __finisher_to_starter_map = dict([(y,x) for x,y in __symbol_pairs])

    def __init__(self):
        super(SymbolBalancer, self).__init__()
        self._symbol_starters =  SymbolBalancer.__starter_to_finisher_map
        self._symbol_finishers = SymbolBalancer.__finisher_to_starter_map

    def is_balanced(self, symbols):
        for s in symbols:
            print("symbol {}".format(s))
            try:
                if s in self._symbol_starters:
                    self.push(s)
                elif s in self._symbol_finishers:
                    c = self.pop()
                    if self._symbol_finishers[s] != c:
                        return False
                else:
                    pass
            except Exception, ex:
                return False
        return self.is_empty()



class BasicStackTest(unittest.TestCase):

    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())
        with self.assertRaises(IndexError):
            s.pop()

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        self.assertFalse(s.is_empty())


class SymbolBalancingTest(unittest.TestCase):

    def test_balanced(self):
        symbols = """(({[]}))"""
        balancer = SymbolBalancer()
        self.assertTrue(balancer.is_balanced(symbols))

    def test_balanced_other_symbols(self):
        symbols = """(a(b{c[d]e}f)g)h"""
        balancer = SymbolBalancer()
        self.assertTrue(balancer.is_balanced(symbols))


    def test_unbalanced_unordered(self):
        symbols = """([)]"""
        balancer = SymbolBalancer()
        self.assertFalse(balancer.is_balanced(symbols))

    def test_unbalanced_asymmetric(self):
        symbols = """((())"""
        balancer = SymbolBalancer()
        self.assertFalse(balancer.is_balanced(symbols))



if __name__=="__main__":
    unittest.main()


