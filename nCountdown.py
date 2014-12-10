##############################################################
# nCountdown - Simple app to run a countdown in chat in case
# you're looking to race or drag or something in a practice
# session. lol
#
# The MIT License (MIT)
#
# Copyright (c) 2014 Anthony Goins
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#############################################################

import ac
import acsys
import functools

appWindow = None
nButton = None
countdown = 0
passes = 0


class nCountdown:
    def __init__(self, app):
        global appWindow

        appWindow = app

        self.button = ac.addButton(appWindow, 'Start Countdown')
        self.btnEvent = functools.partial(self.onClick, msg='Countdown started')

        ac.setPosition(self.button, 1, 35)
        ac.setSize(self.button, 175, 25)

        ac.addOnClickedListener(self.button, self.btnEvent)

    def onClick(self, x, y, msg):
        global countdown
        countdown = 5


def acMain(ac_version):
    global appWindow

    appWindow = ac.newApp("nCountdown")
    ac.setSize(appWindow, 177, 60)
    nButton = nCountdown(appWindow)

    return "nCountdown"


def acUpdate(deltaT):
    global countdown, passes

    if passes < 150:
        passes += 1
    else:
        updateCountdown(countdown)
        passes = 0


def updateCountdown(count):
    global countdown

    if count == 5:
        countdown = 4
        ac.sendChatMessage('Get ready...')
    elif count == 4:
        countdown = 3
        ac.sendChatMessage('3')
    elif count == 3:
        countdown = 2
        ac.sendChatMessage('2')
    elif count == 2:
        countdown = 1
        ac.sendChatMessage('1')
    elif count == 1:
        countdown = 0
        ac.sendChatMessage('GO!')
    else:
        countdown = 0
