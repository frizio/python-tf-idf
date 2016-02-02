# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:18:20 2016

@author: frizio
"""

from tfidfLib import *

table = TfIdf()
table.addDocument("foo", 
                  ["alpha", "bravo", "charlie", "delta", 
                   "echo", "foxtrot", "golf", "hotel"])
table.addDocument("bar", 
                  ["alpha", "bravo", "charlie", "india", "juliet", "kilo"])
table.addDocument("baz", 
                  ["kilo", "lima", "mike", "november"])
table.addDocument("caz", 
                  ["kilo", "kilo", "pene", "zolo"])


print(table.similarities (["alpha", "bravo", "charlie"]))
print(table.similarities (["alpha"]))