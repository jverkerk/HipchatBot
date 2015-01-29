import requests
from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
from will import settings

class MemeMePlugin(WillPlugin):

# For changes or additional memes look here : http://memegenerator.net/

    @respond_to("meme me (?P<image>.*?) (with) (?P<texttop>.*?) (and) (?P<textbottom>.*)")
    @require_settings("MEMEGEN_USER","MEMEGEN_PASS")
    def meme_me(self, message, image, texttop, textbottom):
        """meme me ___ with ___ and ___: pull up meme image with top and bottom text
           Memes to choose from:
           mimitw - Most Interesting Man in the World
           batman - Batman smacking Robin
           raptor - Philosiraptor
           xzibit - Xzibit
           grumpycat - Grumy Cat
           ... - default is our favorite boss from Office Space
        """
        if not hasattr(settings, "MEMEGEN_USER") or not hasattr(settings, "MEMEGEN_PASS"):
            self.say("I need a username and password for the API to do this.\n You can get one at http://memegenerator.net/, and then set the key as MEMEGEN_USER and MEMEGEN_PASS in config.py", message=message)
        else:
            if image == 'mimitw':
                genid = 74
                imageid = 2485
            elif image == 'batman':
                genid = 1213598
                imageid = 5129437
            elif image == 'raptor':
                genid = 17
                imageid = 984
            elif image == 'xzibit':
                genid = 79
                imageid = 108785
            elif image == 'grumpycat':
                genid = 1771888
                imageid = 6541210
            else:
                genid = 1853998
                imageid = 7665331
            r = requests.get("http://version1.api.memegenerator.net/Instance_Create?username=%s&password=%s&languageCode=en&generatorID=%s&imageID=%s&text0=%s&text1=%s" % (settings.MEMEGEN_USER, settings.MEMEGEN_PASS, genid, imageid, texttop, textbottom))
            resp = r.json()
            if len(resp["result"]["instanceImageUrl"]) > 0:
		link = resp["result"]["instanceImageUrl"]

                self.say("%s" % link, message=message)
            else:
                self.say("something went wrong", message=message)
