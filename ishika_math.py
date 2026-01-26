import os
import math

def study_buddy():
    os.system('clear')
    print("\033[1;36m====================================")
    print("      ISHIKA'S SMART ASSISTANT      ")
    print("====================================\033[0m")
    
    print("1. किसी संख्या का वर्गमूल (Square Root)")
    print("2. वृत्त का क्षेत्रफल (Area of Circle)")
    print("3. प्रतिशत निकालें (Percentage)")
    
    choice = input("\nइशिका, आप क्या हल करना चाहती हैं? (1/2/3): ")

    if choice == '1':
        n = float(input("संख्या लिखें: "))
        print(f"\nउत्तर: {n} का वर्गमूल है {math.sqrt(n)}")
    elif choice == '2':
        r = float(input("त्रिज्या (Radius) लिखें: "))
        area = math.pi * (r**2)
        print(f"\nउत्तर: वृत्त का क्षेत्रफल है {area:.2f}")
    elif choice == '3':
        total = float(input("कुल अंक: "))
        obtained = float(input("प्राप्त अंक: "))
        print(f"\nउत्तर: आपकी प्रतिशत है {(obtained/total)*100}%")

if __name__ == "__main__":
    study_buddy()
