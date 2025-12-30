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
