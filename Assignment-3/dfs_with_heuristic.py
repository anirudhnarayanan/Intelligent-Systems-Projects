#!/usr/bin/env python

import random
from Node import Node
import pdb
from mapcolor import colormap
import time


colorlist = []


all_states = []
backtracks = 0

def pick_big_state(legal_colors):
    for k in sorted(legal_colors, key=lambda k: len(legal_colors[k]), reverse=True):
        #print k
        return k

def update_neighbors(statechanged,legal_colors,statedict,color_assigned,states):
    for state in statedict[statechanged]:
            #print(state)
            if color_assigned in list(filter(lambda x:x[0]==state,legal_colors))[0][1]:
                list(filter(lambda x:x[0]==state,legal_colors))[0][1].remove(color_assigned)


def init_colors(n):
    for i in range(n):
        colorlist.append(random.randint(0,255))

def random_color(n):
    return tuple(colorlist)

def build_color_graph(num,numstates,states):
    colors = random_color(3)
    a = Node(colors[0],states[0])
    root = a
    mystates = {}
    for i in range(1,numstates,1):
        w = Node(colors[0],states[i])
        a.put_child(w)
        a.nextnode = w
        #a = w
        mystates[states[i]] = a

        for j in range(1,num,1):
            b = Node(colors[j])
            a.put_child(b)

        #x.put_child(Node(colors[0],states[i]))
        a = w
            
    print(root)
    print(root.next)
    print(root.next[1].next)

def getcolors(states,mystatedict):
    listcol = []
    for i in states:
        listcol.append(mystatedict.get(i,""))

    return listcol

def gencols(states,i,numcolors,colors):
    tlist = []
    #colors = random_color(numcolors)
    for j in range(numcolors):
        tlist.append(Node(colors[j],states[i]))

    return tlist

def dfs_heuristic_included(mystatedict,statedict,numcolors,curstate,states,num,legal_colors):
    global backtracks
    #pdb.set_trace()
    #colormap(mystatedict)
    all_states.append(mystatedict.copy())
    for i in range(len(curstate.next)):
        temp_legal_colors = legal_colors.copy()
        mystatedict[curstate.next[0].myname] = curstate.next[i].mycolor   

        if mystatedict.get(curstate.next[0].myname) in getcolors(statedict[curstate.next[0].myname],mystatedict):
            #print("continued")
            continue

        #mystatedict[curstate.next[0].myname] = curstate.next[i].mycolor   
        if num == len(states) - 1:
            return 1,mystatedict

        
        backtracks +=1
        update_neighbors(curstate.next[0].myname,temp_legal_colors,statedict,curstate.next[i].mycolor,states)
        #big_statename = pick_big_state(legal_colors)
        
        temp_legal_colors = sorted(temp_legal_colors,key=lambda x:len(x[1]))



        #swap_ind = states.index(big_statename)

        #states[num+1],states[swap_ind] = states[swap_ind],states[num+1]


        temp_colorlist = colorlist.copy()
        #remove_colors = getcolors(temp_legal_colors[num+1][0],mystatedict)
        #temp_colorlist = temp_colorlist - remove_colors
        #temp_colorlist = [x for x in temp_colorlist if x not in remove_colors]
        curstate.next[i].next = gencols(states,num+1,numcolors,temp_colorlist)


        #mystatedict[curstate.next[i].next[0].myname] =   







        ans = dfs_heuristic_included(mystatedict,statedict,numcolors,curstate.next[i],states,num+1,temp_legal_colors)
        if ans[0] == 1:
            return 1,mystatedict

        continue

    return 0,mystatedict 


def init(states,statedict,numcolors):
    colors = colorlist
    root = Node(colors[0],states[0])
    for j in range(numcolors):
        root.put_child(Node(colors[j],states[0]))

    return root
    



        


            
            
    
    
