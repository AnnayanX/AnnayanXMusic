from AnnayanX.core.bot import AnnayanX
from AnnayanX.core.dir import dirr
from AnnayanX.core.git import git
from AnnayanX.core.userbot import Userbot
from AnnayanX.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = AnnayanX()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
