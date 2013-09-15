'''
Created on 15.09.2013

@author: Marco Hoyer
'''
import unittest
import check_http_yaml


class Test(unittest.TestCase):


    def test_construct_url(self):
        self.assertEqual(check_http_yaml.construct_url("testhost", 9000, "/icinga-status", "query=STATUSFILEAGETT"),"http://testhost:9000/icinga-status?query=STATUSFILEAGETT")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()