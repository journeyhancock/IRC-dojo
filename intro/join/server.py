#!/opt/pwn.college/python

import subprocess

command = ["/challenge/ircserver/miniircd", "--listen", "127.0.0.1", "--ports", "8080", "--motd", "/flag"]

subprocess.run(command, text=True);