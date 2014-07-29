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

	def get_podcasts(self):
		cursor = self.podcasts.find()
		all_podcasts = self.cursor_to_array(cursor)
		return all_podcasts

	def get_podcast(self, name):
		cursor = self.podcasts.find({"name": {"$regex": name}})
		podcasts = self.cursor_to_array(cursor)
		return podcasts

	def cursor_to_array(self, cursor):
		podcasts = []
		for podcast in cursor:
			clean_podcast = self.filter_dict(podcast)
			podcasts.append(clean_podcast)
		return podcasts

	# Need to remove the _id item from the dict
	def filter_dict(self, podcast):
		new_podcast = {}
		for key in podcast:
			if key != "_id":
				new_podcast[key] = podcast[key]
		return new_podcast
