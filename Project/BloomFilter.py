import hashlib

class BloomFilter:
  def __init__(self, size, num_hashes):
    self.size = size
    self.num_hashes = num_hashes
    self.bit_array = [0] * size

  def _hashed(self, item):
    """여러 해시값 생성"""
    result = []
    for i in range(self.num_hashes):
      h = hashlib.md5(f"{item}{i}".encode()).hexdigest()
      result.append(int(h, 16) % self.size)
    return result

  def add(self, item):
    """원소 추가"""
    for pos in self._hashes(item):
      self.bit_array[pos] = 1

  def check(self, item):
    return all(self.bit_array[pos] == 1 for pos in self._hashes(item))


# 사용 예시
bf = BloomFilter(size=100, num_hashes=3)
bf.add("apple")
bf.add("banana")

print(bf.check("apple"))    # True
print(bf.check("orange:))    # False (또는 False Positive)
