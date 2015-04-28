#!/usr/bin/python
import os
PTH = r"b:\pybtc\simpybitcointools\sbtc"
try:
    os.chdir(PTH)
    from sbtc import *
except:
    from bitcoin import *

if len(sys.argv) == 1:
    print "pybtctool <command> <arg1> <arg2> ..."
else:
    cmdargs, preargs, kwargs = [], [], {}
    i = 2
    # Process first arg tag
    if sys.argv[1] == '-s':
        preargs.extend(re.findall(r'\S\S*', sys.stdin.read()))
    elif sys.argv[1] == '-B':
        preargs.extend([sys.stdin.read()])
    elif sys.argv[1] == '-b':
        preargs.extend([sys.stdin.read()[:-1]])
    elif sys.argv[1] == '-j':
        preargs.extend([json.loads(sys.stdin.read())])
    elif sys.argv[1] == '-J':
        preargs.extend(json.loads(sys.stdin.read()))
    else:
        i = 1
    while i < len(sys.argv):
        if sys.argv[i][:2] == '--':
            kwargs[sys.argv[i][2:]] = sys.argv[i+1]
            i += 2
        else:
            cmdargs.append(sys.argv[i])
            i += 1
    cmd = cmdargs[0]
    args = preargs + cmdargs[1:]
    o = vars()[cmd](*args, **kwargs)
    if isinstance(o, (list, dict)):
        print json.dumps(o)
    else:
        print o
