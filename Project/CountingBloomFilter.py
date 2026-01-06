import hashlib

class CountingBloomFilter:
  def __init__(self, size, num_hashes):
    self.size = size
    self.num_hashes = num_hashes
    self.counting_array = [0] * size

  def _hashes(self, item):
    result = []
    for i in range(self.num_hashes):
        h = hashlib.md5(f"{item}{i}".encode()).hexdigest()
        result.append(int(h, 16) % self.size)
    return result

  def add(self, item):
      for idx in self._hashes(item):
         self.counting_array[idx] += 1

  def check(self, item):
      return all(self.counting_array[idx] > 0 for idx in self._hashes(item))

  def delete(self, item):
    if self.check(item):
        for idx in self._hashes(item):
            self.counting_array[idx] -= 1
        return True
    else:
        return False
