from pymongo import MongoClient

class Database:
	def open_connection(self, host, port):
		self.client = MongoClient(host, port)
		self.db = self.client.podingcast
		self.podcasts = self.db.podcasts

	def close_connection(self):
		self.client.close()

	def insert_podcast(self, podcast):
		# Maybe some validation...
		self.podcasts.insert(podcast)