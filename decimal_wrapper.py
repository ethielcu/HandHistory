#!/usr/bin/env python

try:
    import sys, cdecimal
    sys.modules['decimal'] = cdecimal
    from cdecimal import *
except ImportError:
    from decimal import *
