import numpy as np

def Cramer(mat):
    vals=[]
    A=np.linalg.det(np.delete(mat,n,1))
    for i in range(n):
        X=mat.copy()
        X[:,[i,n]]=X[:,[n,i]]
        X=np.linalg.det(np.delete(X,n,1))
        vals.append("x{}: {}".format(i+1,round(X/A,2)))
    return vals

n=int(input("Introduce el número de incógnitas: "))
l=list(map(float, input("Introduce los coeficientes en una sola línea separados por espacio (deben ser {} elementos): ".format(n*(n+1))).split()))

try:
    m=np.array(l).reshape(n,n+1)
    try:
        print(m)
        print(Cramer(m))
    except:
        print("No hay solucion")
except:
    print("Error al escribir")
