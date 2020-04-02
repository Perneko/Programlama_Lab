import random
def get_n_random_numbers(n,min,max):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers
def my_frequency_with_dict(list):
    frequency_dict={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict
def my_frequency_with_list_of_tuples(list):
    frequency_list=[]
    for i in range(len(list)):
        s=False
        for j in range(len(frequency_list)):
            if(list[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list[i],1])
    return frequency_list
def my_mode_with_dict(my_hist_d):
    frequency_max=-1
    mode=-1
    for key in my_hist_d.keys():
        if(my_hist_d[key]>frequency_max):
            frequency_max=my_hist_d[key]
            mode=key
    return mode,frequency_max
def my_mode_with_list(my_hist_list):
    frequency_max=-1
    mode=-1
    for item,frequency in my_hist_list:
        print(item,frequency)
        if frequency>frequency_max:
            frequency_max=frequency
            mode=item
    return mode,frequency_max

def my_lineer_search(list,item_search):
    found=(-1,-1)
    n=len(list)
    for indis in range(n) :
        if list[indis]==item_search:
            found=(list[indis],indis)
            #break,uncomment for last found
    return found
def my_mean(list):
    s,t=0,0
    for item in list:
        s=s+1
        t=t+item
    mean=t/s
    return mean
def bouble_short(list):
    n=len(list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(list[j]<list[j+1]):
                list[j],list[j+1]=list[j+1],list[j]
    return list

def my_binary_search(list,item_search):
    found=(-1,-1)
    low=0
    high=len(list)-1
    while(low<=high):
        mid = (low + high) //2
        if list[mid]== item_search:
            return list[mid],mid
        elif list[mid]>item_search:
            high=mid-1
        else:
            low=mid+1
    return found
def my_median(list):
    list2=bouble_short(list)
    n=len(list2)
    if n%2==1:
        middle=int(n/2)+1
        median=list2[middle]
    else:
        middle1=list2[int(n/2)]
        middle2=list2[int(n/2)+1]
        median=((middle1+middle2)/2)
    return median




list=get_n_random_numbers(5,-3,3)
print(list)
print(my_frequency_with_dict(list))
print(my_frequency_with_list_of_tuples(list))
print(my_mode_with_dict(my_frequency_with_dict(list)))
print(my_mode_with_list(my_frequency_with_list_of_tuples(list)))
print(my_lineer_search(list,0))
print(my_mean(list))
