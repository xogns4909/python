while True:
    co ,tem = map(int,input().split())
    print((co+(co//tem))+((co%tem+co//tem)//tem))
