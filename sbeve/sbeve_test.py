#import unittest

from sbeve import Sbeve

reddit_part = ''#'sbeve'
outtake = 'shes wanting love and understanding again'#'he lied'
full = 'hes waluigi'#'she believed'

tests = [{'full':  'shes wanting love and understanding again',
  'outtake': 'hes waluigi',
  'reddit_part':''},
 {'full':  'she believed',
  'outtake': 'he lied',
  'reddit_part': 'sbeve'},
         {
             'full': 'be loving but a zen motherfucker',
             'outtake': 'blazo'
         }]

class Tests:
    def __init__(self, full, outtake, reddit_part):
        #self.full =
        pass

test = tests[2]

sbeve = Sbeve(test['full'], test['outtake'], drop_spaces=True)
print(sbeve.full)
print(sbeve.out)
print(sbeve.reddit_part)
print(str(sbeve))
sbeve.visualize(show=True)

#class Sbeve_Tester(unittest.TestCase):
#    pass