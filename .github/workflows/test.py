import os,subprocess


#Settings
TEST_DIR = "/tests"
CODE_FILE = "main.c"
COMPILER_TIMEOUT = 10.0
RUN_TIMEOUT = 10.0

code_path = os.path.join(TEST_DIR,CODE_FILE)
app_path = os.path.join(TEST_DIR,"app")

print("Building......")

#Compile the program
try:
    ret = subprocess.run(["gcc",code_path,"-o",app_path],
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE,
                         timeout = COMPILER_TIMEOUT
                         )
    

except Exception as e:
    print("ERROR:Compilation fail.",str(e))
    exit(1)


#Parse output
output = ret.stdout.decode('utf-8')
print(output)
output = ret.stderr.decode('utf-8')
print(output)

if ret.returncode != 0:
    print("Compilation fail. ")
    exit(1)

#Run the compile program
print("Running...")
try:
    ret = subprocess.run([app_path],stdout = subprocess.PIPE,timeout = RUN_TIMEOUT)

except Exception as e:
    print("ERROR:Run time fail.",str(e))
    exit(1)

#Parse output
output = ret.stdout.decode('utf-8')
print("Output:",output)
#All tests passed!
print("All test passed~~")
exit(0)