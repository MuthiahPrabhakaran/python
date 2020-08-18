# -*- coding: utf-8 -*-
"""
When we run this file alone, if will be true
"""

def func():
    print("func in main1.py")
    return

print("Top level in main1.py")

if __name__ == "__main__":
    print("main1.py is the main file")
else:
    print("main1.py is imported into another file")
    
"""
Result:
    Top level in main1.py
    main1.py is the main file
"""