#!/usr/bin/python
#-*- coding:utf-8 -*- 
'''
Author: Wangshuqin
Data: 2019-09-07 15:22:22
Last Modified time: 2019-09-07 15:22:22
Description: Using BISQUE to convert RefSeq Transcript ID(NM_) to Ensembl Transcript ID(ENST).
            BISQUE,a human genomic, transcriptomic, and proteomic conversion tool.
'''

import requests
from multiprocessing.dummy import Pool
from requests.exceptions import RequestException

pool = Pool(processes=20)


def convert_nm_to_enst(name):
     while 1:
        params = {
                'id': name,
                'output': 'enst'
            }
        try:
            r = requests.get('http://bisque.yulab.org/cgi-bin/run.cgi', params=params)
            return '|'.join([enst['output_identifier'] for enst in r.json()])  # if one nm have multi enst, separated it by '|' 
        except ValueError:  # if can't find enst write 'NA'
            return 'NA'
        except RequestException:
            continue
        except Exception:
            return 'Error'


def convert_uniprot_to_enst(name):
     while 1:
        params = {
                'id': name,
                'output': 'enst'
            }
        try:
            r = requests.get('http://bisque.yulab.org/cgi-bin/run.cgi', params=params)
            return '|'.join([enst['output_identifier'] for enst in r.json()])  # if one uniprot have multi enst, separated it by '|'
        except IndexError:
            return 'NA'
        except RequestException:
            continue
        except Exception:
            return 'Error'


if __name__ == '__main__':
    convert_nm_to_enst()
    convert_uniprot_to_enst()