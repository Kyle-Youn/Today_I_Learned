import torch

# GPU가 사용 가능한지 확인
is_gpu_available = torch.cuda.is_available()

print(is_gpu_available)      # True 또는 False 출력
