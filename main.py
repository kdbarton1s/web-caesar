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
import caesar
import cgi

header = """
    <header>
        <h1>Caesar Cipher</h1>
    </header>
"""
def build_page(textarea_content):
    rotation_label = "<label>Rotation Amount</label>"
    message_label = "<label>Enter a message</label>"
    textArea = "<textarea name='message'>" + textarea_content + "</textarea>"
    rotation_input = "<input type='number' name='rotation'/>"
    submit = "<input type='submit'/>"
    form = "<form method='post'>" + rotation_label + rotation_input + "<br>" + message_label + textArea + "<br>" + submit + "</form>"
    return header + form


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):

        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message, rotation)
        encrypted_message_escaped = cgi.escape(encrypted_message)
        content = build_page(encrypted_message_escaped)
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
