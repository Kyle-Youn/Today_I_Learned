import zipfile

with zipfile.Zipfile(example_zip_buffer, "r") as zip_file:
  example_file_list = zip_file.namelist()
  print(file_list)
