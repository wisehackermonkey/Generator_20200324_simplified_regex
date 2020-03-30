#Simplified regex text generator 
#20200324
#by oran collins

# TODO fix phone number & imbeding
# command = "([1-9][A-Z][1-9])-([1-9][A-Z][1-9])"

import sys

from generator import generator


if __name__ == "__main__":
 
    if len(sys.argv) >=2:
        command  = sys.argv[1]

        gen = generator(command)

        result = gen.get()
        # print(sys.argv[-1])
        print(f"Result: {command} => {result}")
    else:
        print("no Args")
        print('please run something like > python Generator.py "\([1-9][A-Z][1-9]\)" ')
    
    


