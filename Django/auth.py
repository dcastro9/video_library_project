from openid.consumer.consumer import SUCCESS
from django.contrib.auth.models import User
from django.core.mail import mail_admins

class GoogleBackend:
    def authenticate(self, openid_response):
        if openid_response is None:
            return None
        if openid_response.status != SUCCESS:
            return None

        google_email = openid_response.getSigned('http://openid.net/srv/ax/1.0',  'value.email')
        google_firstname = openid_response.getSigned('http://openid.net/srv/ax/1.0', 'value.firstname')
        google_lastname = openid_response.getSigned('http://openid.net/srv/ax/1.0', 'value.lastname')
        try:
            #user = User.objects.get(username=google_email)
            # Make sure that the e-mail is unique.
            user = User.objects.get(email=google_email)
        except User.DoesNotExist:
            # Create the user.
            user = User.objects.create_user(google_email, google_email, 'password')
            user.save()

            # Create default segmentation options for the user.
            user = User.objects.get(username=google_email)
            return user
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None