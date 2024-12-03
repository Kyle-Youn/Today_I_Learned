
import torch
from torchvision.io.image import read_image
from torchvision.models import resnet50, ResNet50_Weights
import urllib.request
import rebel  # RBLN 런타임

# 입력 데이터 준비
img_url = "https://rbln-public.s3.ap-northeast-2.amazonaws.com/images/tabby.jpg"
img_path = "./tabby.jpg"
with urllib.request.urlopen(img_url) as response, open(img_path, "wb") as f:
    f.write(response.read())
img = read_image(img_path)
weights = ResNet50_Weights.DEFAULT
preprocess = weights.transforms()
batch = preprocess(img).unsqueeze(0)

# 컴파일된 모델 불러오기
module = rebel.Runtime("resnet50.rbln", tensor_type="pt")

# 추론
rebel_result = module(batch)

# 결과 확인
score, class_id = torch.topk(rebel_result, 1, dim=1)
category_name = weights.meta["categories"][class_id]
print("Top1 category: ", category_name)
