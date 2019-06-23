
def scat(x,y,filename,lx,ly,color="black", s=0.9):
    print("creating plot: {}".format(filename))
    fig = plt.figure(figsize=(18,8))
    plt.scatter(x,y, s=s, color=color)#, cmap=cmap)
    plt.xlabel(lx,fontsize=23)
    plt.ylabel(ly,fontsize=23)
    plt.savefig("data/{}.png".format(filename))
    plt.clf()

def hist1d(x,filename,lx,ly,bins=90):
    print("creating plot: {}".format(filename))
    fig = plt.figure(figsize=(18,8))
    plt.hist(x, bins=bins, histtype="step")#, cmap=cmap)
    plt.xlabel(lx,fontsize=23)
    plt.ylabel(ly,fontsize=23)
    plt.savefig("data/{}.png".format(filename))
    plt.clf()

def hist(x,y,filename,lx,ly,bins=[181,100],cmap="gist_heat_r"):
    global suf
    plt.rcParams.update({"font.size":20})
    print("creating plot: {}".format(filename))
    fig = plt.figure(figsize=(18,8))
    plt.hist2d(x,y, bins=bins, cmap=cmap)
    plt.xlabel(lx,fontsize=23)
    plt.ylabel(ly,fontsize=23)
    plt.colorbar()
    plt.savefig("data/{}{}.png".format(filename,suf))
    plt.clf()
