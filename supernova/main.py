#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) DP Technology Development Team.

import argparse
import sys
import os
from supernova.motto.motto import verifyMotto
"""
Instructions
"""

__author__ = "Yuzhi Zhang, et al."
__copyright__ = "DP Technology Copyright 2020, 2021"
__status__ = "Development"

def main():
    parser = argparse.ArgumentParser(description="""
        `supernova` is a sample command for instructions.
        Type "supernova sub-command -h" for sub-command instructions.""")
    
    subparsers = parser.add_subparsers()
    
    parser_verifyMotto = subparsers.add_parser("verifyMotto", help='Verify if a setence is the motto of one person.')
    parser_verifyMotto.add_argument('-n',  dest='name', help='The name of person.')
    parser_verifyMotto.add_argument('-m', dest='motto',help='The motto you want to verify.')
    
    parser_verifyMotto.set_defaults(func=verifyMotto)
    
    args = parser.parse_args()
    try:
        getattr(args, "func")
    except AttributeError:
        parser.print_help()
        sys.exit(0)
    args.func(args)

if __name__ == "__main__":
    main()

