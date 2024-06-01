import random

def spin_spinner():
    body_parts = ["right foot", "right hand", "left foot", "left hand"]
    colors = ["red", "blue", "yellow", "green"]
    
    body_part = random.choice(body_parts)
    color = random.choice(colors)
    
    return body_part, color

def main():
    body_part, color = spin_spinner()
    print("Spinner landed on:", body_part, "and", color)

if __name__ == "__main__":
    main()

