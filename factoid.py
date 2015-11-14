import re

from errbot import BotPlugin, botcmd, re_botcmd

class Factoid(BotPlugin):
    """Factoid plugin"""

    factoid_store = {}

    @re_botcmd(pattern=r'^((\w+\s??){1,3}) is (.+$)', prefixed=True, flags=re.IGNORECASE)
    def learn_factoid(self, message, match):
        """ Save a factoid. Example: !learn factoid water is wet """

        factoid = match.group(1)
        content = match.group(3)

        if 'FACTOID' in self:
            self.factoid_store = self['FACTOID']

        if factoid in self.factoid_store:
            return "I already know about %s, but you can tell me to forget it." % (factoid)

        self.factoid_store[factoid] = content
        self['FACTOID'] = self.factoid_store

        return "Got it, %s is %s" % (format(factoid), format(content))

    @re_botcmd(pattern=r'^(what is )?((\w+\s??){1,3})\?$', prefixed=False, flags=re.IGNORECASE)
    def tell_factoid(self, message, match):
        """ Ask about a factoid (prefix not needed). Example: water?  """

        factoid = match.group(2)
        if 'FACTOID' in self:
            self.factoid_store = self['FACTOID']

        if factoid in self.factoid_store:
            return "%s is %s" % (factoid, format(self.factoid_store[factoid]))

        else:
            return "/me does not know about %s" % (factoid)

    @re_botcmd(pattern=r'^forget( about)? ((\w+\s??){1,3})$', prefixed=True, flags=re.IGNORECASE)
    def forget_factoid(self, message, match):
        """ Forget a factoid.  Example: !forget water or !forget about water """

        if 'FACTOID' in self:
            self.factoid_store = self['FACTOID']

        factoid = match.group(2)

        if factoid in self.factoid_store:
            self.factoid_store.pop(factoid, None)
            self['FACTOID'] = self.factoid_store

            return "OK, I forgot about %s" % (format(factoid))

        else:
            return "I did not know about %s." % (format(factoid))

    @botcmd
    def list_factoids(self, message, args):
        """ List all known factoids """

        if 'FACTOID' in self:
            self.factoid_store = self['FACTOID']

        if self.factoid_store:
            yield "I'm {}! I know about:" .format(self.bot_config.CHATROOM_FN)
            yield ', '.join(sorted(self.factoid_store.keys()))

        else:
            yield "I have not learned any factoids yet."
