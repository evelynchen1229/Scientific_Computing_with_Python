''' create a class called Hat '''
''' Hat should take argument about number of balls and their colours
but the number of colour are not fixed '''
'''Hat should have at least 1 ball '''

import random

class Hat():
    def __init__(self, **kwargs):
        content = []
        for key,value in kwargs.items():
            #setattr(self, key, value)
            self.key = key
            self.value = value
            content += [self.key] * self.value
        self.content = content

    def draw(self, num_balls):
        balls = []

        if num_balls >= len(self.content):
            return self.content

        while num_balls > 0:
            n = random.randint(0,(len(self.content)-1))
            balls.append(self.content.pop(n))
            num_balls -= 1
        self.content += balls
        return balls

def experiment(hat, expected_balls, num_balls, num_experiment):
    expected = 0
    num_exp = num_experiment
    while num_exp:
        result = hat.draw(num_balls)
        l = []
        for k,v in expected_balls.items():
            l.append(v <= result.count(k))

        if sum(l) == len(l):
            expected += 1
        num_exp -= 1
        
    return round(expected/num_experiment,2)

hat1 = Hat(yellow=1,red=3,blue=3)
probability = experiment(hat1,{'red':1,'blue':2},4,1000)
print(probability)






