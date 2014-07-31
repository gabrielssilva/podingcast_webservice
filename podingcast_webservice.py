import web
from database import Database
import json

urls = (
    '/podcasts', 'get_podcasts',
    '/podcasts/(.*)', 'get_podcast_by_name',
    '/save_podcast/(.*)', 'save_podcast',
    '/save_podcast', 'save_podcast'
)

class get_podcasts:
	def GET(self):
		podcasts = {}
		with Database("localhost", 27017) as database:
			podcasts = database.get_podcasts()

		web.header('Content-Type', 'application/json')
		return json.dumps(podcasts)

class get_podcast_by_name:
	def GET(self, podcast_name):
		podcasts = {}
		with Database("localhost", 27017) as database:
			podcasts = database.get_podcast(podcast_name)
			
		web.header('Content-Type', 'application/json')
		return json.dumps(podcasts)

class save_podcast:
	def POST(self):
		json_podcast = web.data()
		podcast = json.loads(json_podcast)

		with Database("localhost", 27017) as database:
			database.insert_podcast(podcast)

		web.header('Content-Type', 'text/plain')
		return "OK"

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()