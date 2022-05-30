from allauth.account.adapter import DefaultAccountAdapter
import threading


class BackgroundEmailSendingAccountAdapter(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        mailing_thread = threading.Thread(
            target=super(BackgroundEmailSendingAccountAdapter, self).send_mail,
            args=(template_prefix, email, context)
        )
        mailing_thread.start()
