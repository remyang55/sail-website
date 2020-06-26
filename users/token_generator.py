from django.contrib.auth.tokens import PasswordResetTokenGenerator

""" Generates a one-time use token that is appended to the activation link users receive in their email when signin up """
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_active)

account_activation_token = TokenGenerator()
