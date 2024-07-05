import subprocess
import os
import sys

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

# 获取EXE文件所在的路径
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

# 切换到EXE文件所在的路径
os.chdir(application_path)

# 定义要执行的命令
commands = [
    'hexo clean',
    'hexo generate',
    'hexo deploy'
]

# 在git bash中执行命令
for command in commands:
    run_command(f'D:\git\Git\bin\bash.exe -c "{command}"')

