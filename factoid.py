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

        if factoid in self.factoid_store:
            return "%s is %s" % (factoid, format(self.factoid_store[factoid]))

        else:
            return "/me doesn't know about %s" % (factoid)

    @re_botcmd(pattern=r'^forget( about)? ((\w+\s??){1,3})$', prefixed=True, flags=re.IGNORECASE)
    def forget_factoid(self, message, match):
        factoid = match.group(2)

        if factoid in self.factoid_store:
            self.factoid_store.pop(factoid, None)
            self['FACTOID'] = self.factoid_store

            return "OK, I forgot about %s" % (format(factoid))

        else:
            return "It's not like I knew about %s in the first place." % (format(factoid))
