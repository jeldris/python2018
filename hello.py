import csv
import matplotlib.pyplot as plt
f = open('서울시 신생아수.csv')
p = input('어디사십니까?ex:/효자동:')
data = csv.reader(f)
data = list(data)
place = []
rate = []
v = 0
for row in data :
    if p in row[0] :
        for i in range(3,len(row),3) : 
            place.append(int(row[i]))
        plt.rc('font',family='Malgun Gothic') 
        plt.plot(place)
        plt.title(row[0]+'신생아 수') 
        plt.xticks(range(6),['2017년12월','2018년1월','2018년2월','2018년3월','2018년4월','2018년5월'])
        plt.xlabel('년도') 
        plt.ylabel('수') 
        plt.ylim(0,80) 
        plt.show()
      
        for i in range(3,len(row),3) : 
                v = v+int(row[i])
        for i in range(3,len(row),3) : 
            rate.append(float(row[i])/v)
        date= ['2017년12월','2018년1월','2018년2월','2018년3월','2018년4월','2018년5월']
        plt.bar(range(6),rate , width = 0.5, label='비율')
        plt.xticks([0,1,2,3,4,5], date)
        plt.legend()
        plt.show()
    #else:
       # print('그런곳은 존재하지않습니다.다시시도해주세요')
    #(break)
#여기 부분은 틀린곳이 마땅히 보이지 않았는데 자료에 존재하는값인데도 불구하고 저것이 프린트가 되었더.
k = input('남녀신생아 성비를 알고싶습니까?')
woman = 0
man = 0
if k == '네' :
    for row in data :
        if p in row[0] :
            for z in (1,16,3) :
                woman = woman + int(row[z])           
            for q in (2,17,3) :
                man = man + int(row[q])
    plt.pie([woman ,man], labels = ['남','녀'], autopct='%1.1f%%')
    colors = ['red', 'blue']  
    plt.title('남녀 신생아수 비율')
    plt.rc('font',family='Malgun Gothic') 
    plt.axis('equal')
    plt.show()
    print('도움이 되셨나요?, 이용해주셔서 감사합니다')
else :
    print('이용해주셔서 감사합니다.')

