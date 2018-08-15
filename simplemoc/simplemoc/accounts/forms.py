from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

#campos do formulario de redefinir senha
class PasswordResetForm(forms.Form):

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data('email')
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Nenhum usuário encontrado com este e-mail')

#campos do formulário registrar usuário no sistema
class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmação de Senha', widget=forms.PasswordInput
    )
    # campo do formulário que confirmará se o password2 está correto
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação não está correta')
        return password2
    # função que salvará o usuário no sistema
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
    #campos que seram retornados para o usuário
    class Meta:
        model = User
        fields = ['username', 'email']

#campos para editar os dados do usuário
class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name']