"""
Copyright (C) 2012 Mattias Ugelvik

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from settings import settings
import time
import webbrowser
import os

def nice_print(args):
    if not settings['log-to-console']:
        return
    base = time.strftime("%H:%M:%S: ")
    for arg in args:
        base += '{0:<33}'.format(arg)
    print base

def open_help_in_browser():
    abs_path = os.path.abspath('.') #Absolute path of current working directory
    filename = os.path.join(abs_path,"help", 'help.html')
    nice_print('Trying to open ' + filename)
    webbrowser.open(filename)
