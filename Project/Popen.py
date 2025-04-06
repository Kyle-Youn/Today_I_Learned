import subprocess

# 새 프로세스에서 'ls' 명령어 실행
process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)

output, error = process.communicate()

if output:
  print(output.decode('UTF-8'))
if error:
  print(error.decode('UTF-8'))