if __name__ == "__main__":
    numcolors = 4
    init_colors(numcolors)

    colorlist = ["red","blue","green","black"]
    #states = ["a","b","c"]
    #statedict = {"a":["b"],"b":["a","c"],"c":["b"]}




    statedict = {
'Alabama':['Florida', 'Georgia', 'Mississippi', 'Tennessee'],
'Arizona':['California', 'Colorado', 'Nevada', 'New Mexico', 'Utah'],
'Arkansas' :['Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'],
'California':['Arizona', 'Nevada', 'Oregon'],
'Colorado':['Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'],
'Connecticut':['Massachusetts', 'New York', 'Rhode Island'],
'Delaware':['Maryland', 'New Jersey', 'Pennsylvania'],
'Florida':['Alabama', 'Georgia'],
'Georgia':['Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'],
'Idaho':['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
'Illinois':['Indiana','Iowa', 'Michigan', 'Kentucky', 'Missouri', 'Wisconsin'],
'Indiana':['Illinois', 'Kentucky', 'Michigan', 'Ohio'],
'Iowa': ['Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'],
'Kansas' :['Colorado', 'Missouri', 'Nebraska', 'Oklahoma'],
'Kentucky':['Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee', 'Virginia', 'West Virginia'],
'Louisiana':['Arkansas', 'Mississippi', 'Texas'],
'Maine':["New Hampshire"],
"Maryland":['Delaware','Pennsylvania','Virginia', 'West Virginia'],
'Massachusetts':['Connecticut', 'New Hampshire', 'New York', 'Rhode Island', 'Vermont'],
'Michigan':['Illinois', 'Indiana', 'Minnesota', 'Ohio', 'Wisconsin'],
'Minnesota':['Iowa', 'Michigan', 'North Dakota', 'South Dakota', 'Wisconsin'],
'Mississippi':['Alabama', 'Arkansas', 'Louisiana', 'Tennessee'],
'Missouri':['Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma', 'Tennessee'],
'Montana':['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
'Nebraska' :['Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'],
'Nevada':['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'],
'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
'New Jersey':["Delaware", "New York", "Pennsylvania"],
'New Mexico':['Arizona', 'Colorado', 'Oklahoma', 'Texas', 'Utah'],
'New York':['Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Rhode Island', 'Vermont'],
'North Carolina':['Georgia', 'South Carolina', 'Tennessee', 'Virginia'],
'North Dakota':['Minnesota', 'Montana', 'South Dakota'],
'Ohio':['Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'],
'Oklahoma' :['Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'],
'Oregon':["California", 'Idaho', 'Nevada', "Washington"],
'Pennsylvania':['Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'],
'Rhode Island':['Connecticut', 'Massachusetts', 'New York'],
'South Carolina':['Georgia', 'North Carolina'],
'South Dakota':['Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'],
'Tennessee':['Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'],
'Texas':['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'],
'Utah':['Arizona', 'Colorado', 'Idaho', 'Nevada', 'New Mexico', 'Wyoming'],
'Vermont':['Massachusetts', 'New Hampshire', 'New York'],
'Virginia':['Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'],
'Washington':['Idaho', 'Oregon'],
'West Virginia':['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'],
'Wisconsin':['Illinois', 'Iowa', 'Michigan', 'Minnesota'],
'Wyoming':['Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah']
}

    states = ['Alabama','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine',"Maryland",'Massachusetts',
        'Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon',
        'Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

    #states = ['North Dakota', 'North Carolina', 'Connecticut', 'Utah', 'Nebraska', 'New Jersey', 'South Carolina', 'Maine', 'Minnesota', 'Colorado', 'Kansas', 'Indiana', 'Florida', 'Tennessee', 'Idaho', 'New York', 'Michigan', 'Massachusetts', 'Oklahoma', 'New Hampshire', 'Ohio', 'Mississippi', 'Arizona', 'Montana', 'Pennsylvania', 'Virginia', 'Louisiana', 'Kentucky', 'Rhode Island', 'Alabama', 'South Dakota', 'Wyoming', 'New Mexico', 'Wisconsin', 'Missouri', 'Maryland', 'West Virginia', 'Illinois', 'Georgia', 'Vermont', 'Washington', 'California', 'Nevada', 'Texas', 'Iowa', 'Arkansas', 'Oregon', 'Delaware']

    #states = ['Maine', 'Minnesota', 'South Dakota', 'Illinois', 'Utah', 'Wyoming', 'Texas', 'Idaho', 'Wisconsin', 'Connecticut', 'Pennsylvania', 'Kansas', 'West Virginia', 'North Carolina', 'Colorado', 'California', 'Florida', 'Vermont', 'Virginia', 'North Dakota', 'Michigan', 'New Jersey', 'Nevada', 'Arkansas', 'Mississippi', 'Iowa', 'Kentucky', 'Maryland', 'Louisiana', 'Alabama', 'Oklahoma', 'New Mexico', 'Rhode Island', 'Massachusetts', 'South Carolina', 'Indiana', 'Delaware', 'Tennessee', 'Georgia', 'Arizona', 'Nebraska', 'Missouri', 'New Hampshire', 'Ohio', 'Oregon', 'Washington', 'Montana', 'New York']

    #states = ['Illinois', 'Oklahoma', 'California', 'Utah', 'Wyoming', 'Missouri', 'Michigan', 'Texas', 'Iowa', 'Delaware', 'Tennessee', 'Maryland', 'Kentucky', 'Montana', 'Minnesota', 'Connecticut', 'Louisiana', 'West Virginia', 'Pennsylvania', 'Nebraska', 'Kansas', 'Indiana', 'Rhode Island', 'Arizona', 'Florida', 'Massachusetts', 'South Dakota', 'Nevada', 'South Carolina', 'Ohio', 'New Hampshire', 'Idaho', 'Washington', 'Colorado', 'Oregon', 'New Jersey', 'Mississippi', 'Arkansas', 'Vermont', 'Wisconsin', 'Alabama', 'Georgia', 'Maine', 'New Mexico', 'North Carolina', 'New York', 'Virginia', 'North Dakota']

    states = ['Maine', 'Minnesota', 'South Dakota', 'Illinois', 'Utah', 'Wyoming', 'Texas', 'Idaho', 'Wisconsin', 'Connecticut', 'Pennsylvania', 'Kansas', 'West Virginia', 'North Carolina', 'Colorado', 'California', 'Florida', 'Vermont', 'Virginia', 'North Dakota', 'Michigan', 'New Jersey', 'Nevada', 'Arkansas', 'Mississippi', 'Iowa', 'Kentucky', 'Maryland', 'Louisiana', 'Alabama', 'Oklahoma', 'New Mexico', 'Rhode Island', 'Massachusetts', 'South Carolina', 'Indiana', 'Delaware', 'Tennessee', 'Georgia', 'Arizona', 'Nebraska', 'Missouri', 'New Hampshire', 'Ohio', 'Oregon', 'Washington', 'Montana', 'New York']




    legal_colors = []

    for state in states:
        legal_colors.append([state,colorlist.copy()])

    """
    
    states=['wa','nt','q','nsw','v','sa']

    statedict  ={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']}
    """
    
    mystatedict = {}
    #print(states[41])
    #random.shuffle(states)

    #print(states)
    root = init(states,statedict,numcolors)

    start_time = time.time()
    answer = dfs_heuristic_included(mystatedict,statedict,numcolors,root,states,0,legal_colors)

    end_time = time.time()
    count = 0 
    for key in answer[1]:
        count+=1
        if answer[1][key] in getcolors(statedict[key],mystatedict):
            print("oops")



    print(len(all_states))

    for i in range(0,len(all_states),200):
        colormap(all_states[i])


    colormap(mystatedict)
    time.sleep(10)
    print("VERIFIED ANSWER")
    print(answer)
    print("NUMBER OF BACKTRACKS: "+ str(backtracks))
    print("TIME OF EXECUTION: " + str(end_time - start_time) + "seconds") 

    

