#!/usr/bin/python

import time
import datetime
import pdb
import requests

def main():
	ts = time.time()
	print ts
	
	r = requests.get("http://www.google.fr")
	print r.encoding
	
if __name__ == '__main__':
    main()
