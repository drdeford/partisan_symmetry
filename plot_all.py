import matplotlib.pyplot as plt
from partisan_symmetry_noplot import partisan_symmetry
for k in range(1,100):
    a=[]
    for i in range(1,100):
        a.append([])
        for j in range(1,100):
            a[i-1].append(partisan_symmetry([5*i/100,.20,5*j/100],1000,False))

    plt.imshow(a)
    plt.colorbar()
    plt.xticks(range(99),[x/20 for x in range(1,100)])
    plt.yticks(range(99),[x/20 for x in range(1,100)])
    plt.title("Partisan Symmetry Difference for (x,"+str(k)+",y)")
    plt.savefig("./ps"+str(k)+".png")
    plt.close()
    print("figure",k,"done")
    
