class Edge:
    def __init__(self, f, t, w=None):
        # f and t are node ids from node f to t
        self.f = f
        self.t = t
        # w is the weight of the edge
        self.w = w

    def update_weight(self, w):
        if self.w is None:
            self.w = w
        else:
            # Don't replace a shorter road with a longer one
            # in case of two or more roads between the same nodes
            self.w = min(w, self.w)
