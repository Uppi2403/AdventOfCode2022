with open('input_strategy', 'r') as f:
    lines = f.readlines()

    endScore = 0

    for line in lines:
        if line.strip():
            print(f"Enemys Choice {line[0]} | Elfs Choice {line[2]} ")
            
            if line[2] == "X": # Rock
                endScore += 1
                if line[0] == "A": # Draw - Enemy choose also Rock
                    endScore += 3
                elif line[0] == "C": # Win - Enemy choose Scissors
                    endScore += 6
            elif line[2] == "Y": # Paper
                endScore += 2
                if line[0] == "B": # Draw - Enemy choose also Paper
                    endScore += 3
                elif line[0] == "A": # Win - Enemy choose Rock
                    endScore += 6
            elif line[2] == "Z": # Scissor
                endScore += 3
                if line[0] == "C": # Draw - Enemy choose also Scissors
                    endScore += 3
                elif line[0] == "B": # Win - Enemy choose Paper
                    endScore += 6

print(f"Endscore: {endScore}")