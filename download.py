#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : download.py
# Author            : Amar Lakshya <amar.lakshya@protonmail.com>
# Date              : 30.07.2020
# Last Modified Date: 31.07.2020
# Last Modified By  : Amar Lakshya <amar.lakshya@protonmail.com>
import wikipediaapi
def print_section(prefix, data):
    for line in data.splitlines():
        print("%s,%s" % (prefix,line))

def print_sections(prefix, data, level=0):
    for lines in data:
        for line in lines.text.splitlines():
            print("%s,%s" % (prefix, line))
            print_sections(prefix, lines.sections, level + 1)

def print_pretty(data, section, level=0):
    prefix = data.title
    secData = data.section_by_title(section)
    subsections = len(secData.sections)
    if subsections >= 1:
        print_sections(prefix, secData.sections)
    else:
        print_section(prefix, secData.text)


get = wikipediaapi.Wikipedia('en')

page = get.page("Category:Days of the year")
section='Deaths'

for member in page.categorymembers:
    result = get.page(member)
    print_pretty(result, section)

