def roll_call_dwarves(dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]):
    index = 0
    while index < len(dwarves):
        print(f"{index+1}. {dwarves[index]}")
        index += 1

def summon_captain_planet(planeteer_calls = ["earth", "wind", "fire", "water", "heart"]):
    return [call.capitalize() + "!" for call in planeteer_calls]

def long_planeteer_calls(calls_list):
    list = []
    [list.append(call) for call in calls_list if len(call) > 4]
    if list != []:
        return True
    else:
        return False

def find_the_cheese(ingridients):
    cheeses = ["cheddar", "gouda", "camembert"]
    first_cheese = [ingridient for ingridient in ingridients if ingridient in cheeses]
    if first_cheese != []:
        return first_cheese[0]
    else:
        return None
