from assignment2.Vector import Vec


class Matrix(object):
    def __init__(self, lables, function):
        self.lables = lables
        self.function = function
        self.rows = self.lables[0]
        self.cols = self.lables[1]

    @staticmethod
    def identity_matrix(D):
        return Matrix((D, D), {(d, d): 1 for d in D})

    def __str__(self):
        print '   ',
        for x in self.lables[1]:
            print x + ' ',
        print
        print '  ',
        print '-' * 10
        for x in self.lables[0]:
            print x + ' |',
            for z in self.lables[1]:
                print str(self.function[(x, z)] if (x, z) in self.function else 0) + ' ',
            print
        return ''

    def mat2coldict(self):
        return {x: Vec(self.lables[0], {row: self.function[(row, x)] if (row, x) in self.function else 0
                                        for row in self.lables[0]}) for x in self.lables[1]}

    def transpose(self):
        return Matrix((self.cols, self.rows),
                      {(col, row): self.function[(row, col)] if (row, col) in self.function else 0
                       for row in self.rows for col in self.cols})


M = Matrix(({'1', '2', '3'}, {'a', 'b', 'c'}), {('1', 'a'): 123})
print M
M = M.transpose()
print M
