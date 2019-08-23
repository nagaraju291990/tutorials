"""#import argparse
from argparse import ArgumentParser

#parser = argparse.ArgumentParser(description="Argument parser working")
parser = ArgumentParser(description="Argument parser working")

parser.add_argument("-i","--input", dest="inp",help="first variable", required=True)
parser.add_argument("-o","--output", dest="out",help="second variable", required=True)

args = parser.parse_args()

input = args.inp
output = args.out

print(input)
print(output)
"""
from argparse import ArgumentParser
import re
import os
import sys
import pysrt

parser = ArgumentParser(description='Extract text from srt file \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=file.srt " + "-o=all"
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide .srt file name",required=True)
args = parser.parse_args()

inputfile = args.inputfile


print(inputfile)