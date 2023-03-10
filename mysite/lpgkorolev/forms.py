from django import forms
from .models import *
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re


# phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Телефон должен быть введен в "
#                                                                "формате: +7(999)999-99-99")
# phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'specialist', 'first_name', 'last_name', 'phone_number', 'fact_date']
        widgets = {
            'service': forms.Select(attrs={"class": "form-select bg-light border-0", "style": "height: 55px;"}),

            'specialist': forms.Select(attrs={"class": "form-select bg-light border-0", "style": "height: 55px;"}),

            'first_name': forms.TextInput(attrs={"type": "text", "class": "form-control bg-light border-0",
                                                 "placeholder": "Ваше имя", "style": "height: 55px;"}),

            'last_name': forms.TextInput(attrs={"type": "text", "class": "form-control bg-light border-0",
                                                "placeholder": "Ваше фамилия", "style": "height: 55px;"}),

            'phone_number': forms.TextInput(attrs={"class": "form-control bg-light border-0",
                                                   "placeholder": "Ваш номер телефона", "style": "height: 55px;"}),

            'fact_date': forms.DateTimeInput(attrs={"type": "text",
                                                    "class": "form-control bg-light border-0 datetimepicker-input",
                                                    "placeholder": "Дата и время записи",
                                                    "data-target": "#datetimepicker2",
                                                    "style": "height: 55px;"}),

        }

    # def clean_first_name(self):
    #     first_name = self.cleaned_data['first_name']
    #     if re.match(r'\d', first_name):
    #         raise ValidationError('Данное поле не может начинаться с цифры')
    #     return first_name
    #
    # def clean_last_name(self):
    #     last_name = self.cleaned_data['last_name']
    #     if re.match(r'\d', last_name):
    #         raise ValidationError('Данное поле не может начинаться с цифры')
    #     return last_name


