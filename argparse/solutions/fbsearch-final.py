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

parser = argparse.ArgumentParser(description='return scientific names for common name')
parser.add_argument('common_name',
                    help='serch will be preformed for common name (default is exact match only)')
parser.add_argument('-f', '--fuzzy', action='store_true', help='perform search using taxamatch')
parser.add_argument('-v', '--verbose', action='store_true', help='print verbose output')
args = parser.parse_args()
# The FishBase search url
result_url = 'http://fishbase.se/ComNames/CommonNameSearchList.php'
# The common name we are serching on
common_name = args.common_name
scientific_names = []
query = {'CommonName' : common_name}
if args.fuzzy:
    result_url = 'http://fishbase.se/NoRecordForCommonName.php'
    query['crit1_operator'] = 'EQUAL'
query_string = '?' + urllib.urlencode(query)
# Keep checking for the next link, when it no longer appers in the results we have
# them all
while True:
    # Concatenate parts of the url together and have open the url
    full_url = result_url + query_string
    if args.verbose:
        print "Fetching " + full_url
    soup = BeautifulSoup(urllib2.urlopen(full_url))
    scientific_names += page_results(soup)
    # If there is an <a href=''>Next</a> tag in the results it means we don't have all
    # the results and we should also parse additional results from the next page
    next_link = soup.find('a', text='Next')
    if next_link:
	    query_string = next_link['href']
	    if args.verbose:
	        print "Found another page of results"
    else:
        break
if args.verbose:
    print "Results"
    print "========================================"
for name in scientific_names:
    print name