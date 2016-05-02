import os
import time
from os.path import isfile
import shutil
import filecopydb

now = time.time()
lastupdatefull = filecopydb.getLastUpdate()
lastupdate = lastupdatefull[2]

def createfilearray(sourcepath, filelist):
    filestocopy = []
    for textfile in filelist:
        if not isfile(textfile) and textfile.endswith('.txt'):
            stamp =  os.stat(sourcepath + '/' + textfile).st_mtime
            if stamp > lastupdate:
                filestocopy.append(textfile)
    return filestocopy

def copy(filearray, srcpath, destpath):
    for filename in filearray:
        src = srcpath +'/'+filename
        dest = destpath +'/'+filename
        shutil.copy2(src, dest)

def main():
    print (timesince)


if __name__ == "__main__": main()
