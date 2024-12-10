import json
import yaml
import time

data = {"name": "Alice", "age": 25, "skills": ["Python", "JavaScript"], "active": True}

# JSON 직렬화/역직렬화
start = time.time()
for _ in range(100000):
    serialized = json.dumps(data)
    deserialized = json.loads(serialized)
end = time.time()
print(f"JSON Time: {end - start} seconds")

# YAML 직렬화/역직렬화
start = time.time()
for _ in range(100000):
    serialized = yaml.dump(data)
    deserialized = yaml.safe_load(serialized)
end = time.time()
print(f"YAML Time: {end - start} seconds")
