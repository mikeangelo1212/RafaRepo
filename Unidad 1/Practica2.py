#quitar los que son multiplo de 3
l= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
x=len(l)#metemos la longitud de la lista pa que no se pase
i=0
b=-1 #b de borrar ajajaja

while True:
    b=b+3
    l.pop(b)
    b=b-1
    i=i+1

    if x>=15:
        break
print(l)#ESTA NO JALA TODAVIA