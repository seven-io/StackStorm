from sms77api.Sms77api import Sms77api

from st2common.runners.base_action import Action


class Sms77SendSMSAction(Action):
    def __init__(self, config=None, action_service=None):
        super(Sms77SendSMSAction, self).__init__(config, action_service)
        self.client = Sms77api(self.config['api_key'])

    def run(self, to, text, **kwargs):
        try:
            self.client.sms(to, text, kwargs)
        except Exception as e:
            error_msg = ('Failed sending sms to: %s, exception: %s\n' % (to, str(e)))
            self.logger.error(error_msg)
            raise Exception(error_msg)

        self.logger.info('Successfully sent sms to: %s\n' % to)
