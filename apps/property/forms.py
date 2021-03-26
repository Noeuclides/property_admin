from django import forms
from apps.property.models import Company, Property


class PropertyRegisterForm(forms.ModelForm):

    class Meta:
        model = Property
        exclude = ['owner', '_delete']

    def __init__(self, *args, **kwargs):
        super(PropertyRegisterForm, self).__init__(*args, **kwargs)
        # self.fields['type'].initial = None
        for visible in self.visible_fields():
            print(visible.field)
            print(visible.field.initial)
            if hasattr(visible.field.widget, 'input_type'):
                visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        """
        valida la cantidad de ods seleccionadas
        """
        cleaned_data = super(PropertyRegisterForm, self).clean()
        if type == 1:
            # urbano
            street = cleaned_data.get('street')
            street_number = cleaned_data.get('street_number')
            corner = cleaned_data.get('corner')
            corner_number = cleaned_data.get('corner_number')
            address = [street, street_number, corner, corner_number]
            if not all(address):
                raise forms.ValidationError(
                    "Por favor ingresar dirección de predio urbano."
                )
        if type == 2:
            # rural
            if not cleaned_data.get('rural'):
                raise forms.ValidationError(
                    "Por favor poner el nombre del predio rural."
                )

        return cleaned_data


class CompanyRegisterForm(forms.ModelForm):

    class Meta:
        model = Company
        exclude = ['associate']

    def __init__(self, *args, **kwargs):
        super(CompanyRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if hasattr(visible.field.widget, 'input_type'):
                if visible.field.widget.input_type == 'text':
                    visible.field.widget.attrs['class'] = 'form-control'