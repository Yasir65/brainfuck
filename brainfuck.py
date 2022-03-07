#!/usr/bin/env python3

import os
import argparse

BRAINFUCK = [">", "<", "[", "]", ".", ",", "+", "-"]

parser = argparse.ArgumentParser()
parser.add_argument("-file", type=str, required=True)
parser.add_argument("-o", type=str, required=False)
args = parser.parse_args()

COMPILER = "gcc"

file = args.file

try:
    brainfuck_file = open(file, "r")
except:
    print("error: can't open " + file)

if args.o == None:
    outputfile = "output"
else:
    outputfile = args.o

code = brainfuck_file.read()
code = list(code)

print(code)

os.chdir("c")

brainfuck_file.close()

os.system("bash -c cat < _start.c > ../out.c")

for command in code:
    if command in BRAINFUCK:
        print("info: currently working on: " + command)
        
    if command == ">":
        os.system("bash -c cat < 5.c >> ../out.c")

    elif command == "<":
        os.system("bash -c cat < 6.c >> ../out.c")

    elif command == ".":
        os.system("bash -c cat < 3.c >> ../out.c")

    elif command == ",":
        os.system("bash -c cat < 4.c >> ../out.c")

    elif command == "+":
        os.system("bash -c cat < 1.c >> ../out.c")

    elif command == "-":
        os.system("bash -c cat < 2.c >> ../out.c")

    elif command == "[":
        os.system("bash -c cat < 7.c >> ../out.c")

    elif command == "]":
        os.system("bash -c cat < 8.c >> ../out.c")

os.system("bash -c cat < _end.c >> ../out.c")
os.system(f"gcc -w ../out.c -o ../{outputfile}")
os.remove("../out.c")