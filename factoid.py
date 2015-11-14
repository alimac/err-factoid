import re

from errbot import BotPlugin, botcmd, re_botcmd


class Factoid(BotPlugin):
    """Factoid plugin"""

    factoid_store = {}
    re_learn_factoid = r'^((\w+\s??){1,3}) is (.+?)(\?+)?$'
    re_tell_factoid = r'^(what is )?((\w+\s??){1,3})\?+$'
    re_forget_factoid = r'^forget( about)? ((\w+\s??){1,3})$'

    @re_botcmd(pattern=re_learn_factoid, prefixed=True, flags=re.IGNORECASE)
    def learn_factoid(self, message, match):
        """ Save a factoid. Example: !learn factoid water is wet """

        factoid = match.group(1)
        content = match.group(3)
        question = match.group(4)

        if question:
            return

        if 'FACTOID' in self:
            self.factoid_store = self['FACTOID']

        if factoid in self.factoid_store:
            return "I already know about %s." % (factoid)

        self.factoid_store[factoid] = content
        self['FACTOID'] = self.factoid_store

        return "Got it, %s is %s" % (format(factoid), format(content))

    @re_botcmd(pattern=re_tell_factoid, prefixed=False, flags=re.IGNORECASE)
    def tell_factoid(self, message, match):
        """ Ask about a factoid (prefix not needed). Example: water?  """

        factoid = match.group(2)
        if 'FACTOID' in self:
            self.factoid_store = self['FACTOID']

        if factoid in self.factoid_store:
            return "%s is %s" % (factoid, format(self.factoid_store[factoid]))

        else:
            return "/me does not know about %s" % (factoid)

    @re_botcmd(pattern=re_forget_factoid, prefixed=True, flags=re.IGNORECASE)
    def forget_factoid(self, message, match):
        """ Forget a factoid.  Example: !forget water """

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
