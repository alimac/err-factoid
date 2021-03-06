[![Build Status](https://travis-ci.org/alimac/err-factoid.svg?branch=master)](https://travis-ci.org/alimac/err-factoid)
[![Coverage Status](https://coveralls.io/repos/alimac/err-factoid/badge.svg?branch=master&service=github)](https://coveralls.io/github/alimac/err-factoid?branch=master)

# Factoid plugin for Errbot

Factoid is a plugin for [Errbot](http://errbot.io), a Python-based chat bot.
It allows chat users to create "factoids" which the bot can recall on demand.

## Installation

To install the plugin, tell your bot in a private chat:

```
!repos install https://github.com/alimac/err-factoid.git
```

## Configuration

There is nothing to configure, yet.

While not required, I recommend that you uncomment and set the following in your
`config.py` file:

```
BOT_ALT_PREFIXES = ('Err',)
BOT_ALT_PREFIX_SEPARATORS = (':', ',', ';')
BOT_ALT_PREFIX_CASEINSENSITIVE = True
```

## Interaction

This plugin allows your bot to store and recall "factoids". Factoids are between
one and three words in length and follow the formula `thing is description`.

Examples:
```
!water is wet
!hot water is wet
!super hot water is wet and scalding
```

### Add a new factoid

```
!water is wet
```

Or, if you enabled the recommended prefixes:

```
Err, water is wet
```

Your bot should respond with:

```
Got it, water is wet
```

### Ask about a factoid

To have the bot recall a factoid, simply ask:

```
water?
what is water?
```

Your bot should reply:

```
water is wet
```

### Remove a factoid

To remove one of the factoids, say one of the following:

```
!forget water
!forget about water
```

Or, if you enabled the alternate prefix:

```
Err, forget water
Err, forget about water
```

### List all factoids

To list all the factoids, use:

```
!list factoids
```

The bot should respond with a comma-delimited list of factoids it knows about.

```
I'm Err! I know about:
water, hot water, very hot water
```
