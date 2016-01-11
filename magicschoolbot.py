"""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from pybot import PyBot
import re

class MagicSchoolBot(PyBot):

    def bot_init(self):

        self.config['api_key'] = ''
        self.config['api_secret'] = ''
        self.config['access_key'] = ''
        self.config['access_secret'] = ''

        self.config['search_interval'] = 60
        self.config['search_keywords'] = [
            '"Please let this be"',
            '"please let this be"',
            '"Please, let this be"',
            '"please, let this be"',
            ]

    def on_tweet(self):
        pass

    def on_mention(self, tweet, prefix):
        pass

    def on_timeline(self, tweet, prefix):
        pass

    def on_search(self, tweet):
        name = tweet.user.screen_name
        match = re.search('', tweet.text)
        status = "@" + name + " with the Frizz? No way!"
        self.update_status(status, reply_to = tweet)

    def on_follow(self, friend):
        pass

if __name__ == "__main__":
    bot = MagicSchoolBot()
    bot.run()
