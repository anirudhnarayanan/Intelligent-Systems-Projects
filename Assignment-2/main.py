#!/usr/bin/env python

from new_sideways import sidewaysascent
from steepestascent import steepestascent

def randrestart(n,sideways = False):
    ans = 1
    numiters = 0
    total_iters = 0
    array_iters = []
    while(not ans == 0):
        #print(sideways)
        if sideways == True:
            ans,iters,board = sidewaysascent(n)
        else:
            print("calling steepest")
            ans,iters = steepestascent(n)

        total_iters +=iters
        array_iters.append(iters)

        numiters +=1

    #print(numiters)
    #print("my iters")
    #print(iters)
    #print(total_iters)
    #print(array_iters)
    return numiters,float(total_iters)


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
            mycount = 0
            printed = True
            for i in range(numruns):
                printme = True if i<4 else False 
                if i > 4 and printed:
                    print("please wait for finishing hill climbing")
                    printed = False
                mypass,iters = steepestascent(n,printme)
                success+= 1 if mypass == 0 else 0
                if mypass == 0:
                    success_counter +=iters
                else:
                    fail_counter += iters

            print("The success percentage is : "+ str(float(success)*100/float(numruns)))
            print("Failure Rate: " + str(100.0 - float(success)*100/float(numruns) ))

            if success == 0:
                print("Average iters in success: 0 (no success)")
            else:
                print("Average Iters in success : "+ str(float(success_counter)/float(success)))

            if numruns == success:
                print("Average Iterations in Failure: 0 (No failure)")
            else:
                print("Average Iters in failure : "+ str(float(fail_counter)/(float(numruns)- float(success))))
        

        if rrestart == 1:
            sum1 = 0
            total_iters =0
            for i in range(numruns):
                mysum,avgiters =randrestart(n)
                total_iters+=avgiters
                sum1+=mysum
            
            print(str(float(sum1)/float(numruns)) + " is the average number of restarts required")
            print(str(float(total_iters)/float(numruns)) + " is the average number of iterations required in each restarted attempt")



        
        

    elif type_run == 1:
        success = 0

        if rrestart == 0:
            success_counter = 0
            fail_counter = 0
            all_boards = []
            times = 4
            mytime=0
            printed = True
            for i in range(numruns):
                printme = True if mytime<4 else False
                mypass,iters,board = sidewaysascent(n,printme)
                if mytime > 4 and printed:
                    print("Please wait for hill climbing to finish")
                    printed = False
                mytime+=1
                all_boards.append(board)
                success+= 1 if mypass == 0 else 0
                if mypass == 0:
                    success_counter +=iters
                else:
                    fail_counter += iters
            print("The success percentage is : "+ str(float(success)*100/float(len(all_boards))))
            print("Failure Rate: " + str(100.0 - float(success)*100/float(numruns) ))
            if success == 0:
                print("Average iters in success: 0 (no success)")
            else:
                print("Average Iters in success : "+ str(float(success_counter)/float(success)))
            if len(all_boards) == success:
                print("Average Iterations in Failure: 0 (No failure)")
            else:
                print("Average Iters in failure : "+ str(float(fail_counter)/(len(all_boards)- success)))


        if rrestart == 1:
            sum1 = 0
            total_iters = 0
            for i in range(numruns):
                mysum,avgiters =randrestart(n,True)
                total_iters+=avgiters
                sum1+=mysum
            
            print(str(float(sum1)/float(numruns)) + " is the average number of restarts required")
            print(str(float(total_iters)/float(numruns)) + " is the average number of iterations required in each restarted attempt")
        
        


    



