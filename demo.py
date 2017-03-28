import pandas as pd
import numpy as np
import random
a = [[[1,"fruit","apple"],[1,"vegetable","potato"],[1,"drink","milk"]],
	 [[2,"electronic","computer"],[2,"laptop",'Mac'],[2,"cellphone","iphone"]],
	 [[3,"clothes","coat"],[3,"head","hat"]],
	 [[4,"body","arm"],[4,"eyes","glasses"],[4,"hand","finger"],[4,"foot","toe"]],
	 [[5,"building","library"],[5,"china","the great wall"],[5,"french","big bang"]]]
for i in range(len(a)):
	for j in range(len(a[i])):
		for item in random.sample(range(i) + range(i+1,len(a)),3):
			a[i][j].append(a[item][random.sample(range(len(a[item])),1)[0]][2])
print a