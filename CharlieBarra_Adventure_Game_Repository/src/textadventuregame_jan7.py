rooms = {
        'Hall': {
            'south': 'Kitchen',
            'east': 'Dining Room',
            'item': 'key'
        },
        'Kitchen': {
            'north': 'Hall',
            'item': 'monster'
        },
        'Dining Room': {
            'west': 'Hall',
            'south': 'Garden',
            'item' : 'potion'
        },
        'Garden': {
            'north': 'Dining Room'
        }
}

inventory = []
current_room = 'Hall'

def show_instructions():
    print('RPG Game')
    print('========')
    print('')
    print('Get to the Garden with a key and a potion')
    print('Avoid the monsters!')
    print('')
    print('Commands:')
    print('  go [direction]')
    print('  get [item]')

def show_status(current_room, inventory):
    print('--------')
    print('You are in the',current_room)
    print('Inventory: ' + str(inventory))
    if 'item' in rooms[current_room]:
        print('You see a',rooms[current_room]['item'])
        
show_instructions()
show_status(current_room,inventory)


while True:
    direction = ''
    item = ''
    action = input('>')
    command = action.split(' ')
    
    if command[0] == 'go':
        direction = command[1]
        if direction not in rooms[current_room]:
            print('You cant go that direction')
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            
    if command[0] == 'get':
        item = command[1]
        if item not in rooms[current_room]['item']:
            print('You cant grab that item')
        if item in rooms[current_room]['item'] and item != '':
            inventory.append(item)

    show_status(current_room,inventory)

    if current_room == 'Kitchen':
        print('You died the monster in the kitchen.')
        break
        current_room == 'Garden'
    if current_room == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house.. YOU WIN!')
        break
