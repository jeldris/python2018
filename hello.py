import csv
import matplotlib.pyplot as plt
f = open('수행ㅇ.csv')
p = input('어디사십니까?ex:/효자동:')
data = csv.reader(f)
place = []
for row in data :
    if p in row[0] :
        for i in range(3,len(row),3) : 
            place.append(int(row[i]))
        plt.plot(place)
        plt.title(row[0]+'신생아 수') 
        plt.rc('font',family='Malgun Gothic') 
        plt.xticks(range(6),['2017년12월','2018년1월','2018년2월','2018년3월','2018년4월','2008년5월')]
        plt.xlabel('년도') 
        plt.ylabel('수') 
        plt.ylim(0,70) 
	plt.show()
    #else:
       # print('그런곳은 존재하지않습니다.다시시도해주세요')
    #(break)
#여기 빨간 부분은 틀린곳이 마땅히 보이지 않았는데 오류가 심했고 break이라는 것을 넣어서 반복으로 멈추려고 하여도 안되어어서 일단 실제 할때는 제외 시켰다.

        plt.show()
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
else :
    print('이용해주셔서 감사합니다.')
e = input('구내에서의 비율을 알고싶습니까?')
gu = []
glit = []
if e == '네' :
    m=input('구를 입력해주세요')
    if m in row[0] :
        for i in range(3,len(row),3) : 
            gu.append(int(row[i]))
            date= ['2017년12월','2018년1월','2018년2월','2018년3월','2018년4월','2018년5월']
            for i in range(5) :
                glit.append(place[i]/gu[i])
            plt.bar(range(4),date , width = 0.4, label='비율')
            plt.xticks([0,1,2,3,4,], glit)
            plt.legend()
            plt.show()
else:
    print('이용해주셔서 감사합니다.') 
