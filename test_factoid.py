import os
import unittest
import factoid
from errbot.backends.test import testbot
from errbot import plugin_manager


class TestFactoid(object):
    extra_plugin_dir = '.'

    def test_list_factoids(self, testbot):
        testbot.push_message('!list factoids')
        assert 'I have not learned any factoids yet.' in testbot.pop_message()

        testbot.push_message('!water is wet')
        assert 'Got it, water is wet' in testbot.pop_message()

        testbot.push_message('!list factoids')
        assert "I'm Err! I know about:" in testbot.pop_message()
        assert 'water' in testbot.pop_message()

    def test_learn_factoid(self, testbot):
        testbot.push_message('!water is wet')
        assert 'Got it, water is wet' in testbot.pop_message()

        testbot.push_message('water?')
        assert 'water is wet' in testbot.pop_message()

        testbot.push_message('!water is hot')
        assert 'I already know about water.' in testbot.pop_message()

        testbot.push_message('!water is wet?')
        assert '/me does not know about water is wet' in testbot.pop_message()

    def test_tell_factoid_unknown(self, testbot):
        testbot.push_message('sky?')
        assert '/me does not know about sky' in testbot.pop_message()

    def test_forget_factoid(self, testbot):
        testbot.push_message('!sky is blue')
        assert 'Got it, sky is blue' in testbot.pop_message()

        testbot.push_message('sky?')
        assert 'sky is blue' in testbot.pop_message()

        testbot.push_message('!forget sky')
        assert 'OK, I forgot about sky' in testbot.pop_message()

        testbot.push_message('!list factoids')
        assert 'I have not learned any factoids yet.' in testbot.pop_message()

    def test_forget_factoid_unknown(self, testbot):
        testbot.push_message('!forget sky')
        assert 'I did not know about sky' in testbot.pop_message()
