def bouble_short(list):
    n=len(list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(list[j]<list[j+1]):
                list[j],list[j+1]=list[j+1],list[j]
    return list
def my_frequency_with_dict(list):
    frequency_dict={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict
def my_mean(list):
    s,t=0,0
    for item in list:
        s=s+1
        t=t+item
    mean=t/s
    return mean
def my_median(list):
    list2=bouble_short(list)
    n=len(list2)
    if n%2==1:
        middle=int(n/2)+1
        median=list2[middle-1]
    else:
        middle1=int(n/2)-1
        middle2=(n/2)+1
        median=((middle1+middle2)/2)
    return median
with open("input_hw_2.csv","r") as dosya:
    liste = dosya.readlines()
    liste1=[]
    for i in range(len(liste)):
        s=0
        j=0
        while j<len(liste[i]):
            if(liste[i][j]=="-" and s==0):
                j=j+4
                s=1
            elif(liste[i][j]=="-" and s==1):
                x=liste[i][j+1]+liste[i][j+2]
                x=int(x)
                liste1.append(x)
                break
            else:
                j=j+1

frequancy=my_frequency_with_dict(liste1)
print(frequancy)#cevap
liste2=[]
for i in frequancy:
    liste2.append(frequancy[i])


ortalama =str(my_mean(liste2))
medyan=str(my_median(liste2))

dosya2 = open("output_dir_name.txt","a")
dosya2.write("Medyan "+medyan+"\n")
dosya2.write("Ortalama "+ortalama)

