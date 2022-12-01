with open('puzzle_input', 'r') as f:
    lines = f.readlines()

    maxCalories = 0
    actualCalories = 0
    carryingPerElf = []
    
    for line in lines:
        if line.strip():
            actualCalories += int(line)
        else: # Counter is reset because new elf and possible highscore is saved
            
            if(actualCalories > maxCalories):
                maxCalories = actualCalories
                
            carryingPerElf.append(actualCalories)
            actualCalories = 0

carryingPerElf.sort()
sumMostCarrying = sum(carryingPerElf[-3:])
print(f"sumMostCarrying: {sumMostCarrying}")
print(f"maxCalories: {maxCalories}")