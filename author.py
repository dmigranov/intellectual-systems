class Author:
    def __init__(self, name):
        self.name = name
        self.inited = False


    def add_transition_matrix(self, T):
        if not self.inited:
            self.T = T
            self.inited = True
        else:
            self.T = self.T + T 
