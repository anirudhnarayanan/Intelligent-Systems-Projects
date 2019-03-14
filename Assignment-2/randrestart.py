#!/usr/bin/env python

from new_sideways import sidewaysascent
from steepestascent import steepestascent

def randrestart(n,sideways = False):
    ans = 1
    numiters = 0
    total_iters = 0
    while(not ans == 0):
        print(sideways)
        if sideways == True:
            ans,iters = sidewaysascent(n)
        else:
            print("calling steepest")
            ans,iters = steepestascent(n)

        total_iters +=iters

        numiters +=1

    print(numiters)
    return numiters,float(total_iters)/float(numiters)


if __name__ == "__main__":
    import sys
    args = {1:"How many queens: ",2: "How many new random generated algorithms do you want it to run: ",3:"Steepest Ascent(0) or Sideways(1): ",4: "Include Random Restart(0 for no, 1 for yes) ? "}
    input_args = []
    for i in range(1,5,1):
        input_args.append(int(input(args[i])))

    n = input_args[0]
    numruns = input_args[1]
    type_run = input_args[2]
    rrestart = input_args[3]


    if type_run == 0:
        success = 0
        if rrestart == 0:
            success_counter = 0
            fail_counter = 0
            for i in range(numruns):
                mypass,iters = steepestascent(n)
                success+= 1 if mypass == 0 else 0
                if mypass == 0:
                    success_counter +=iters
                else:
                    fail_counter += iters

            print("The success percentage is : "+ str(float(success)*100/float(numruns)))
            print("Average Iters in success : "+ str(float(success_counter)/float(numruns)))
            print("Average Iters in failure : "+ str(float(fail_counter)/float(numruns)))
        

        if rrestart == 1:
            sum1 = 0
            for i in range(numruns):
                mysum,avgiters =randrestart(n)
                sum1+=mysum
            
            print(str(float(sum1)/float(numruns)) + " is the average number of restarts required")
            print(str(avgiters) + " is the average number of iterations required in each restarted attempt")



        
        

    elif type_run == 1:
        success = 0

        if rrestart == 0:
            for i in range(numruns):
                mypass,iters = sidewaysascent(n)
                success+= 1 if mypass == 0 else 0
                if mypass == 0:
                    success_counter +=iters
                else:
                    fail_counter += iters
            
            print(str(float(sum1)/float(numruns)) + " is the average number of restarts required")
            print("Average Iters in success : "+ str(float(success_counter)/float(numruns)))
            print("Average Iters in failure : "+ str(float(fail_counter)/float(numruns)))


        if rrestart == 1:
            sum1 = 0
            for i in range(numruns):
                mysum,avgiters =randrestart(n,True)
                sum1+=mysum

            print(str(float(sum1)/float(numruns)) + " is the average number of restarts required")
            print(str(avgiters) + " is the average number of iterations required in each restarted attempt")
        
        


    



