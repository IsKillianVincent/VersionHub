from django.db.models import QuerySet

class UserAgreementQuerySet(QuerySet):
    def for_user(self, user):
        return self.filter(user=user)

    def latest_for_user(self, user):
        return self.for_user(user).order_by('-accepted_at').first()