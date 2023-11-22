
ships = {
        'blue_ship': {
            (60, 100): 'pirate_pack/ships/ship (5).png',
            (30, 59): 'pirate_pack/ships/ship (11).png',
            (1, 29): 'pirate_pack/ships/ship (17).png',
            0: 'pirate_pack/ships/ship (23).png'
        },
        'red_ship': {
            (60, 100): 'pirate_pack/ships/ship (5).png',
            (30, 59): 'pirate_pack/ships/ship (11).png',
            (1, 29): 'pirate_pack/ships/ship (17).png',
            0: 'pirate_pack/ships/ship (23).png'
        }
    }

def get_ship_image(ship_color, life):
    ship_states = ships.get(ship_color, {})

    for state_range, image_path in ship_states.items():
        state_min, state_max = state_range
        if state_min <= life <= state_max:
            return image_path

    # If no matching state is found, return a default image path or handle as needed
    return 'default_image_path.png'

# Example usage:
ship_color = 'blue_ship'
life_value = 40
image_path = get_ship_image(ship_color, life_value)
print(f"The corresponding image path for {ship_color} and life {life_value} is: {image_path}")
