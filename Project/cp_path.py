import os
import shutil

input_path = ''
store_dir = ''

if not os.path.exists(store_dir):
    os.makedirs(store_dir)

print("input_path 내용:")
print(os.listdir(input_path))

for item in os.listdir(input_path):
    source_item_path = os.path.join(input_path, item)
    store_item_path = os.path.join(store_dir, item)
    print(f"처리 중인 항목: {item}")

    try:
        if os.path.isdir(source_item_path):
            shutil.copytree(source_item_path, store_item_path, dirs_exist_ok=True)
            print(f"디렉터리 복사 완료: {source_item_path} -> {store_item_path}")
        elif os.path.isfile(source_item_path):
            shutil.copy2(source_item_path, store_item_path)
            print(f"파일 복사 완료: {source_item_path} -> {store_item_path}")
    except Exception as e:
        print(f"오류 발생: {e}")
