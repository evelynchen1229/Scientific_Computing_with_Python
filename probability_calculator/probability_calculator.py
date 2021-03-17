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
     #   print(content)
        self.content = content

    def draw(self, num_balls):
        balls = []

        if num_balls >= len(self.content):
            return self.content

        while num_balls > 0:
            n = random.randint(0,(len(self.content)-1))
            #print(n)
            balls.append(self.content.pop(n))
            #print(balls)
            num_balls -= 1
        #    print(num_balls)

        self.content += balls
        return balls





# print(hat1.draw(4))
#ball = hat1.draw(4)
#print(ball)
#print(ball.count('red'))

def experiment(hat, expected_balls, num_balls, num_experiment):
    expected = 0
    num_exp = num_experiment
#    print(num_exp)
    while num_exp:
 #       print(hat)
        result = hat.draw(num_balls)
  #      print(result)
        l = []
        for k,v in expected_balls.items():
   #         print(k,v)
            l.append(v <= result.count(k))
    #        print(l)
        #for i in range (0,len(expected_balls)):
         #   ball = expected_balls.keys()
          #  num = expected_balls.values()
           # print(ball,num)
            #l.append(
            #print(expected_balls[expected_balls[i]] >= result.count(expected[i]))

        if sum(l) == len(l):
            expected += 1
        num_exp -= 1
     #   print(expected,num_exp)

    return round(expected/num_experiment,2)

hat1 = Hat(yellow=1,red=3,blue=3)
probability = experiment(hat1,{'red':1,'blue':2},4,1000)
print(probability)






