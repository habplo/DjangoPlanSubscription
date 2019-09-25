from .models import notes
from plans.validators import ModelCountValidator


class MaxNotesValidator(ModelCountValidator):
    code = 'MAX_NOTES_COUNT'
    model = notes

    def get_queryset(self, user):
        return super(MaxNotesValidator, self).get_queryset(user).filter(user=user)


max_notes_validator = MaxNotesValidator()