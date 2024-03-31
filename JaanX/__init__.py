from JaanX.core.bot import AyushSolo
from JaanX.core.dir import dirr
from JaanX.core.git import git
from JaanX.core.userbot import Userbot
from JaanX.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()
git()
dbb()
heroku()
# sudo()

app = AyushSolo()
userbot = Userbot()


from .platforms import *

Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
