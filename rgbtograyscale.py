import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def greyscale(piksel):
    Y = (0.299*piksel[0]) + (0.587*piksel[1]) + (0.114*piksel[2]) #piksel[0] = R, [1] = G, [2] = B
    U = (piksel[2] - Y)*0.565
    V = (piksel[0] - Y)*0.713
    UV = U + V
    R1=piksel[0]*0.299
    R2=piksel[0]*0.587
    R3=piksel[0]*0.114
    G1=piksel[1]*0.299
    G2=piksel[1]*0.587
    G3=piksel[1]*0.114
    B1=piksel[2]*0.299
    B2=piksel[2]*0.587
    B3=piksel[2]*0.114
    R4=(R1+R2+R3)/3
    G4=(G1+G2+G3)/3
    B4=(B1+B2+B3)/3
    result =(R4+G4+B4+UV)/4
    return result
        

def convert(namafile):
    gambar = plt.imread(namafile)
    a = gambar.shape
    gmatrix = np.zeros((a[0],a[1])) #generate matriks 0 berukuran sama dengan piksel baris dan kolom gambar
    lengambar = len(gambar)
    for i in range(lengambar):
        for j in range(len(gambar[i])):
            gmatrix[i][j] = greyscale(gambar[i][j])

    plt.imshow(gmatrix, cmap = matplotlib.cm.Greys_r) #plotting matriks dengan colormaps
    plt.savefig('resultconv.png')
    plt.show()
   

nput = str(input('Masukkan nama file gambar yang akan dikonversi ke greyscale: '))
convert(nput)

                                      
    
    
