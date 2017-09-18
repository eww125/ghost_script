#!/usr/bin/python3

import os

number_of_pages = 68
input_pdf = "abstracts_rev09.pdf"

for i in range(1, number_of_pages +1):
    os.system("gs -q -dBATCH -dNOPAUSE -sOutputFile=page{page:04d}.pdf"
              " -dFirstPage={page} -dLastPage={page}"
              " -sDEVICE=pdfwrite {input_pdf}"
              .format(page=i, input_pdf=input_pdf))
