# -*- coding:utf-8 -*-
from builtins import range
def hab(n):
    return (n*n+1)//2
print(hab(100))

hab=0;
for n in range(1,11,1):
    hab+=n*n;
print(hab)

def hab2(nn):
    return nn*((nn+1)*(2*nn+1))//6;
print(hab2(10))


#주어진 숫자 n개중에 가장 큰 숫자 찾기
#17 , 92,18,33,58,7,33,42
        
a=[17,92,18,33,58,7,33,42]
b=0;

for aa in range (0,len(a)):
    if(b<a[aa]):
        b=a[aa]
print(b)


#계산복잡도 고려
#리스트에 숫자 n개 있을때 가장 큰 값 있는 위치 번호를 돌려주는 알고리즘
a=[1,2,3,4,16,22,666,221]
n = len(a)
b=0
for i in range(0,n):
    if(a[b]<a[i]):
        b=i;
print(b)

#계산복잡도 고려
#리스트에 숫자 n개 있을때 가장 큰 값 있는 위치 번호를 돌려주는 알고리즘
def find_max_idx(a):
    n=len(a)
    max_idx=0
    for i in range(0,n):
        if a[i]>a[max_idx]:
            max_idx=i
    return max_idx
    
print(find_max_idx(a))
#최솟값 구하는 알고리즘
aa=[1,2,3,4,5,6,7,8,0,2]
def find_min(aa):
    n=len(aa)
    b=0;
    for i in range(0,n):
        if(aa[i]<b):
            b=aa[i]
    return b;
print(find_min(aa))

#동명이인 찾기 알고리즘
name=["TOM","MIKE","APPLE","TOM"]
same=set()
for i in range(0,len(name)-1):
    for j in range(i+1,len(name)):
        if(name[i]==name[j]):
            same.add(name[i]);
print(same)

def find_same_name(name):
    n=len(name)
    result=set()
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(name[i]==name[j]):
                result.add(name[i])
    return result
print(find_same_name(name));

#위의 알고리즘은 
#반복문이 2개 들어갔기에 O(n제곱)으로 표기하고
#n의값이 증가함에 따라 엄청난 시간속도가 늘어남


#n명중 두명을뽑아 짝을 짓는다 짝을 지을수있는 모든 조합수를 출력
#ex:리스트 ["톰","기린","사과","뷰"]
a=["a","b","c","d"]
def zohab(a):
    n=len(a);
    for i in range(0,n-1):
        for j in range(i+1,n):
            print(a[i],"-",a[j])
    
zohab(a)


65536 #O(l)
n-1 #O(n)
#3분의 2n제곱 +10000n O(n제곱)
#3n4제곱 -4엔3제곱 +5 n제곱 -6n O(n4제곱)

#펙토리얼
def fact(n):
    f=1
    for i in range(1,n+1):
        f=i*f
        print(f)
    return f

print(fact(5))

#재귀호출 함수안에 함수가 있어 계속 무한루프도는    
# def hello():
#     print("hello")
#     hello()
#     
# hello()

#재귀호출 알고리즘
#n!=n*(n-1)!
def fact2(n):
    if n<=1:
        return 1;
    return n*(fact(n-1));
print(fact2(5))

#1부터 n까지의 합 구하기를 재귀호출로 만들어보기
def habguhagi(n):
    if n==0:
        return 0;
    return n+habguhagi(n-1)
print(habguhagi(5))

#숫자 n개중에서 최댓값 찾기 재귀호출로
a=[1,2,3,4,16,22,666,221]
def find_maxzaegy(a,n):
    if(n==1):
        return a[0]
    max_n=find_maxzaegy(a, n-1);
    if(max_n>a[n-1]):
        return max_n
    else:
        return a[n-1]

print(find_maxzaegy(a, len(a)))

#최대공약수
def gcd(a,b):
    i=min(a, b);#두 수중에서 최소값 구하는 함수
    while True:
        if a%i==0 and b%i==0:
            return i
        i=i-1
print(gcd(10, 15))

#유클리드 알고리즘을 활용 최대공약수 구하는걸 재귀로 써보자
def gcd2(a,b):
    if b==0:
        return a;
    return gcd2(b, b%a)
print(gcd2(20, 15))

#0과 1부터 시작해서 바로 앞의 두 수를 더한값을 피보나치 수열
#0+1=1 1+1=2 1+2=3
def fibo(n):
    if(n<=1):
        return n;
    return fibo(n-1) + fibo(n-2)

print(fibo(7))

#하노이의 탑 알고리즘
#입력: 옮기는 원반 개수
#출력: 옮기는 원반 순서
#from_pos시작
#to_pos 도착
#aux_pos:보조기둥
def hanoi(n,from_pos,to_pos,aux_pos):
    if n==1:
        print(from_pos,"->",to_pos);
        return;
    #원반 n-1개를 aux_pos로 이동
    hanoi(n-1, from_pos, aux_pos, to_pos)
    #가장 큰 원반 이동
    print(from_pos,"->",to_pos)
    #보조에 있는 원반을 목적지로 이동
    hanoi(n-1, aux_pos, to_pos, from_pos)
print("n==1")
hanoi(1, 1, 3, 2)
print("n==2")
hanoi(2, 1, 3, 2)
print("n==3")
hanoi(3, 1, 3, 2)
#하노이의 탑은 O(2엔승)관계를 갖는다

    
#순차 탐색 알고리즘
#x의 값이 a리스트 안에 몇번째에 있는지
#없으면 -1반환
a=[1,2,3,4,5,6,10]
def search_list(a,x):
    n=len(a)
    for i in range(1,n):
        if(x==a[i]):
            return i
    return -1
