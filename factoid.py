import re

from errbot import BotPlugin, botcmd, re_botcmd

class Factoid(BotPlugin):
    """Factoid plugin"""

    factoid_store = {}

    @re_botcmd(pattern=r'^((\w+\s??){1,3}) is (.+$)', prefixed=True, flags=re.IGNORECASE)
    def learn_factoid(self, message, match):
        factoid = match.group(1)
        content = match.group(3)

        self.factoid_store[factoid] = content
        self['FACTOID'] = self.factoid_store

        return "Got it, %s is %s" % (format(factoid), format(content))

    @re_botcmd(pattern=r'^((\w+\s??){1,3})\?$', prefixed=False, flags=re.IGNORECASE)
    def tell_factoid(self, message, match):
        factoid = match.group(1)
        self.factoid_store = self['FACTOID']

        if self.factoid_store[factoid]:
            return "%s is %s" % (
                factoid,
                format(self.factoid_store[factoid])
            )
