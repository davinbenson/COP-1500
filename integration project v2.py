#Davin Benson
#COP 1500
#Integration project Sprint 2

def phase_one():
    #everything from sprint 1 mostly unchanged
    print("Welcome to the Virtual Fantasy Combat Simulator")
    playName = input("Please enter a name: ")
    print("Hello," , playName ,"\nThe simulation begins now.", sep = ' ')
    print("Due to a lack of funding, we must ask that you rely on your imagination to visualize the upcoming events.")
    print("There is also no limit to any damage values, so go overboard at your own risk.", end = '\n\n')
    print("Your first opponent will be a common slime enemy. You are given a sword to defend yourself.")
    dmg1 = abs(int(float(input("To begin, assign a damage number value to your sword: "))))
    print(playName + " strikes the slime dealing " , dmg1 , " damage. The slime is defeated.", sep = '', end = '\n\n')
    print("Next up, a goblin approaches holding a wooden shield.")
    dmg2 = abs(int(float(input("Try a different attack this time. Enter another damage value: "))))
    print(playName + " swings at the goblin, its shield blocking some of the force. " , abs(dmg2 - 50) , " damage is dealt.", sep = '')
    numHits = abs(int(float(input("It's wide open. How many times do you hit it?: "))))
    flurryDmg = (dmg2 * numHits)
    print(playName + " throws a flurry of strikes at the goblin dealing " , flurryDmg , " damage. Another victory.", sep = '', end = '\n\n')
    print("Here comes a strong knight. His armor looks sturdy.")
    dmg3 = abs(int(float(input("Go for another technique. Enter an extra powerful damage value: "))))
    armorHit = int(dmg3 / 3)
    print(playName + " swipes at the knight, though he stands his ground and takes only " , armorHit , " damage.", sep = '')
    print("It isn't enough. Time for extreme measures.")
    potionDmg = abs(int(float(input("You take a strength potion. Enter the potency of its effect: "))))
    enhancedDmg = int(dmg3 ** potionDmg)
    lessEnhancedDmg = int(enhancedDmg / 3)
    print(playName + " goes all out, striking the knight with " , lessEnhancedDmg , " damage. It is enough.", sep = '', end = '\n\n')
    print("You feel unstoppable. Next you challange a giant dragon.")
    combo1 = abs(int(float(input("Time to use everything you've learned. Try a combo of strikes, how many?: "))))
    combo2 = ((dmg1 + dmg2 + dmg3) * combo1) ** potionDmg
    print("The dragon is no match for your power. You strike relentlessly dealing ", combo2 ," damage. Easy.", sep = '', end = '\n\n')
    print("No worldly force can hold you back any longer. You challenge the simulation itself.")
    finalHit = abs(int(float(input("You open the developer console and type in the largest number you can think of: "))))
    print("You swing at nothing in particular dealing " , combo * finalHit , " damage to the fabric of space-time.", sep = '', end = '\n\n')
    print("You have torn a hole in reality.")
    print("The simulation is over." * 20, end=" goodbye.", sep = ' ')

def phase_two_start():
    #everything here is new from sprint 1
    print("hi")

def main():
    phase_one()
    phase_two_start()

#####################################

main()
