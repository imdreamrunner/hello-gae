import webapp2
from webapp2_extras import sessions
from apple_tree import Game


class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()


class IndexPage(webapp2.RequestHandler):
    def get(self):
        self.redirect("/static/index.html")


class NewGame(BaseHandler):
    def get(self):
        game = Game([])
        self.session["state"] = game.get_states()
        self.response.write(game.get_output())


class InputHandler(BaseHandler):
    def post(self):
        game = Game(self.session.get("state"))
        game.set_input(self.request.body)
        self.session["state"] = game.get_states()
        self.response.write(game.get_output())


urls = [
    ('/', IndexPage),
    ('/new_game', NewGame),
    ('/input', InputHandler)
]

config = {'webapp2_extras.sessions': {
    'secret_key': 'my-super-secret-key',
}}

app = webapp2.WSGIApplication(urls, config = config)