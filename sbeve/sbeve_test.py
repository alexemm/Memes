#import unittest

from sbeve import Sbeve

reddit_part = 'sbeve'
outtake = 'he lied'
full = 'she believed'

sbeve = Sbeve(full, outtake)
print(sbeve.full)
print(sbeve.out)
print(str(sbeve))
sbeve.visualize()

#class Sbeve_Tester(unittest.TestCase):
#    pass