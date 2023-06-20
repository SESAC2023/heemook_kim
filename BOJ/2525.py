h, m = map(int, input().split())
t = int(input())

if h==0 and (m+t)//60:
    print((m+t)//60, (m+t)%60)
elif h!=0 and (m+t)//60:
    if h+(m+t)//60<24:
        print(h+(m+t)//60, (m+t)%60)
    else:
        print((h+(m+t)//60)-24, (m+t)%60)

elif h==0 and (m+t)<60:
    print(0, (m+t))
elif h!=0 and (m+t)<60:
    if h+(m+t)//60<24:
        print(h, (m+t))
    else:
        print((h+(m+t)//60)-24,(m+t))
