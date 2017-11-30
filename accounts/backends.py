#   File checks if email and password are correct
#   If not Login will not be allowed
#   Can also be customised to check for other properties in stead
#   Default is username and password

from models import User     #   custom User

class EmailAuth(object):
    #   FUNCTION saves the user and then returns it
    def authenticate(self, email=None, password=None):
        """
        Get an instance of USER using the supplied email
        Then check its password before returning
        :param email:
        :param password:
        :return: user
        """
        try:
            #   Retrieve User based on email address
            user = User.objects.get(email=email)
            #   Return user if password is correct
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Used by Django authentication system to retrieve an instance of User based on USER_ID
        :param user_id:
        :return:
        """
        try:
            user = User.objects.get(pk=user_id)
            #   CHECK WHETHER THE USER IS ACTIVE
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None



