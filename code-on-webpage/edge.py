class Edge:
    def __init__(self, f, t, w=None):
        # Create an edge with weight w from Node f to Node t,
        # f and t are node ids and w is a number
        self.f = f
        self.t = t
        self.w = w

    def update_weight(self, w):
        if self.w is None:
            self.w = w
        else:
            # Don't replace a shorter road with a longer one
            # in the case of two or more roads between the same nodes
            self.w = min(w, self.w)
