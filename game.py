import world
from player import Player

def play():
	world.load_tiles()
	player = Player()
	#These lines load the starting room and display the text
	room = world.tile_exists(player.location_x, player.location_y)
	if room is None:
		room = world.tile_exists(2,0)
	print(room.intro_text())
	while player.is_alive() and not player.victory:
		#loop that shit
		room = world.tile_exists(player.location_x, player.location_y)
		room.modify_player(player)
		#check again since the room could've changed the player's state
		if player.is_alive() and not player.victory:
			print("Choose an action:\n")
			available_actions = room.available_actions()
			for action in available_actions:
				print(action)
			action_input = input('Action: ')
			for action in available_actions:
				if action_input == action.hotkey:
					player.do_action(action, **action.kwargs)
					break


if __name__ == "__main__":
	play()
