import subprocess
from collections import deque

maxWorkers = 8
argList = [number for number in range(10,200,10)]
commonArgument = "option"
outputDir = "./results/"
commands = [f"python script1.py --arg1 {arg} --common_arg {commonArgument} --output_dir {outputDir}" for arg in argList]


if __name__ == '__main__':
   try:
      currentProcesses = deque()
      for command in commands:
         print("Starting another process")
         process = subprocess.Popen(command, shell=True)
         currentProcesses.append(process)
         if len(currentProcesses) == maxWorkers:
            print("waiting for resources...")
            if currentProcesses[0].poll() is None:
               currentProcesses[0].wait()
            else:
               print("freeing resources...")
               currentProcesses[0].kill()
               currentProcesses.popleft()
               continue
   finally:
      if process.poll() is None:
         process.wait()
      else:
         print("Killing last process")
         process.kill()
      print('done')