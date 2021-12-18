# Copyright (c) 2021 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from korth_spirit import Instance, EventEnum
from korth_spirit.coords import Coordinates
from korth_spirit.sdk import aw_wait

with Instance(name="Portal Mage") as bot:
    try:
        (
            bot
                .login(
                    citizen_number=(int(input("Citizen Number: "))),
                    password=input("Password: ")
                )
                .subscribe(
                    EventEnum.AW_EVENT_AVATAR_ADD,
                    lambda e: bot.say(f"Salutations {e.avatar_name}!")
                )
                .enter_world(input("World: "))
                .move_to(Coordinates(0, 0, 0))
        )
    except Exception as e:
        print("An error occurred:", e)
        exit()

    while True:
        aw_wait(1)
