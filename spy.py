import os
import time

def spy_mission():
    print("\033[1;31m--- मिशन: जासूसी कैमरा चालू ---")
    print("प्रिंस और इशिका, सावधान! 3 सेकंड में फोटो खींचेगी...\033[0m")
    
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    # पीछे वाले कैमरे से फोटो खींचकर 'spy_photo.jpg' नाम से सेव करेगा
    os.system("termux-camera-photo -c 0 spy_photo.jpg")
    print("\n\033[1;32m✅ फोटो खींच ली गई है! इसे देखने के लिए 'termux-open spy_photo.jpg' टाइप करें।\033[0m")

if __name__ == "__main__":
    spy_mission()
