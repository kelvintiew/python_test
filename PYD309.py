#TODO

#此為格式化輸出之標頭
#print('%s \t  %s' % ('Month', 'Amount'))
#TODO

    #此為格式化輸出之內容，需置於置於迴圈中
    
    #total = eval(input())
total = eval(input())
y = eval(input())
m = eval(input())

print('%s t  %s' % ('Month', 'Amount'))

for i in range(1, m + 1):
    total += total * y / 1200    
    print('%3d t %.2f' % (i, total))