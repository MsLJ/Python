# -*- coding:utf-8 -*-

#콘솔출력 print()=println();
print("a");print("q");print("w");
#줄 안바뀌게 출력하려면? end추가
print("thank",end="");print("you");
#printf()는? 따로 -X   
#println(String.format("%d",10));
print("%d"%10)
print("%.2f"%1.23445)
print("키:%.1f\n몸무게:%.1fkg"%(180.1,80.1))
#\:\t,\n,\r
print("*************************")
print("이름:\t%s\t\t*\n나이:\t%d\t\t*\n회사명:\t%s\t\t*"%("이준하",23,"Soldesk"))
print("*************************")
#{"name":"홍삼","age":30}
print('{"name"|"red ginseng"|"age"|30}')

