import web
from database import Database

urls = (
    '/podcasts', 'get_podcasts',
    '/podcasts/(.*)', 'get_podcast_by_name',
    '/save_podcast/(.*)', 'save_podcast'
)

class get_podcasts:
	def GET(self):
		return "Just testing..."

class get_podcast_by_name:
	def GET(self, podcast_name):
		return "Just testing (" + podcast_name + ")..."

class save_podcast:
	def GET(self, podcast_name):
		self.new_podcast(podcast_name)
		return "OK"

	def new_podcast(self, podcast_name):
		podcast = { 
			"name": podcast_name 
		}
		with Database("localhost", 27017) as database:
			database.insert_podcast(podcast)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()