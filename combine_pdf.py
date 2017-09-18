#!/usr/bin/python3

import os
filename = 'KY1703'

os.system("gs -q -sPAPERSIZE=a4 -dNOPAUSE -dBATCH -sDEVICE=pdfwrite"
" -sOutputFile=" + filename + "_Permit_Application.pdf "
+ filename + "_form.pdf "
+ filename + "_map_1.pdf "
+ filename + "_map_2.pdf "
+ filename + "_microtrench.pdf "
+ filename + "_traffic1.pdf "
+ filename + "_traffic2.pdf")
