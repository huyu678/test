c;:`oding:utf-8

import csv
import matplotlib.pyplot as plt
with open("sitka_weather_07-2014.csv") as f:
    reader = csv.reader(f) #创建一个和f相联系的阅读器对象
    print(reader)
    header_row = next(reader)#返回阅读器的下一行
    column_2 = []
    for row in reader:
     #其实这里reader被读取了头文件之后，剩下的部分就是数值了
        column_2.append(int(row[1]))

fig = plt.figure(dpi = 128,figsize = (10,6))
plt.plot(column_2,c = "red")
plt.title("Daily high temperature,July 2014",fontsize = 14)
plt.xlabel("",fontsize = 14)
plt.ylabel("Temperature(F)",fontsize = 14)
# plt.tick_params(axis = "both",which = "both",labelsize = 14)
#感觉上面这句加上或者不加上没有什么太大的区别
plt.show()
        

'''enumerate接受列表为参数，返回的是一个可迭代的对象，内部元素以类似于健值得方式
#配对
In [3]: for i,j in enumerate(['a','b','c']):
   ...:     print(i,j)
   ...:     
0 a
1 b
2 c'''

