import re

from errbot import BotPlugin, botcmd, re_botcmd

class Factoid(BotPlugin):
    """Factoid plugin"""

    @re_botcmd(pattern=r'^((\w+\s??){1,3}) is (.+$)', prefixed=False, flags=re.IGNORECASE)
    def factoid(self, message, match):
        factoid = match.group(1)
        content = match.group(3)
        return "You said: %s is %s" % (format(factoid), format(content))
