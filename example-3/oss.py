import webapp2

c = 1


class CountPage(webapp2.RequestHandler):
    def get(self):
        global c
        c += 1
        self.response.write(c)

urls = [
    ('/', CountPage)
]

app = webapp2.WSGIApplication(urls)