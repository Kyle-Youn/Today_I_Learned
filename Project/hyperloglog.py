import mmh3

class HyperLogLog:
    def __init__(self, precision=14):
        self.m = 1 << precision    # 2^precision buckets
        self.buckets = [0] * self.m
        self.alpha = self._get_alpha(self.m)
