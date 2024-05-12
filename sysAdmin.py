import os 
import subprocess
#os.system("ls")

subprocess.run(["ls","-l"])

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])