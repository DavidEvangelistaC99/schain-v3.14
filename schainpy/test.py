class Operation:

    #ELEMENTNAME = 'Operation'
    ELEMENTNAME = 'Parameter'

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.inputId = None
        self.parameters = {}
        self.operations = []

    def __str__(self):

        if self.ELEMENTNAME == 'Operation':
            s = '  {}[id={}]\n'.format(self.name, self.id)
        else:
            s = '{}[id={}, inputId={}]\n'.format(
                self.name, self.id, self.inputId
            )

        for key, value in self.parameters.items():
            if self.ELEMENTNAME == 'Operation':
                s += '    {}: {}\n'.format(key, value)
            else:
                s += '  {}: {}\n'.format(key, value)

        for conf in self.operations:
            s += str(conf)

        return s

if __name__ == "__main__":

    op = Operation("SpectraLagProc", 10)

    op.parameters = {
        "nFFTPoints": 128,
        "window": "hamming",
        "axis": 1
    }

    print(op)