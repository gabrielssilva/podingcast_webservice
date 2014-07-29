from pymongo import MongoClient

class Database:
	def __init__(self, host, port):
		self.host = host
		self.port = port

	def __enter__(self):
		self.client = MongoClient(self.host, self.port)
		self.db = self.client.podingcast
		self.podcasts = self.db.podcasts
		return self

	def __exit__(self, type, value, traceback):
		self.client.close()

	def insert_podcast(self, podcast):
		# Maybe some validation...
		self.podcasts.insert(podcast)