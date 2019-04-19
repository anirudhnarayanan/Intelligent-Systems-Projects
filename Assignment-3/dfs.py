#!/usr/bin/env python

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def build_color_graph(num,numstates,states):
    colors = random_color()
    a = Node(colors[0],states[0])
    mystates = {}
    for i in range(1,numstates,1):
        w = Node(colors[0],states[i])
        a.put_child(w)
        #a = w
        mystates[states[i]] = a

        for j in range(1,num,1):
            b = Node(colors[j])
            a.put_child(b)

        #x.put_child(Node(colors[0],states[i]))
        a = w
            
            
            
    
    

