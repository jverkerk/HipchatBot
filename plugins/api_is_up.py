import requests

from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class api_is_upPlugin(WillPlugin):

    @periodic(second='30')
    def api_is_up(self):
       try:
          r = requests.get("http://api01-usw2a.app.netuitive.com:8081/health")
          last_status = self.load("last_api01_status")
          if last_status != r.json()["status"]:
             if r.json()["status"] == "UP":
                self.say("api01 is up")
                self.save("last_api01_status", "UP")
       except requests.exceptions.ConnectionError, e:
          last_status = self.load("last_api01_status")
          if last_status != "DOWN":
             self.say("FYI everyone, api01 is having trouble: %s" % e, color="red")
          self.save("last_api01_status", "DOWN")
