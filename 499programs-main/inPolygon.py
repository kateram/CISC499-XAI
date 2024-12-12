import numpy as np

def contains(polyx,polyy,linex,liney):
    
    try:
        
        iter(polyx)
        iter(polyy)
    except TypeError:
        raise TypeError("polyx, polyy must be iterable")
    if len(polyx) != len(polyy):
        raise ValueError("polyx, poly must be of same size")
    if len(polyx) < 3:
        raise ValueError("polygon must consist of at least three points")

    
    single_val = True
    try:
        iter(linex)
    except TypeError:
        linex = np.asarray([linex],dtype=float)
    else:
        linex = np.asarray(linex,dtype=float)
        single_val = False

    try:
        iter(liney)
    except TypeError:
        liney = np.asarray([liney],dtype=float)
    else:
        liney = np.asarray(liney,dtype=float)
        single_val = False

    if linex.shape != liney.shape:
        raise ValueError("linex, liney must be of same shape")
    
    
    def lines():
        p0x = polyx[-1]
        p0y = polyy[-1]
        p0 = (p0x,p0y)
        for i,x in enumerate(polyx):
            y = polyy[i]
            p1 = (x,y)
            yield p0,p1
            p0 = p1

    mask = np.array([False for i in range(len(linex))])
    for i,x in enumerate(linex):
        y = liney[i]
        result = False

        for p0,p1 in lines():
            if ((p0[1] > y) != (p1[1] > y)) and (x < ((p1[0]-p0[0])*(y-p0[1])/(p1[1]-p0[1]) + p0[0])):
                result = not result 
        mask[i] = result

    
    if single_val:
        mask = mask[0]

    return mask


print(contains([375, 400, 450, 475, 450, 400],[150, 100, 100, 150, 200, 200], 380.0, 170.0))