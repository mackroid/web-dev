#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import funcVal

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
	<br>

	<input type="submit">
</form>
"""
class MainHandler(webapp2.RequestHandler):



    def get(self):
        self.response.write('Hello, Udacity!')
        self.write_form()

    def write_form(self, error="", month="", day="", year=""):
		self.response.write(form % {"error": error,
									"month": month,
									"day": day,
									"year": year})

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
    		self.response.write("Thanks for answering")

    


# class TestHandler(webapp2.RequestHandler):
#     def post(self):
#         #q = self.request.get("q")
#         #self.response.write(q)

#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
   # ('/testform', TestHandler)
], debug=True)


