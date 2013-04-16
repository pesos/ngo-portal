
import account.views

import seva.forms


class SignupView(account.views.SignupView):

   form_class = seva.forms.SignupForm

   def after_signup(self, form):
       self.create_profile(form)
       super(SignupView, self).after_signup(form)

   def create_profile(self, form):
       profile = self.created_user.get_profile()
       profile.birthdate = form.cleaned_data["birthdate"]
       profile.save()