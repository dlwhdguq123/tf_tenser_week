from bmi_calc.bmi import Bmi

def main():
    name = input("이름")
    w= float(input("몸무게"))
    t= float(input("키"))
    bmi= Bmi(name,w,t)
    aa = bmi.bbmi()
    print("{}님은 {}입니다."
            .format(name
                    , aa))

if __name__ == '__main__':
    main()