#!/usr/bin/python3

import requests
import sys
import re

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d=+' sys.argv[1]):

