import hashlib

class BloomFilter:
  def __init__(self, size, num_hashes):
    self.size = size
    self.num_hashes = num_hashes
    self.bit_array = [0] * size
