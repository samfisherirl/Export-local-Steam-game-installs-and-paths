import os
import os.path
import regquery
import time


#################################################
# get steam paths from list of installs on reg
# combine in loop with appinfo
# return proper appinfo install path
################################################# 

class Dir:
    def dirname(self):
        directory = os.path.dirname(__file__)
        return directory

    def checker(appinfo):
        if not os.path.exists(appinfo):
            return os.path.join(appinfo, 'appinfo.vdf')
        else:
            return appinfo

    def loop_addys(path):

        pather = os.path.join(path, 'appcache\\appinfo.vdf')
        if os.path.exists(pather):
            return True, pather, path
        else:
            return False, pather, path


def powershell_find_steam():
    app = r"C:\Program Files (x86)\Steam\appcache\appinfo.vdf"
    if os.path.exists(app):
        return app, r"C:\Program Files (x86)\Steam"
    output = regquery.powershell_installs()
    list_of_steam_addys = regquery.parse_output(output)

    for i in list_of_steam_addys:
        try:
            i = i.replace("\\\\", "\\")
            ifexist = Dir.loop_addys(str(i.replace(r"\steam.exe", "")))
            if ifexist[0]:  # if exist
                appinfo = ifexist[1]
                steam = ifexist[2]  # path return
                return appinfo, steam
            else:
                continue
        except:
            continue


def main():
    global steam
    appinfo_locations = powershell_find_steam()

    class Steam:
        appinfo = appinfo_locations[0]
        path = appinfo_locations[1]

    return Steam
    # directory = Dir.dirname()
    # appinfo = Dir.checker(appinfo)


if __name__ == "__main__":
    try:
        print(str(main()))
        time.sleep(0.1)
    except:
        print('\n\nlocate steam error.\n\ncontinuing...\n\n')
