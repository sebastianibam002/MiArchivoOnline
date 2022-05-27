from django import forms
  
class FileForm(forms.Form):
    user_email = forms.EmailField(label="Tu correo")
    send_email = forms.EmailField(label="Correo Destinatario")
    note = forms.CharField(label="Mensaje")
    file = forms.FileField(label="Archivo")
    

