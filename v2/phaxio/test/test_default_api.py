# coding: utf-8

"""
    Phaxio API

    Simple Rest Echo

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest
import urllib3
import requests

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """ DefaultApi unit test stubs """

    def setUp(self):
        swagger_client.configuration.username = os.getenv('API_KEY')
        swagger_client.configuration.password = os.getenv('API_SECRET')
        client = swagger_client.ApiClient()
        #client.set_default_header(header_name='Authorization', header_value=self.config.get_basic_auth_token())
        self.api = swagger_client.apis.default_api.DefaultApi()

    def tearDown(self):
        pass

    def test_get_fax(self):
        result = self.api.faxes_fax_id_get(36467415)
        print('type={}, result={}'.format(type(result), result))

    #def test_get_account_status(self):
    #    result = self.api.account_status_get()
    #    print(result)

    def test_send_fax(self):
        result = self.api.faxes_post(to='7735922266', file=['/mnt/d/src/pyphaxio/v2/phaxio/requirements.txt'])
        print('type={}, result={}'.format(type(result), result))


    def test_raw_request(self):
        http = urllib3.PoolManager()

        post_params=[('to', '7735922266'), ('content_url', 'http://www.google.com'), ('file', ('requirements.txt', 'certifi >= 14.05.14\nsix == 1.8.0\npython_dateutil >= 2.5.3\nsetuptools >= 21.0.0\nurllib3 >= 1.19.1\nrequests >= 2.12\n', 'text/plain'))]
        req_params=[('to', '7735922266')] #, ('content_url[]', ['http://www.google.com', 'http://www.bing.com'])]

        files=[
            ('file', ('requirements.txt', 'certifi >= 14.05.14\nsix == 1.8.0\npython_dateutil >= 2.5.3\nsetuptools >= 21.0.0\nurllib3 >= 1.15.1\n', 'text/plain'))
        ]
        #files=[
        #    ('file[]', ('requirements.txt', open('/mnt/d/src/pyphaxio/generated/requirements.txt', 'rb'))),
        #]


        # DEF WORKS
        #files = [
        #    ('file[]', ('requirements.txt', open('/mnt/d/src/pyphaxio/generated/requirements.txt', 'rb'))),
        #    ('file[]', ('bar.png', open('/mnt/d/src/pyphaxio/generated/tox.ini', 'rb')))]
        header={'Authorization': u'Basic ODJjYTkxY2ZjMWNlMjZhMWJkZGFjMjkxYWM4YzYwZjgxYmJmMmYwYTowNjUzNTUyNmJlNjIwMmMxYjQ5ODJjZTcwYzA4ZDc4OGRhZjRhMzQw', 'Accept': 'application/json', 'User-Agent': 'Swagger-Codegen/1.0.0/python'}

        r = requests.post('https://api.phaxio.com/v2/faxes?direction=received', data=req_params, files=files, headers=header)
        #r = http.request('POST', 'https://api.phaxio.com/v2/faxes',
        #                              fields=post_params,
        #                              encode_multipart=True,
        #                              headers=header)
        print('response={}'.format(r.text))
        print('request.headers={}'.format(r.request.headers))
        print('request.body={}'.format(r.request.body))


    def test_get_fax_data(self):
        result = self.api.faxes_fax_id_file_get(36394889, thumbnail="s")
        print('type={}, result={}'.format(type(result), result))

    def test_get_faxes(self):
        result = self.api.faxes_get(phone_number='+17735922266', per_page=10, page=2, status='success',
                                    created_before='2016-12-24T01:49:22.000')
        print('type={}, result={}'.format(type(result), result))

    def test_delete_fax(self):
        result = self.api.faxes_fax_id_delete(36394889)
        print('type={}, result={}'.format(type(result), result))

    def test_delete_fax_file(self):
        result = self.api.faxes_fax_id_file_delete(36507493)
        print('type={}, result={}'.format(type(result), result))

    def test_cancel_fax(self):
        try:
            result = self.api.faxes_fax_id_cancel_post(36394889)
            print('type={}, result={}'.format(type(result), result))
        except ApiException as e:
            print('[type={}, result={}]'.format(type(e), e))
            raise e

    def test_get_countries(self):
        swagger_client.configuration.username = ""
        swagger_client.configuration.password = ""
        result = self.api.public_countries_get(per_page=10, page=1)
        print('type={}, result={}'.format(type(result), result))

    #def test_resend_fax(self):
    #    #try:
    #    result = self.api.faxes_fax_id_resend_post(36394889)
    #    print('type={}, result={}'.format(type(result), result))
        #except ApiException as e:
        #print('[type={}, result={}]'.format(type(e), e))
        #    raise e

if __name__ == '__main__':
    unittest.main()
