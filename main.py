#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import funcVal
import esc_html
import rot13

form="""
<form method="post">
	What is your birthday?
	<br>

	<label>Month
		<input type="text" name="month" value="%(month)s">
	</label>
	
	<label>Day
	<input type="text" name="day" value="%(day)s">
	</label>

	<label>Year
	<input type="text" name="year" value="%(year)s">
	</label>
	<div style="color: red">%(error)s</div>

	<br>

	<input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):

    def get(self):
        #self.response.write('Hello, Udacity!')
        self.write_form()

    def write_form(self, error="", month="", day="", year=""):
		self.response.write(form % {"error": error,
									"month": esc_html.escape_html(month),
									"day": esc_html.escape_html(day),
									"year": esc_html.escape_html(year)})

    def post(self):
    	user_month = self.request.get('month')
    	user_day = self.request.get('day')
    	user_year = self.request.get('year')

    	month = funcVal.valid_month(user_month)
    	day = funcVal.valid_day(user_day)
    	year = funcVal.valid_year(user_year)
    	
    	if not (month and day and year):
    		self.write_form("Not valid input!", user_month, user_day, user_year)
    	else:
    		self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
	
	def get(self):
		self.response.write("Thanks for answering")


rotForm="""
<h1>Encrypt your text</h1>

<form method="post">
	<textarea name="text" style="height: 140px; width: 440px;">%s</textarea>
	<br>
	<input type="submit">
"""	

class Rot13Handler(webapp2.RequestHandler):

	def get(self):
		#self.response.write(rotForm.replace("%s", ""))
		self.write_form()

	def write_form(self, text=""):
		self.response.write(rotForm % text)

	def post(self):
		user_text = self.request.get('text')
		user_text = rot13.rot(user_text)
		self.write_form(user_text)


signUpForm="""
<h1>Sign up here</h1>
<br>

	<style type="text/css">

		label {
			width: 250px;
			display: inline-block;
			text-align: right;


	</style>

<form method="post">
		

	<label>Username
	<input type="text" name="username" value="%(username)s">
	<div style="color: red">%(error_username)s</div>
	</label>

	<br>
	<label>Password
	<input type="password" name="password" value="">
	<div style="color: red">%(error_password)s</div>
	</label>
	
	<br>
	<label>Verify Password
	<input type="password" name="verify" value="">
	<div style="color: red">%(error_verify)s</div>
	</label>

	<br>
	<label>Email (optional)
	<input type="text" name="email" value="%(email)s">
	<div style="color: red">%(error_email)s</div>
	</label>

	<br>
	<br>
	<input type="submit">

"""

class SignUpHandler(webapp2.RequestHandler):

	def get(self):
		self.write_form()

	def write_form(self, error_username="", error_password="", error_verify="",
				   error_email="", username="", email=""):
		self.response.write(signUpForm % {"error_username" : error_username,
										  "error_password" : error_password,
										  "error_verify" : error_verify,
										  "error_email" : error_email,
										  "username" : esc_html.escape_html(username),
										  "email" : esc_html.escape_html(email)})

	def post(self):
		username = self.request.get('username')
		username_valid = funcVal.valid_username(username)
		if not username_valid:
			error_username = "That's not a valid username."
		else:
			error_username = ""	

		password = self.request.get('password')
		password_valid = funcVal.valid_password(password)
		verify = self.request.get('verify')
		password_match = password == verify
		if not password_valid:
			error_password = "That wasn't a valid password-"
			error_verify = ""
		elif not password_match:
			error_password = ""
			error_verify = "Your passwords didn't match."
		else:
			error_password = ""
			error_verify = ""

		email = self.request.get('email')
		if not email:
			email_valid = True
		else:
			email_valid = funcVal.valid_email(email)

		if not email_valid:
			error_email = "That's not a valid email."
		else:
			error_email = ""



		if all([username_valid, password_valid, password_match, email_valid]):
			self.redirect('/welcome' + '?username=%s' % username)
		else:
			self.write_form(error_username, error_password, error_verify, error_email, username, email)


class WelcomeHandler(webapp2.RequestHandler):

	def get(self):
		username = self.request.get('username')
		self.response.write("Welcome, " + username + "!")


# class TestHandler(webapp2.RequestHandler):
#     def post(self):
#         #q = self.request.get("q")
#         #self.response.write(q)

#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler),
    ('/unit2/rot13', Rot13Handler),
    ('/unit2/signup', SignUpHandler),
    ('/welcome', WelcomeHandler),
    ])