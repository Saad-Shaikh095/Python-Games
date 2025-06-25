import random
from playsound import playsound

def play_sound(result):
    if result == "lose":
        playsound("lose.mp3")
    elif result == "win":
        playsound("prob.mp3")
    elif result == "draw":
        playsound("draw.mp3")
    


def play_game():
    options = ["rock", "paper", "scissors"]
    print("🎮 Welcome to Saad's Rock, Paper, Scissors with SOUND!")

    user_score = 0
    comp_score = 0

    while True:
        user = input("\nChoose rock, paper or scissors (or 'q' to quit): ").lower()
        if user == 'q':
            print("Game Over! Final Scores:")
            print(f"You: {user_score} | Computer: {comp_score}")
            break
        if user not in options:
            print("⚠️ Invalid choice. Try again.")
            continue

        comp = random.choice(options)
        print(f"Computer chose: {comp}")

        if user == comp:
            print("🤝 It's a Draw!")
            play_sound("draw")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("✅ You Win!")
            user_score += 1
            play_sound("win")
        else:
            print("❌ You Lose!")
            comp_score += 1
            play_sound("lose")

        print(f"🏆 Scoreboard: You {user_score} | Computer {comp_score}")

play_game()
