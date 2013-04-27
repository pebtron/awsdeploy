#!/usr/bin/env python

import os
 
print "Content-type: text/html"
print
print "<html><body>"
print "<h1>" + os.uname()[1] + "</h1>"
print "</body></html>"
