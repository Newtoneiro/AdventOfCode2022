import os
import sympy as sp
from sympy import Eq
from collections import defaultdict

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

listeners = defaultdict(list)
values = {}


class Listener:
    def __init__(self, name, operands, operation):
        self.name = name
        self.operands = operands
        self.operation = operation
        self.check()

    def trigger(self, name, val):
        self.operands[name] = val
        self.check()

    def check(self):
        if len([v for v in self.operands.values() if v]) == 2:
            name1, op, name2 = self.operation.split(" ")
            val = 0
            if op == "+":
                val = self.operands[name1] + self.operands[name2]
            elif op == "-":
                val = self.operands[name1] - self.operands[name2]
            elif op == "*":
                val = self.operands[name1] * self.operands[name2]
            elif op == "/":
                val = self.operands[name1] / self.operands[name2]

            values[self.name] = val

            for l in listeners[self.name]:
                if l.name != self.name:
                    l.trigger(self.name, val)


def main():
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            m_name, operation = line.split(":")
            if m_name == 'humn':
                continue
            operation = operation.strip()
            if operation.isnumeric():
                values[m_name] = int(operation)
                if listeners[m_name]:
                    for l in listeners[m_name]:
                        l.trigger(m_name, int(operation))
            else:
                name1, _, name2 = operation.split(" ")
                if m_name == 'root':
                    root_blockers = [name1, name2]
                operands = {}
                for name in [name1, name2]:
                    operands[name] = values.get(name, None)
                listener = Listener(m_name, operands, operation)

                for k, v in operands.items():
                    if v is None:
                        listeners[k].append(listener)

    comparator, equation = (root_blockers[0], root_blockers[1]) if values.get(root_blockers[0]) else (root_blockers[1], root_blockers[0])
    humn = sp.symbols('humn')
    listeners['humn'][0].trigger('humn', humn)
    print(values[equation], values[comparator])
    sol = int(sp.solve(Eq(values[equation], values[comparator]), humn)[0])
    print(sol)


if __name__ == "__main__":
    main()
