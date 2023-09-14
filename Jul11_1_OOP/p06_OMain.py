# -*- coding:utf-8 -*-
#처음에 내가짰던 코드는 이 Main이 병원이라고 생각들어서 
#doctor와 guest를 둘다 불러내서 한명씩 대화하는식으로 코드를짰는데
#그건 잘못됐다는걸 깨달았다.
#여긴 Main에서 소스코드를 늘리는일은 쓰레기코드이며 애초에 적합하지않다.
# 소스코드가 길어지고 계산하는건 M쪽의 일이지 C쪽의 역활이 아니기때문이다.
from doctor.doctor import doctor
d=doctor
d.start(d)


#if __name__ == '__main__':
