# Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.

def combat(health, damage):
    new_health = health - damage
    
    if new_health < 0:
        new_health = 0
        print("Health can't be below 0")
        
    return new_health