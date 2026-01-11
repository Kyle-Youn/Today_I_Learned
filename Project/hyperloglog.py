import mmh3

class HyperLogLog:
    def __init__(self, precision=14):
        self.m = 1 << precision    # 2^precision buckets
        self.buckets = [0] * self.m
        self.alpha = self._get_alpha(self.m)

    def _get_alpha(self, m):
        if m >= 128: return 0.7213 / (1 + 1.079 / m)
        elif m >= 64: return 0.709
        elif m >= 32: return 0.697
        return 0.5
