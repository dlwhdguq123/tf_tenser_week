class Bmi:

     def __init__(self,name,w,t):
         self.name = name
         self.w = w
         self.t = t

     def bbmi(self):
        bmi = (self.w/(self.t*self.t))*10000

        if bmi >= 40:
            result = "고도비만"
        elif bmi >= 35:
            result= "중등도비만"
        elif bmi >= 30:
            result= "경도비만"
        elif bmi >= 25:
            result="과체중"
        elif bmi >= 18.5:
            result="정상"

        return result