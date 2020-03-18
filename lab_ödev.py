list =[]
list2=[]
my_d = dict()

def file_txt():
    with open("file.txt","w") as dosyalar:

        for i in range(1,11):
            a=str(i)
            file=open(a+".txt","r")
            for satir in file:
                dosyalar.write(satir)
            dosyalar.write("\n")
            file.close()

def my_h(list_1):

    my_d = dict()

    for i in list_1:

        if i in my_d:
            my_d[i] += 1

        else:
            my_d[i] = 1


    return my_d

def complist(list_1,height):
    list_2 =[]
    for i in range(0,len(list_1)-height+1):
        str =""

        for k in range(i, i + height):
            str2=list_1[k]

            str += str2
            str += ' '

        list_2.append(str)

    return list_2

def countstr(str):

    spacecount = 0

    for c in str:

        if c==' ':
            spacecount +=1

    return spacecount+1

def Maxhis(my_d,str):
    value =""
    maxnum = 0
    for k in my_d:
        num = int(my_d[k])
        index = k.find(str)

        if num > maxnum and index == 0:
            maxnum = num
            value = k


    return value

with open("input.txt","r") as dosyainput:
    with open("output.txt", "w") as dosyaoutput:
        for inputsatir in dosyainput:
            num = countstr(inputsatir)
            if inputsatir.endswith("\n"):
                inputsatir = inputsatir.replace("\n","")
            list2.clear()

            dosyalar = open("file.txt", "r")
            for satir in dosyalar:
                list.clear()
                for kelime in satir.split(" "):
                    list.append(kelime)
                if num <= 5:
                    list2.extend(complist(list, num+1))
            dosyalar.close()

            my_d = my_h(list2)

            if num <= 5:
                tahmin = Maxhis(my_d,inputsatir)
            else:
                tahmin = "5 kelimelik cümle giriniz"

            dosyaoutput.write(tahmin+"\n")

    print("Sonuclara output.txt dosyasından ulaşabilirsiniz")