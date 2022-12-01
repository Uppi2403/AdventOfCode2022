with open('puzzle_input', 'r') as f: # encoding="utf-8"
    lines = f.readlines()

    maxCalories = 0
    actualCalories = 0
    
    for line in lines:
        if line.strip():
            print(int(line))
            actualCalories += int(line) 
        else: # Counter is reset because new elf and possible highscore is saved
            if(actualCalories > maxCalories):
                maxCalories = actualCalories
            actualCalories = 0
            
print(f"maxCalories: {maxCalories}")