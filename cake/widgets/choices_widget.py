from import_export.widgets import Widget


class ChoicesWidget(Widget):
    def __init__(self, choices, *args, **kwargs):
        self.choices = dict(choices)
        self.revert_choices = dict((v, k) for k, v in self.choices.items())

    def clean(self, value, row=None, *args, **kwargs):
        return self.revert_choices.get(value, value) if value else None

    def render(self, value, obj=None):
        return self.choices.get(value, '')