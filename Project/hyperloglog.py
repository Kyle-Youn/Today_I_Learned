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

    def add(self, item):
        # Hash and split
        h = mmh3.hash(str(item), signed=False)
        idx = h & (self.m - 1)
        w = h >> 24

        # Count leading zeros + 1
        self.buckets[idx] = max(self.buckets[idx], self._leading_zeros(w) + 1)

    def _leading_zeros(self, w):
        return (w | (1 << 50)).bit_length() - 51

    def count(self):
        raw = self.alpha * (self.m ** 2) / sum(2 ** -x for x in self.buckets)
