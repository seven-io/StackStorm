from sms77api.Sms77api import Sms77api
from sms77api.classes.Lookup import LookupType

from st2common.runners.base_action import Action


class SevenLookupCnamAction(Action):
    def __init__(self, config=None, action_service=None):
        super(SevenLookupCnamAction, self).__init__(config, action_service)
        self.client = Sms77api(self.config['api_key'], 'StackStorm')

    def run(self, number):
        def on_error(ex):
            err = ('Failed looking up CNAM for: %s, exception: %s\n' % (number, str(ex)))
            self.logger.error(err)
            raise Exception(err)

        try:
            return self.client.lookup(LookupType.CNAM, number)

        except Exception as e:
            on_error(e)
