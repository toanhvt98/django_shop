from django import forms


class LoginForm(forms.Form):
    label_suffix = ""
    username = forms.CharField(
        label="Your username",
        widget=forms.TextInput(
            attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "Enter your username",
                "id":"login_usernameInput",
                
            }
        ),
        required=True
    )
    password = forms.CharField(
        label="Your password",
        widget=forms.PasswordInput(
            attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "**********",
                "id":"login_passwordInput",
            }
        ),
        required=True
    )
    remember_me = forms.BooleanField(
        label="Remember Me",
        widget=forms.CheckboxInput(
            attrs={
                "class":"w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-600 dark:border-gray-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800",
                "id":"login_remembercheckbox",
            }
        ), 
        required=False
    )
class RegisterForm(forms.Form):
    label_suffix = ""
    username = forms.CharField(
        label="Your username",
        widget=forms.TextInput(
            attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "Enter username",
                "id":"register_usernameInput",
                
            }
        ),
        required=True
    )
    password = forms.CharField(
        label="Your password",
        widget=forms.PasswordInput(
            attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "**********",
                "id":"register_passwordInput",
            }
        ),
        required=True
    )
    re_password = forms.CharField(
        label="Re-type your password",
        widget=forms.PasswordInput(
            attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "**********",
                "id":"register_repasswordInput",
            }
        ),
        required=True
    )
   