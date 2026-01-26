import random
import os

def play_game():
    os.system('clear')
    print("===============================")
    print("   KANSWAL MATH CHALLENGE 🏆   ")
    print("===============================")
    
    # सवाल बनाना
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_ans = num1 + num2
    
    print(f"प्रिंस और इशिका, बताइए: {num1} + {num2} = ?")
    
    try:
        user_ans = int(input("आपका जवाब लिखें: "))
        if user_ans == correct_ans:
            print("\n✅ शाबाश! बिल्कुल सही जवाब। 🌟")
        else:
            print(f"\n❌ गलत जवाब! सही उत्तर {correct_ans} था।")
    except:
        print("⚠️ कृपया सिर्फ नंबर ही लिखें!")

if __name__ == "__main__":
    play_game()

