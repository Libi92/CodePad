import os
import subprocess


def runProcess(exe):
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    result = []
    while(True):
        retcode = p.poll()
        result.append(p.stdout.readline())
        if(retcode is not None):
            break
    result = removeall(result, '')
    print(os.getcwd())
    print(result)
    return result


def removeall(list, item):
    return filter(lambda a: a != item, list)


# print(os.getcwd())
# ouput = runProcess(["javac", "../code/HelloWorld.java"])
# print(len(ouput), ouput)
#
# ouput = runProcess(["java", "-cp", "../code/", "HelloWorld"])
# print(len(ouput),ouput)