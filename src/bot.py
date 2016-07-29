import telepot
import yaml
import logging
from random import getrandbits

from pkg_resources import resource_filename

from telepot.delegate import per_chat_id, per_inline_from_id, create_open


class NoSpoiler(telepot.helper.InlineUserHandler, telepot.helper.AnswererMixin):
    """NoSpoiler"""

    def __init__(self, seed_tuple, timeout):
        super(NoSpoiler, self).__init__(seed_tuple, timeout)

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        # shows that bot is typing
        self.bot.sendChatAction(chat_id, 'typing')
        answer = 'Olar {}'.format(msg['from']['first_name'])
        # to send a private msg back to user
        self.sender.sendMessage(answer)
        # so send a msg back to group, using reply
        self.bot.sendMessage(chat_id, answer,
                             reply_to_message_id=msg['message_id'])

        if ('entities' in msg.keys()):
            '''
             Can be mention (@username), hashtag, bot_command, url, email, 
             bold (bold text), italic (italic text), code (monowidth string), 
             pre (monowidth block), text_link (for clickable text URLs), 
             text_mention (for users without usernames)
            '''
            for entities in msg['entities']:
                print(entities['type'])
        else:
            # Only text
            print(msg)

        logging.debug(msg)

    def on_edited_chat_message(self, msg):
        print(msg)
        self.on_chat_message(msg)  # update output

    def on_inline_query(self, msg):
        query_id, from_id, query_string = telepot.glance(
            msg, flavor='inline_query')

        def compute_answer():
            # should return a list with this model
            result = [{'type': 'gif',
                       # generate a random id
                       'id': str(hex(getrandbits(64))[2:]),
                       'title': 'Title',
                       'gif_url': 'http://66.media.tumblr.com/e66a2bd899987ded265aa57352f566a3/tumblr_mqfbcij4QK1sbjbn3o1_400.gif',
                       'thumb_url': 'http://66.media.tumblr.com/e66a2bd899987ded265aa57352f566a3/tumblr_mqfbcij4QK1sbjbn3o1_400.gif',
                       }
                      ]
            return result

        self.answerer.answer(msg, compute_answer)

    def on_chosen_inline_result(self, msg):
        # look that on_inline_query already answers, so no magic here
        self.sender.sendMessage(msg['query'])


def main():
    config = resource_filename(__name__, 'configs.yaml')
    config = yaml.load(open(config).read())
    bot = telepot.DelegatorBot(config['token'], [
        (per_inline_from_id(), create_open(NoSpoiler, timeout=30)),
        (per_chat_id(), create_open(NoSpoiler, timeout=2)),
    ])
    bot.message_loop(run_forever='Running ...')


def test():
    config = resource_filename(__name__, 'configs.yaml')
    config = yaml.load(open(config).read())
    print(config['token'])

if __name__ == '__main__':
    main()
