import requests
from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
from will import settings

class WeatherPlugin(WillPlugin):


    @respond_to("tell me the weather in (?P<place>.*)")
    @require_settings("WORLD_WEATHER_ONLINE_KEY",)
    def tell_me_the_weather_in(self, message, place):
        """tell me the weather in ___: Tell the weather in almost any city on earth."""
        if not hasattr(settings, "WORLD_WEATHER_ONLINE_KEY"):
            self.say("I need a world weather online key to do that.\n You can get one at http://developer.worldweatheronline.com, and then set the key as WORLD_WEATHER_ONLINE_KEY", message=message)
        else:
            r = requests.get("http://api.worldweatheronline.com/free/v2/weather.ashx?q=%s&format=json&num_of_days=1&key=%s" % (place, settings.WORLD_WEATHER_ONLINE_KEY))
            resp = r.json()
            if "request" in resp["data"] and len(resp["data"]["request"]) > 0:
                place = resp["data"]["request"][0]["query"]
		temp = resp["data"]["current_condition"][0]["temp_F"]
		desc = resp["data"]["current_condition"][0]["weatherDesc"][0]["value"]
                #current_time = self.parse_natural_time(resp["data"]["time_zone"][0]["localtime"])

                self.say("It's currently %s and %sF in %s." % (desc, temp, place), message=message)
            else:
                self.say("I couldn't find anywhere named %s." % (place, ), message=message)
