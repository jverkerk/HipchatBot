from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings

class ResponsePlugin(WillPlugin):

    @respond_to("make me a sandwich")
    def sandwich(self, message):
        """make me a sandwich: I can make you a sandwich"""
        self.say("http://blogs.plos.org/obesitypanacea/files/2014/10/sandwich.jpg", message=message)

    @respond_to("make me a pie")
    def pie(self, message):
        """make me a pie: I know what pie is."""
        self.reply(message, "http://www.csn.edu/uploadedfiles/academics/divisions/science_and_math/math/images/potd_pi-pie.jpg")

    @respond_to("rm -rf.*")
    def rm(self, message):
        """rm -rf: I can erase it all"""
        self.reply(message, "Erasing everything.. Say bye bye to your Production environment (boom)")
