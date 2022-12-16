import subprocess
import codecs
import os
import sys
import shutil
import json

appinfo = r'C:\Program Files (x86)\Steam\appcache\appinfo.vdf'

def moveV(directory):
    shutil.copy2(appinfo, (os.path.join(directory, 'appinfo.vdf')))


# f'{VDFexe} {appinfo} --pretty >output.json'
def cmd4(directory):
# Joining the directory and the VDFP.exe file.
    VDFexe = os.path.join(directory, 'VDFP.exe')
    out = os.path.join(directory, 'output.json')
    
    result = subprocess.run([VDFexe, appinfo, '-p'], capture_output=True) # , "--pretty", ">output.json"
# It's converting the output of the command to a string.
    val = str(result.stdout.strip(), encoding='utf-8')

    vals = json.loads(val)
    list = vals['datasets']
    return list
    
def parse(list):
    array = []
    for i in list:
        try:
            array.append(i['data']['appinfo']['config']['launch']['0']) 
        except:
            continue

    with open('out.txt', 'w', encoding='utf-8') as f:
        for i in array: 
            f.write(str(i) + '\n') 


    
def cmd5(directory):
    VDFexe = os.path.join(directory, 'VDFparse.exe')
    out = os.path.join(directory, 'output.json')
    
    result = subprocess.run([VDFexe, '-h']) # , "--pretty", ">output.json"
    print()

def cmd3():
    base_args = list()
    VDFexe = r'C:\Users\dower\OneDrive\VDF_STEAM_PARSER\VDFparse.exe'
    print(VDFexe)
    base_args = ["VDFparse.exe"]
    appinfo = r'C:\Program Files (x86)\Steam\appcache\appinfo.vdf'
    output = '-h'
    base_args.extend([output])
    p = subprocess.Popen(' '.join(base_args),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    x = p.communicate()
    print(x)
    # 42maybe


def cmd():
    proc = subprocess.Popen([f'{VDFexe} {appinfo} --pretty >output.json'],
                            shell=True,
                            stdout=subprocess.PIPE)

    # proc = subprocess.Popen([VDFexe, ' appinfo > output.json'], stdout=subprocess.PIPE)
    return proc


# base_args = list()
# base_args.extend(["dotnet", "depot_downloader/DepotDownloader.dll"])
# p = subprocess.Popen(
#             ' '.join(args), creationflags=CREATE_NO_WINDOW,
#             shell=False,
#             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# p.read() maybe


def cmd2(val):
    VDFexe = cwd + '\\VDFparse.exe'
    appinfo = r'C:\Program Files (x86)\Steam\appcache\appinfo.vdf'
    proc = subprocess.Popen([VDFexe, 'query', appinfo, '*', val],
                            stdout=subprocess.PIPE)
    output = proc.stdout.read()
    return output


def clean(val):
    try:
        x = val.split()
        for i in x:
            print(i, '\n')
    except:
        pass
    return val


def parse(s, t):
    exe = []
    relative = []
    dir = []
    C = 'C:\\Program files (x86)\\Steam\\steamapps\\common\\'
    D = 'D\\Steam\\steamapps\\common\\'
    for i, p in zip(s.split('\n'), t.split('\n')):
        dir.append(str(C + i.replace('\r', '') + "\\" + p.replace('\r', '')))
        relative.append(str(i.replace('\r', '') + "\\" + p.replace('\r', '')))
    for i in t.split('\n'):
        i = i.replace('\r', '')
        if i:
            exe.append(i.replace('\r', ''))
    return [exe, dir]


def writer(exe, dir):
    log = cwd + '\\output.txt'
    with open(log, 'w', encoding='utf-8') as f:
        x = 0
        for i, p in zip(exe, dir):
            f.write(f'"{i}": {p},')
            f.write('\n')


# >>> s = b'your\nbyte\nstring'
# >>> s = s.decode()
# >>> s.split('\n')
# ['your', 'byte', 'string']
def main():
    x = cmd2("appid name executable installdir")
    z = (len(x))
    s = (x.decode('utf-8')).strip('\r\n')
    # .split('\n')
    # y = cmd2("executable")
    l = []
    l = parse(s, t)
    exe = l[0]
    dir = l[1]  # .split('\n')
    writer(exe, dir)



# run command line args