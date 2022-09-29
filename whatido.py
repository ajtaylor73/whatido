# whatido.py

def get_user_msg():
	msg = input("--> ")
	if msg == 'q':
		exit()
	print(f"Recording: {msg}")
	return msg
	
if __name__ == '__main__':
	while (True):
		get_user_msg()

