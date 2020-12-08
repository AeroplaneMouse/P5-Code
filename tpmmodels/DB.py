from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps

class DB:
    def __init__(self, pattern):
        self.Pattern = pattern
        self.Prfx_s_ep = remove_corresponding_eps(pattern)
        self.ES = []
        self.Paren_nums = []
