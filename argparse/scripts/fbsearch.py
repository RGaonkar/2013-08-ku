#!/usr/bin/env python
"""
fbsearch.py

Created by Darren Boss on 2013-08-21.
"""
import urllib, urllib2
from bs4 import BeautifulSoup
import argparse

def page_results(soup):
    """Return a list of names
    
    Given an instance of BeautifulSoup, will return all the names it can find
    in the search result table

    """
    result_table = soup.find('table', class_='commonTable')
    if not result_table:
        result_table = soup.find('table', id='TableResult')
    if result_table:
        scientific_names = [it.text for it in result_table.find_all('i')]
        return scientific_names
    else:
        return ["No results."]
# --- Insert argpase setup here
# --- End argparse setup
# The FishBase search url
result_url = 'http://fishbase.se/ComNames/CommonNameSearchList.php'
# The common name we are serching on
# --- Create a common_name  variable = args.common_name
scientific_names = []
# --- Change the hard coded 'tuna' string to the common_name variable
query = {'CommonName' : 'tuna'}
query_string = '?' + urllib.urlencode(query)
# Keep checking for the next link, when it no longer appers in the results we have
# them all
while True:
    # Concatenate parts of the url together and have open the url
    full_url = result_url + query_string
    # --- insert if args.verbose print full_url message here
    # --- end if args.verbose
    soup = BeautifulSoup(urllib2.urlopen(full_url))
    scientific_names += page_results(soup)
    # If there is an <a href=''>Next</a> tag in the results it means we don't have all
    # the results and we should also parse additional results from the next page
    next_link = soup.find('a', text='Next')
    if next_link:
            query_string = next_link['href']
            # --- insert if arg.verbose print message saying we
            # --- found another page of results
            # --- end if arg.verbose
    else:
        break
for name in scientific_names:
    print name
