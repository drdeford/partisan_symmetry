# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:09:41 2018

@author: daryl
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

def partisan_symmetry(pvec,n=200,plots=False):
    
    l=len(pvec)
    pvec = np.array(sorted(pvec))
    seats = []
    votes = []
    small = pvec[0]
    large = pvec[-1]
    
    gap = large - small
    
    
    
    mean = np.mean(pvec)
    
    lvec = pvec - mean*np.ones([1,l])
    
    
    
    for t in range(n):
        tvec = lvec + (t/n)*np.ones([1,l])
        #print(tvec)
        votes.append(np.mean(tvec))
        seats.append(sum(sum(tvec>=.5))/l)
        
   # print(votes)
    #print(seats)
    
    bn = np.array([mean+ (.5-x) for x in pvec])
    
    
    cn=[str(round(float(bn), 3)) for bn in bn]
    bvotes=[]
    bseats=[]
    
    for t in range(n):
        bvotes.append(t/n)
        bseats.append(sum(bn<(t/n))/l)
        
#    plt.figure()
#    plt.plot([.5],[.5],'ro', markersize=15)
#    plt.plot([mean],[sum(pvec>=.5)/l],'g*', markersize=20)
#
#    plt.plot(votes,seats)
#    plt.xlabel("Vote %")
#    plt.ylabel("Seat %")
#    plt.title("Seats -- Votes")
#     ys=[x/l for x in range(l+1)]
#    zs=[str(round(float(ys), 3)) for ys in ys]
#    plt.yticks(ys,zs)

#    plt.xticks(bn,cn, rotation=45)
#
#    plt.show()
#    
    
    bn = np.array([mean+ (.5-x) for x in pvec])
    
    bvotes=[]
    bseats=[]
    
    for t in range(n):
        bvotes.append(t/n)
        bseats.append(sum(bn<(t/n))/l)
        
    dn=list(bn[:])
    for x in bn:
        dn.append(1-x)
        
    rseats=list(reversed(seats))

            
    en=[str(round(float(dn), 3)) for dn in dn]
    area=0
    for t in range(n):
        area += (1/n)*abs(seats[t]-(1-rseats[t])) 


    if plots:
        
#       plt.figure()
#       plt.plot([.5],[.5],'ro', markersize=15)
#       plt.plot([mean],[sum(pvec>=.5)/l],'g*', markersize=20)
#
#       plt.plot(votes,seats)
#       plt.xlabel("Vote %")
#       plt.ylabel("Seat %")
#       plt.title("Seats -- Votes")
#       ys=[x/l for x in range(l+1)]
#       zs=[str(round(float(ys), 3)) for ys in ys]
#       plt.yticks(ys,zs)    
#       plt.xticks(bn,cn, rotation=45)
#
#       plt.show()
#    

        plt.figure()    
        plt.plot([.5],[.5],'ro', markersize=10)
        plt.plot([mean],[sum(pvec>=.5)/l],'g*', markersize=20)
    
        plt.plot(bvotes,bseats)
        plt.xlabel("Vote %")
        plt.ylabel("Seat %")
        plt.xticks(bn,cn, rotation=45)
        ys=[x/l for x in range(l+1)]
        zs=[str(round(float(ys), 3)) for ys in ys]
        plt.yticks(ys,zs)
    
        plt.title("Seats -- Votes")
        
        plt.show()
        
        
        fig, ax = plt.subplots(1)    
        
        rseats=list(reversed(seats))
    
        
        errorboxes = []
    
        # Loop over data points; create box from errors at each point
        #area = 0
        for t in range(n):
            #if 1-rseats(i)
            rect = Rectangle((t/n, min(seats[t],1-rseats[t])), 1/n,abs(seats[t]-(1-rseats[t])))
            errorboxes.append(rect)
            
    
        # Create patch collection with specified colour/alpha
        pc = PatchCollection(errorboxes, facecolor='gray', edgecolor=None)
    
        # Add collection to axes
        ax.add_collection(pc)
        plt.plot([.5],[.5],'ro', markersize=10)
        plt.plot(votes,seats,'b',label='Original')
        
        
        plt.plot(votes,[1-x for x in rseats],'y',label="Flipped")
        
        
        
        plt.legend()    
        plt.xlabel("Vote %")
        plt.ylabel("Seat %")
        
        #dn=list(bn[:])
        #for x in bn:
        #    dn.append(1-x)
        #    
        #en=[str(round(float(dn), 3)) for dn in dn]
    
        
        plt.xticks(dn,en, rotation=45)
        ys=[x/l for x in range(l+1)]
        zs=[str(round(float(ys), 3)) for ys in ys]
        plt.yticks(ys,zs)
        plt.title("Seats -- Votes: Symmetry Gaps")
    
	plt.show()    

    

        
    
    mvec = pvec + (.5-np.median(pvec))*np.ones([1,l])
    mm = np.mean(mvec) - .5
    mvec = pvec - mean*np.ones([1,l]) + .5*np.ones([1,l])
    pb = .5 - sum(sum(mvec >= .5))/l
    eg = 2*np.mean(pvec) - sum(pvec>=.5)/l - .5
    ps = 0
    for t in range(int(n/2)):
        ps += abs(seats[t] - (1-seats[-(t+1)]))
        
    ps = 2*ps/n
        
        
    
    print("Mean-Median:", mm)
    print("Partisan Bias:", pb)
    print("Efficiency Gap:", eg)
    print("Partisan (a)Symmetry:", ps)
    
    
    bmm = np.median([.5-x for x in bn])
    mvec = pvec - mean*np.ones([1,l]) + .5*np.ones([1,l])
    
    bpb = .5 - bseats[int(n/2)]
    
    beg = 2*np.mean(pvec) - sum(pvec>=.5)/l - .5
    
    
    #this one needs to be reformulated!
    bps = 0
    for t in range(int(n/2)):
        bps += abs(seats[t] - (1-seats[-(t+1)]))
        
    bps = 2*bps/n
        
        
    
    print("2Mean-Median:", bmm)
    print("2Partisan Bias:", bpb)
    print("2Efficiency Gap:", beg)
    print("2Partisan (a)Symmetry:", bps)
    print("Rectangle Area:", area)
    
    print(cn,sorted(en))
    print(mean)

    
#Add plots with B_n endpoints need to keep track of
#both the value and the index to set the y-values
#Draw gray rectangles all the way along showing plus and minus

#Replace the Mean--Median measurement from partisan.pdf
    #Also add the partisan-bias functional version
    #Also direct efficiency gap copmutation. 
    #Also direct efficiency
    
#
    
partisan_symmetry([.1,.2,.3,.4,.41,.42,.43,.44,.45,.46,.6],10000,False)

        
#partisan_symmetry([.283, .283, .288, .288, .38, .384, .497, .51, .51],1000)
        
        


        