print(search_list(a, 10))


#조금 더 효율적이게    
def selection_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                #파이썬의 강점 위치 바꾸기
                a[min_idx], a[j] = a[j], a[min_idx]

a = [10, 20, 30, 40, 1, 2, 3, 4]
print(a)


#선택 정렬 알고리즘
def selection_sort2(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(a[i]>a[j]):
                a[i],a[j]=a[j],a[i]
                
a=[1,5,112,435,12,1,0,23]
selection_sort2(a)
print(a)                

#큰수 -> 작은수
def selection_reverse_sort(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(a[i]<a[j]):
                a[i],a[j]=a[j],a[i]
a=[1,5,112,435,12,1,0,23] 
selection_reverse_sort(a)
print(a)

#삽입정렬
def find_insert_index(sorted_list, value):
    for i in range(len(sorted_list)):
        if value < sorted_list[i]:
            return i
    return len(sorted_list)

def insertion_sort(input_list):
    result = []
    while input_list:
        value = input_list.pop(0)
        index = find_insert_index(result, value)
        result.insert(index, value)
    return result
print(insertion_sort(a))

def ins_sort(a):
    n=len(a)
    for i in range(0,n):
        key=a[i]
        j=i-1
        while j >=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key


def find_insert_index2(sorted_list, value):
    for i in range(len(sorted_list)):
        if value < sorted_list[i]:
            return i
    return len(sorted_list)

def insertion_sort2(input_list):
    result = []
    while input_list:
        value = input_list.pop(0)
        index = find_insert_index2(result, value)
        result.insert(index, value)
    return result
a=[1,2,3,4,5,6,7,8,11,2142,2121,0,1,2,3]
print(insertion_sort2(a))


#퀵 정렬
def quick_sort(a):
    n=len(a)
    if n<=1:
        return a
    pivot=a[-1]
    g1=[]
    g2=[]
    for i in range(0,n-1):
        if a[i]<pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
    return quick_sort(g1)+[pivot]+quick_sort(g2)
a=[1,2,321,123,555,123,2,0]
print(quick_sort(a)) 

def quick_sort_sub(a,start,end):
    if end - start<=0:
        return
    
    pivot = a[end]
    i=start
    for j in range(start,end):
        if a[j]<=pivot:
            a[i],a[j]=a[j],a[i]
            i+=1
    a[i],a[end]=a[end],a[i]
    quick_sort_sub(a, start, i-1)
    quick_sort_sub(a, i+1, end)
    
def quick_sort2(a):
    quick_sort_sub(a, 0, len(a)-1)
a=[1,2,321,123,555,123,2,0]
quick_sort2(a)
print(a)
#a.sort()라는 함수를 쓰면 그냥 정렬됌

    
#이분탐색 시간복잡도는 O(log n)
def binart_search(a,x):
    start=0
    end=len(a)-1
    while start<=end:
        mid=(start+end)//2
        if x == a[mid]:
            return mid
        elif x> a[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1

print(binart_search(a, 321))

#이분탐색을 재귀함수로
def binart_search_sub(a,x,start,end):
    if start>end:
        return -1
    
    mid=(start+end)//2
    if x==a[mid]:
        return mid
    
    elif x<a[mid]:
        return binart_search_sub(a, x, start, mid-1)
    else:
        return binart_search_sub(a, x, mid+1, end)


def binart_search3(a,x):
    return binart_search_sub(a, x, 0, len(a)-1)
    
print(binart_search3(a, 2))


#자료구조
#큐&스택
q=[]
st=[]
# 선입 선출
q.append(1)
q.pop(0)
#선입 후출
st.append(1)
st.pop()

def palindrome(s):
    qu=[]
    st=[]
    
    for x in s:
        #특수문자,공백,숫자 없애주는 isalpha
        if x.isalpha():
            #소문자로 바꿔주는 lower
            qu.append(x.lower())
            st.append(x.lower())
            
    while qu:
        if qu.pop(0)!=st.pop():
            return False
        
    return True

print(palindrome("WOW"))
print(palindrome("APPLE"))
print("---------------------")
def palindrome2(s):
    a=[]
    j=len(a)-1
    for x in s:
        #isalpha()로 쓸것 괄호없으면 안됌
        if x.isalpha():
            
            a.append(x.islower)
    for i in range(0,len(a)):
        if a[i]!=a[j]:
            return False
        j-=1
    return True
    
print(palindrome2("WOW"))
print(palindrome2("APPLEA"))
print(palindrome2("QWERQ"))
print(palindrome2("QWER"))
print(palindrome2("madam,i'm adam."))

#dict
d={1:"QWE",2:"WER",3:"RRR"}
print(len(d))
print(d[1])
d[1]=1
print(d[1])
del d[1]
# print(d[1])
print(2 in d)
d.clear()
#빈 딕트 생성
d=dict()

def nameCount(a):
    name_dict={}
    for name in a:
        if name in name_dict:
            name_dict[name]+=1
        else:
            name_dict[name]=1
    
    result=set()
    for name in name_dict:
        if name_dict[name]>=2:
            result.add(name)
    return result
a=["TOM","TOM","TOM","JERRY"]
print(nameCount(a))

