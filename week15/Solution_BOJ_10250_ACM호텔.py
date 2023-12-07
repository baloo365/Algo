T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    ho = (N//H)+1
    floor = N%H
    
    if N%H == 0:
        ho = N//H
        floor = H
    else:
        pass
    
    
    if ho < 10:
        print(str(floor)+"0"+str(ho))
    else:
        print(str(floor)+""+str(ho))
