

import  random
import  numpy as np
import numpy.random as npr
import simpy
import time

landa=100
alpha=100
miu=100






users=100000


mohlatZamani_karha_deadline=[]
nerkh_serviceDehi_moshtari_schedular=[]
works=[]
nerkhArrivalTime=[]
zamane_residan=[]
shoroe_serviceDehi=[]
saf_schedular=[]
cores={ "cores1":[], "cores2":[], "cores3":[], "cores4":[], "cores5":[], "cores6":[], "cores7":[], "cores8":[],
        "cores9":[], "cores10":[], "cores11":[], "cores12":[], "cores13":[], "cores14":[], "cores15":[], }



line=input().split(",")

line1 = input().split(",")
cores["cores1"].append(float(line1[0]))
cores["cores2"].append(float(line1[1]))
cores["cores3"].append(float(line1[2]))

line2 = input().split(",")
cores["cores4"].append(float(line2[0]))
cores["cores5"].append(float(line2[1]))
cores["cores6"].append(float(line2[2]))

line3 = input().split(",")
cores["cores7"].append(float(line3[0]))
cores["cores8"].append(float(line3[1]))
cores["cores9"].append(float(line3[2]))

line4 = input().split(",")
cores["cores10"].append(float(line4[0]))
cores["cores11"].append(float(line4[1]))
cores["cores12"].append(float(line4[2]))

line5 = input().split(",")
cores["cores13"].append(float(line5[0]))
cores["cores14"].append(float(line5[1]))
cores["cores15"].append(float(line5[2]))


mohlatZamani_karha_deadline = list(npr.exponential(scale=1,size=(100000,(alpha))).sum(axis=1))
nerkh_serviceDehi_moshtari_schedular = list(np.random.poisson(1/miu, 100000))
# baraye nafar avval
nerkhArrivalTime.append(0)
for i in list( np.random.exponential( (1/landa) , 99999)):
    nerkhArrivalTime.append(i)




def find_kind_of_work(users):
    while users !=0:
        items = {1: 10, 2: 90}
        works.append(  (random.choice([k for k in items for dummy in range(items[k])]))   )
        # darkhastZadan( resorces)
        users -=1
find_kind_of_work(users)

numberOf1=works.count(1)
numberOf2=works.count(2)

def calc_zamane_residan(zamane_residan,nerkhArrivalTime,users):
    zamane_residan.append(0)
    ii=1
    while ii !=users:
        a=nerkhArrivalTime[ii]
        b=zamane_residan[ii-1]
        c=a+b
        zamane_residan.append(c)
        ii+=1
calc_zamane_residan(zamane_residan,nerkhArrivalTime,users)




def calc_shoroe_serviceDehi(shoroe_serviceDehi,nerkh_serviceDehi_moshtari_schedular,users):
    shoroe_serviceDehi.append(0)
    ii=1
    while ii !=users:
        a= shoroe_serviceDehi[ii-1] + nerkh_serviceDehi_moshtari_schedular[ii-1]
        b=zamane_residan[ii]
        m=max(a,b)
        shoroe_serviceDehi.append(m)
        ii+=1
calc_shoroe_serviceDehi(shoroe_serviceDehi,nerkh_serviceDehi_moshtari_schedular,users)




def calc_saf_schedular(saf_schedular,zamane_residan,shoroe_serviceDehi,users):
    ii=0
    while ii !=users:
        a=abs(zamane_residan[ii]-shoroe_serviceDehi[ii])
        saf_schedular.append(a)
        ii+=1
calc_saf_schedular(saf_schedular,zamane_residan,shoroe_serviceDehi,users)




all_indexes_work1=[]
countOfTime_one=0

if 1 in works:
    all_indexes_work1 = [a for a in range(len(works)) if works[a] == 1]
for i in all_indexes_work1:
    countOfTime_one += mohlatZamani_karha_deadline[i]



all_indexes_work2=[]
countOfTime_two=0

