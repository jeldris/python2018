import csv
import matplotlib.pyplot as plt
f = open('���ष.csv')
p = input('����ʴϱ�?ex:/ȿ�ڵ�:')
data = csv.reader(f)
place = []
for row in data :
    if p in row[0] :
        for i in range(3,len(row),3) : 
            place.append(int(row[i]))
        plt.plot(place)
        plt.title(row[0]+'�Ż��� ��') 
        plt.rc('font',family='Malgun Gothic') 
        plt.xticks(range(6),['2017��12��','2018��1��','2018��2��','2018��3��','2018��4��','2008��5��')]
        plt.xlabel('�⵵') 
        plt.ylabel('��') 
        plt.ylim(0,70) 
	plt.show()
    else:
        print('�׷����� ���������ʽ��ϴ�.�ٽýõ����ּ���')
    (break)
#���� ���� �κ��� Ʋ������ ������ ������ �ʾҴµ� ������ ���߰� break�̶�� ���� �־ �ݺ����� ���߷��� �Ͽ��� �ȵǾ� �ϴ� ���� �Ҷ��� ���� ���״�.

        plt.show()
k = input('����Ż��� ���� �˰�ͽ��ϱ�?')
woman = 0
man = 0
if k == '��' :
    for row in data :
        if p in row[0] :
            for z in (1,16,3) :
                woman = woman + int(row[z])           
            for q in (2,17,3) :
                man = man + int(row[q])
    plt.pie([woman ,man], labels = ['��','��'], autopct='%1.1f%%')
    colors = ['red', 'blue']  
    plt.title('���� �Ż��Ƽ� ����')
    plt.rc('font',family='Malgun Gothic') 
    plt.axis('equal')
    plt.show()
else :
    print('�̿����ּż� �����մϴ�.')
e = input('���������� ������ �˰�ͽ��ϱ�?')
gu = []
glit = []
if e == '��' :
    m=input('���� �Է����ּ���')
    if m in row[0] :
        for i in range(3,len(row),3) : 
            gu.append(int(row[i]))
            date= ['2017��12��','2018��1��','2018��2��','2018��3��','2018��4��','2018��5��']
            for i in range(5) :
                glit.append(place[i]/gu[i])
            plt.bar(range(4),date , width = 0.4, label='����')
            plt.xticks([0,1,2,3,4,], glit)
            plt.legend()
            plt.show()
else:
    print('�̿����ּż� �����մϴ�.') 
