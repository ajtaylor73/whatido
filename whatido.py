# whatido.py


class Log:
	DEFAULT_LOG = "captains.log"

	def __init__(self):
		self.filepath = "."
		self.filename = Log.DEFAULT_LOG

	def store(self, log_item):
		print(f"Recording: {log_item}")



def get_user_msg():
	msg = input("--> ")
	if msg == 'q':
		exit()
	return msg
	
if __name__ == '__main__':
	log = Log()

	while (True):
		log_item = get_user_msg()
		log.store(log_item)