if 1 in works:
    all_indexes_work2 = [a for a in range(len(works)) if works[a] == 2]
for i in all_indexes_work2:
    countOfTime_two += mohlatZamani_karha_deadline[i]



safWork1=0
for i in all_indexes_work1:
    safWork1+=saf_schedular[i]

safWork2=0
for i in all_indexes_work2:
    safWork2+=saf_schedular[i]


kooleWork1=len(all_indexes_work1)
kooleWork2=len(all_indexes_work2)



# expired user in schedular
for i in range(len(mohlatZamani_karha_deadline)):

    a=mohlatZamani_karha_deadline[i]
    b=saf_schedular[i]
    if b > a:
        mohlatZamani_karha_deadline[i]=-11111
        nerkh_serviceDehi_moshtari_schedular[i]=-11111
        works[i]=-11111
        nerkhArrivalTime[i]=-11111
        zamane_residan[i]=-11111
        shoroe_serviceDehi[i]=-11111
        saf_schedular[i]=-11111


monghazi1=0
monghazi2=0

for i in all_indexes_work1:
    if works[i]==-11111:
        monghazi1+=1

for i in all_indexes_work2:
    if works[i]==-11111:
        monghazi2+=1


mohlatZamani_karha_deadline2=[]
works2=[]

def remove_expired_users(lastList , newList):
    for i in lastList:
        if i !=-11111 :
            newList.append(i)

remove_expired_users(mohlatZamani_karha_deadline , mohlatZamani_karha_deadline2)
remove_expired_users(works , works2)



for i in range(len(works2)):

    min_key, min_value = min(cores.items(), key=lambda x: len(set(x[1])))
    if 1 in works2:
        indexOf_one = works2.index(1)
        if min_value[0] <= mohlatZamani_karha_deadline2[indexOf_one] :
            cores[min_key].append(indexOf_one)
        else:
            cores[min_key].append(-11111)


    else:#hame karha =2
        indexOf_two = works2.index(2)
        if min_value==[]:

            min_value=0
            if min_value <= mohlatZamani_karha_deadline2[indexOf_two]:
                cores[min_key].append(indexOf_two)
            else:
                cores[min_key].append(-11111)

        else:
            if min_value[0] <= mohlatZamani_karha_deadline2[indexOf_two]:
                cores[min_key].append(indexOf_two)
            else:
                cores[min_key].append(-11111)



print("koole karhaye 1  ",end="")
print(kooleWork1)
print("koole karhaye 2  ",end="")
print(kooleWork2)
print()
# /////////////////////////////////////////////////////////////
print("koole zamane kare 1  " , end="")
print(countOfTime_one)

print("koole zamane kare 2  " , end="")
print(countOfTime_two)

print("miangin zamane kare 1  " , end="")
print(countOfTime_one/numberOf1)

print("miangin zamane kare 2  " , end="")
print(countOfTime_two/numberOf2)
print()
# /////////////////////////////////////////////////////////////

print("miangin zaman saf dar schedular kare 1 ", end="")
print(safWork1/numberOf1)

print("miangin zaman saf dar schedular kare 2 ", end="")
print(safWork2/numberOf2)
print()
# /////////////////////////////////////////////////////////////

print("nesbate karhaye1 ke expired shodan be kole kare 1 ", end="")
print((monghazi1/kooleWork1)*100)

print("nesbate karhaye2 ke expired shodan be kole kare 2  ", end="")
print((monghazi2/kooleWork2)*100)


print("nesbate karhaye1 ke expired shodan be kole kareha ", end="")
print((monghazi1/users)*100)

print("nesbate karhaye2 ke expired shodan be kole kareha ", end="")
print((monghazi2/users)*100)
print()

# /////////////////////////////////////////////////////////////
safCores=0
for i , j in cores.items():
    safCores+=len(j)-1
print("miangine toole saf servers ",end="")
print((safCores/15)*100)



