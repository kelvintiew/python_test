# TODO
#請撰寫一程式，輸入四個分別含有小數1到4位的浮點數
#然後將這四個浮點數以欄寬為7、欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊
#再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
print('|%7.2f %7.2f|' %(a, b))
print('|%7.2f %7.2f|'%(c, d))
print('|%-7.2f %-7.2f|' %(a, b))
print('|%-7.2f %-7.2f|' %(c, d))
# 靠右對齊
# TODO

# 靠左對齊
# TODO