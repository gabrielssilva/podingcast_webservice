import web

urls = (
    '/podcasts', 'get_podcasts',
    '/podcasts/(.*)', 'get_podcast_by_name'
)

class get_podcasts:
	def GET(self):
		return "Just testing..."

class get_podcast_by_name:
	def GET(self, podcast_name):
		return "Just testing (" + podcast_name + ")..."

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()