# 모델 준비
import torch
from torchvision.models import resnet50, ResNet50_Weights
import rebel  # RBLN 컴파일러

# 토치비전 ResNet50 모델 준비
weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)
model.eval()


# 모델 컴파일
compiled_model = rebel.compile_from_torch(
    model,
    [("input", [1, 3, 224, 224], torch.float32)],
    # 호스트에 NPU가 설치되어 있는 경우, 아래의 `npu`인자는 명시하지 않아도 자동으로 감지됩니다. 
    npu="RBLN-CA12",
)
