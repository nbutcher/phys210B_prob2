import numpy as np

eng = {'a':0.08167, 'b':0.01492, 'c':0.02782, 'd':0.04253, 'e':0.12702, 'f':0.02228, 'g':0.02015, 'h':0.06094, 'i':0.06966, 'j':0.00153, 'k':0.00772, 'l':0.04025, 'm':0.02406, 'n':0.06749, 'o':0.07507, 'p':0.01929, 'q':0.00095, 'r':0.05987, 's':0.06327, 't':0.09056, 'u':0.02758, 'v':0.00978, 'w':0.02360, 'x':0.00150, 'y':0.01974, 'z':0.00074}

fr = {'a':0.07636, 'b':0.00901, 'c':0.03260, 'd':0.03669, 'e':0.14715, 'f':0.01066, 'g':0.00866, 'h':0.00737, 'i':0.07529, 'j':0.00613, 'k':0.00049, 'l':0.05456, 'm':0.02968, 'n':0.07095, 'o':0.05796, 'p':0.02521, 'q':0.01362, 'r':0.06693, 's':0.07948, 't':0.07244, 'u':0.06311, 'v':0.01838, 'w':0.00074, 'x':0.00427, 'y':0.00128, 'z':0.00326}


#print eng['a'] + eng['b'] + eng['c'] + eng['d'] + eng['e'] + eng['f'] + eng['g']

#print eng['u'] + eng['v'] + eng['w'] + eng['x'] + eng['y'] + eng['z']

eproblist = []
for i in eng.values():
    eproblist.append(i)

eprob = np.array(eproblist)
eprob = np.sort(eprob)
print eprob

eletter = []
for i in eprob:
    for j in eng.keys():
        if (eng[j] == i):
            eletter.append(j)

print eletter

total = 0
for i in range(0,13):
    total += eprob[i]
print total

#for i in eng.keys():
#    print i
