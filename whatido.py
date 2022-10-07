# whatido.py

from datetime import datetime


def str_timestamp(t=datetime.now()):
	return t.strftime("%m/%d %H:%M")
	
class Log:
	DEFAULT_LOG = "captains.log"

	def __init__(self):
		self.filepath = "."
		self.filename = Log.DEFAULT_LOG
	
	def store(self, log_item, timestamp=str_timestamp()):
		print(f"<{timestamp}> {log_item}")

class UI:

	actions = {
		"q" : exit,
		"t" : set_time,
		"l" : get_do_log
	}

	def __init__(self, log):
		self.log = log
		self.next_action = 'l'

	def get_user_msg(self):
		msg = input("--> ")
		return msg
	
	def is_action(self, msg):
		if msg in UI.actions:
			return True
		else:
			return False

	def set_next_action(self, action):
		self.next_action = action

	def set_time(self):
		user_time = input("time: ")
		# attempt conversion to datetime
		# set new prompt and query message

	def get_do_log(self):
		log_item = self.get_user_msg()
		if self.is_action(log_item):
			action = log_item
			self.do_action(log_item)
		else:
			log.store(log_item)

	def do_action(self, action):
			UI.actions[action]()
		
if __name__ == '__main__':
	log = Log()
	ui = UI(log)

	while (True):
		ui.get_do_log()
