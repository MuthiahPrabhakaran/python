# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:03:54 2020

@author: Dallps
"""
import main1

print("Top level in main2.py")
main1.func()


if __name__ == "__main__":
    print("main2.py is the main file")
else:
    print("main2.py is imported into another file")
    

"""
Result:
    
    Top level in main1.py
    main1.py is imported into another file
    Top level in main2.py
    func in main1.py
    main2.py is the main file
    
"""