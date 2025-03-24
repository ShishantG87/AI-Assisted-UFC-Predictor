# Import Files
import fight_values

class FightProb:

# Open file and create variables to read in information from UFC Dataset
    with open(r"second-data-set\ufc_fighter_stats.txt", "r") as fdata:
        for line in fdata:
            print(line.rstrip())