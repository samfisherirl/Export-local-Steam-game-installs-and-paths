import subprocess
import codecs
import os
import sys
import shutil
import json
import os.path
import library_paths as LP

appinfo = r'C:\Program Files (x86)\Steam\appcache\appinfo.vdf'


def moveV(directory):
    global appinfo
    try:
        shutil.copy2(appinfo, (os.path.join(directory, 'appinfo.vdf')))
        return True

    except:
        print(
            'file not found in \'C:\Program Files (x86)\Steam\appcache\appinfo.vdf\'\nTry placing it in the same directory as this application.\nIf you already have, ignore this error.')
    try:
        if os.path.exists(os.path.join(directory, 'appinfo.vdf')):
            print('\n\nFound it!')
            appinfo = os.path.join(directory, 'appinfo.vdf')
            return True
    except:
        return False


class Library:
    def __init__(self, exe, path, name, longpath):
        self.exe = str(exe)
        self.path = str(path)
        self.name = str(name)
        self.longpath = str(longpath)

    # exampled output times 3k 
    #  longpath: 'C:\\program files\\Steam\\common\\\\Half-Life\\hlds.exe'
    #   exe:  'hlds.exe'
    #   name: 'Half-Life Dedicated Server'
    #


def constructor(gameLib):
    # create library objects,
    # using a list to keep track
    lib = []
    x = 0
    for i in gameLib:
        lib.append(Library(i['exe'], i['path'], i['name'], 'xxxxx'))
    x = x + 1
    return lib


def callLibrary(lib):
    pathers = LP.main()
    print(str(pathers))
    print(lib[3].path + lib[3].exe)
    return pathers


def pathValidator(paths, lib):
    global matched
    matched = []
    for i in lib:
        for path in paths:
            struct = i.path  # + "\\" + i.exe
            post = i.path + "\\" + i.exe
            x = path + struct.replace('\\\\', '\\')
            if os.path.exists(x):
                i.longpath = x + "\\" + i.exe
                matched.append(i.longpath)
    print('finished')
    print(str(matched))
    return [lib, matched]
    # exampled output times 1k 
    #  path: 'C:\\program files\\Steam\\# It's a string.
    # common\\\\Half-Life\\hlds.exe'
    #   exe:  'hlds.exe'
    #   name: 'Half-Life Dedicated Server'
    #


# f'{VDFexe} {appinfo} --pretty >output.json'
def cmd4(directory):
    # Joining the directory and the VDFP.exe file.
    VDFexe = os.path.join(directory, 'VDFP.exe')
    out = os.path.join(directory, 'output.json')

    result = subprocess.run([VDFexe, appinfo, '-p'], capture_output=True)  # , "--pretty", ">output.json"
    # It's converting the output of the command to a string.
    val = str(result.stdout.strip(), encoding='utf-8')

    vals = json.loads(val)
    list = vals['datasets']
    return list


def parser(list):
    global gameLib
    gameLib = []
    game = {}
    # data format
    # list of games
    # games have attributes (dict)
    # this separates games, dupes and vals
    dot = '.'
    x = 0
    iterator = ['name', 'path', 'exe', 'longpath']

    for i in list:
        x = x + 1
        try:
            exe = i['data']['appinfo']['config']['launch']
        except:
            continue
        try:
            wd = i['data']['appinfo']['config']['installdir']
            wd.replace('/', '\\')
            name = i['data']['appinfo']['common']['name']
            name.replace('/', '\\')
        except:
            continue
        z = 0
        for i, z in enumerate(exe.items()):
            try:
                executable = exe[str(i)]['executable']
                executable = executable.replace('/', '\\')
            except:
                continue
            if ".exe" in executable:
                p = 'C:\\program files\\Steam\common\\'
                holder = [
                    wd,
                    name,
                    executable,
                    'xxxxxx'
                ]

                for t, y in zip(iterator, holder):
                    try:
                        # game.update({f"{i}": f"{y}" })
                        game.update({f'{t}': f'{y}'})
                        # writer(iterator, holder, x)
                    except:
                        break

                gameLib.append(game)
                # writer(iterator, holder, x)
                game = {}
            # exes = exe['0']['executable']
            # holder = [wd, name, i['executable']]
            else:
                continue
            dot = dot + '.'
    return gameLib

    def user():
        # ################################################
        # x = 0
        # for i in list:
        #     x = x + 1
        #     iterator = ['name', 'path', 'exe', 'longpath']
        #     try:
        #         exe = i['data']['appinfo']['config']['launch']
        #     except:
        #         continue
        #     try:
        #         wd =  i['data']['appinfo']['config']
        #         name = i['data']['appinfo']['common']['name']
        # ['executable']:
        #                 p = 'C:\\program files\\Steam\common\\'
        #                 batch = p + "\\" + wd['installdir'] + "\\" + exe[str(z)]['executable']
        #                 holder = [

        #                             ]

        #                 for t, y in zip(iterator, holder):
        #                     try:
        #                         #game.update({f"{i}": f"{y}" })
        #                         game.update({f'{t}': f'{y}'})
        #                         #writer(iterator, holder, x)
        #                     except:
        #                         break

        #                 gameLib.append(game)
        #                 #writer(iterator, holder, x)
        #                 z = z + 1
        #                 game = {}
        #         # exes = exe['0']['executable']
        #         # holder = [wd, name, i['executable']]
        #     except:
        #         print('matched on everything but there was an error on writer')
        # return gameLib
        pass


##########################################################
def writer1(iterator, holder, x):
    for i, y in (iterator, holder):
        try:
            # game.update({f"{i}": f"{y}" })
            game[f"{i}"] = f"{y}"
            gameLib.append(game)
        except:
            pass
    # try:
    #     y = 1
    #     for i in iterator:
    #         if iterator[y]:

    #             y = y + 1
    #             game[x].update({f'exe_{y}': f'{holder[y-1]}'})
    # except:
    #     print('')
    return game


def sendtoClass(lib):
    if not x:
        print(str(lib))
    else:
        pass
    # for i in array: 
    with open('out.txt', 'w', encoding='utf-8') as f:
        for i in array:
            f.write(str(i) + '\n')
    with open('out.csv', 'w', encoding='utf-8') as f:
        for i in array:
            f.write(str(i) + '\n')


def cmd5(directory):
    VDFexe = os.path.join(directory, 'VDFparse.exe')
    out = os.path.join(directory, 'output.json')

    result = subprocess.run([VDFexe, '-h'])  # , "--pretty", ">output.json"
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


# def writer(exe, dir):
#     log = cwd + '\\output.txt'
#     with open(log, 'w', encoding='utf-8') as f:
#         x = 0
#         for i, p in zip(exe, dir):
#             f.write(f'"{i}": {p},')
#             f.write('\n') 

def writer(lib, directory):
    log = os.path.join(directory, 'output.txt')
    csv = os.path.join(directory, 'output.csv')
    try:
        os.path.remove(log)
        os.path.remove(csv)
    except:
        print("")
    with open(log, 'w', encoding='utf-8') as f:
        with open(csv, 'w', encoding='utf-8') as g:
            f.write('here are your matched paths, next update includes name. ')
            x = 0
            for i in matched:
                f.write(i)
                f.write('\n')
                g.write(i)
                g.write('\n')
                # for key, val in i.items():
                #     g.write(("\n   " + key + ': ' + val + '\n'))
                #     g.write('\n')
                #     f.write((key + "\n" + val + "\n"))
                #     f.write('\n')


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
