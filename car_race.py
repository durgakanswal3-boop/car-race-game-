import random
import os
import time
import sys

def race():
    road_width = 15
    car_pos = road_width // 2
    score = 0
    obstacles = []

    while True:
        os.system('clear')
        print(f"\033[1;33m--- KANSWAL RACING CLUB ---")
        print(f"प्रिंस और इशिका, स्कोर: {score}\033[0m")
        print("\033[1;30m|" + "-" * road_width + "|\033[0m")

        # बाधाएं बनाना (Obstacles)
        if random.random() < 0.3:
            obstacles.append([random.randint(0, road_width - 1), 0])

        current_frame = [" "] * road_width
        current_frame[car_pos] = "\033[1;32m🏎️\033[0m" # आपकी कार

        # बाधाओं को नीचे खिसकाना
        for obs in obstacles[:]:
            obs[1] += 1
            if obs[1] > 10:
                obstacles.remove(obs)
                score += 1
            elif obs[1] == 9 and obs[0] == car_pos:
                print("\033[1;31m💥 CRASH! गेम खत्म! 💥\033[0m")
                return

        # सड़क दिखाना
        print("\033[1;30m|\033[0m", end="")
        row = [" "] * road_width
        for obs in obstacles:
            if obs[1] < 10: row[obs[0]] = "🪨"
        row[car_pos] = "🏎️"
        print("".join(row) + "\033[1;30m|\033[0m")

        print("\033[1;37mबाएँ जाने के लिए 'a' और दाएँ के लिए 'd' दबाकर Enter करें\033[0m")
        
        move = input("Move (a/d): ").lower()
        if move == 'a' and car_pos > 0: car_pos -= 1
        elif move == 'd' and car_pos < road_width - 1: car_pos += 1

if __name__ == "__main__":
    race()
