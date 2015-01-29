from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings

class ResponsePlugin(WillPlugin):

    @respond_to("make me a sandwich")
    def sandwich(self, message):
        """make me a sandwich"""
        self.say("http://blogs.plos.org/obesitypanacea/files/2014/10/sandwich.jpg", message=message)

#    @respond_to("^hi")
#    def hi(self, message):
#        """hi: I know how to say hello!"""
#        self.reply(message, "hello!")

#    @respond_to("^hello$")
#    def hello(self, message):
#        self.reply(message, "hi!")
