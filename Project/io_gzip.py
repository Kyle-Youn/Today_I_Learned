import gzip
import io

def get_image_from_filesys(file_path):
  with open(file_path, 'rb') as f:
    retrun f.read()

data = get_image_from_filesys(file_path)
buffer = io.BytesIO()
with gzip.GzipFile(fileobj=buffer, mode='wb', compresslevel=9) as gz:
    gz.write(data)
buffer.seek(0)
