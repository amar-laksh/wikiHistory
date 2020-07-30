#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : wiki.py
# Author            : Amar Lakshya <amar.lakshya@protonmail.com>
# Date              : 30.07.2020
# Last Modified Date: 30.07.2020
# Last Modified By  : Amar Lakshya <amar.lakshya@protonmail.com>
import wikipediaapi
def print_categories(page):
    categories = page.categories
    for title in sorted(categories.keys()):
        print("%s: %s" % (title, categories[title]))

def print_categorymembers(categorymembers, level=0, max_level=1):
    for c in categorymembers.values():
        print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)

def print_sections(data, sections, level=0):
    for s in sections:
        for line in s.text.splitlines():
            print("%s,%s" % (data, line))
        print_sections(data, s.sections, level + 1)

def print_section(data, section):
    for line in section.splitlines():
        print("%s,%s" % (data, line))

wiki_wiki = wikipediaapi.Wikipedia('en')
cat = wiki_wiki.page("Category:Days of the year")
section='Deaths'
for date in cat.categorymembers:
    page_py = wiki_wiki.page(date)
    if(len(page_py.section_by_title(section).sections) >= 1):
        print_sections(date, page_py.section_by_title(section).sections)
    else:
        print_section(date, page_py.section_by_title(section).text)
