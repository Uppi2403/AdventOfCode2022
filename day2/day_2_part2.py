with open('input_strategy', 'r') as f:
    lines = f.readlines()

    endScore = 0

    for line in lines:
        if line.strip():
            print(f"Enemys Choice {line[0]} | Elfs Choice {line[2]} ")
            # Rock      - 1
            # Paper     - 2
            # Scissors  - 3 
            if line[2] == "X": # need to loose
                if line[0] == "A": # Enemy choose Rock
                    endScore += 3
                elif line[0] == "B": # Enemy choose Paper
                    endScore += 1
                elif line[0] == "C": # Enemy choose Scissors
                    endScore += 2
            elif line[2] == "Y": # need to draw
                endScore += 3
                if line[0] == "A": # Enemy choose Rock
                    endScore += 1
                elif line[0] == "B": # Enemy choose Paper
                    endScore += 2
                elif line[0] == "C": # Enemy choose Scissors
                    endScore += 3
            elif line[2] == "Z": # need to win
                endScore += 6
                if line[0] == "A": # Enemy choose Rock
                    # Paper defeats Rock
                    endScore += 2
                elif line[0] == "B": # Enemy choose Paper
                    #Scissors deats Paper
                    endScore += 3
                elif line[0] == "C": # Enemy choose Scissors
                    # Rock defeats Scissors
                    endScore += 1

print(f"Endscore: {endScore}")