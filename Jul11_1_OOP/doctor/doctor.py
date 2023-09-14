from guest.guest import guest

class doctor:
    def start(self):
        print("Start")
        g = self.callGuest(self)
        g.hello(self)
        self.ask(self,g)
        self.getBMI(self,g)
        self.tellResult(self,g)

    def callGuest(self):
        return guest

    def ask(self,g):
        print("이름 나이 몸무게 키를 적어주세요")
        g.name, g.age, g.weight, g.height = g.write(self)
        if g.height>3:
            g.height/=100
            

    def getBMI(self,g):
        g.bmi=g.weight / (g.height * g.height)
        g.status="저체중"
        if g.bmi>=35:
            g.status="고도비만"
        elif g.bmi>=30: 
            g.status="중도비만"
        elif g.bmi>=25: 
            g.status="경도비만"
        elif g.bmi>=23: 
            g.status="과체중"
        elif g.bmi>=18.5: 
            g.status="정상"

    def tellResult(self,g):
        print(g.name,"님의BMI는",g.bmi,"%")
        print(g.age, "세", g.name, "님의 ", g.status, "입니다.")
