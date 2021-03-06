
# object methods
#!/usr/bin/python
# http://www.bagley.org/~doug/shootout/

import sys

#DEJAVU
'''
{
'NAME':"Object methods",
'DESC':"Object methods from computer language shootout",
'GROUP':'real-bench',
'CMPOUT':1,
'ARGS':"10000",
'BARGS':"230000"
}
'''


class Toggle:
    def __init__(self, start_state):
        self.bool = start_state
    def value(self):
        return(self.bool)
    def activate(self):
        self.bool = not self.bool
        return(self)

class NthToggle(Toggle):
    def __init__(self, start_state, max_counter):
        Toggle.__init__(self, start_state)
        self.count_max = max_counter
        self.counter = 0
    def activate(self):
        self.counter += 1
        if (self.counter >= self.count_max):
            self.bool = not self.bool
            self.counter = 0
        return(self)


def main():
    NUM = int(sys.argv[1])
    if NUM < 1:
        NUM = 1

    val = 1
    toggle = Toggle(val)
    for i in xrange(0,NUM):
        val = toggle.activate().value()
    if val:
        print "true"
    else:
        print "false"

    val = 1
    ntoggle = NthToggle(val, 3)
    for i in xrange(0,NUM):
        val = ntoggle.activate().value()
    if val:
        print "true"
    else:
        print "false"

main()