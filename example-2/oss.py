import webapp2

class IndexPage(webapp2.RequestHandler):
    def get(self):
        self.redirect("/static/index.html")

urls = [
    ('/', IndexPage)
]

app = webapp2.WSGIApplication(urls)