# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from rocketmq.client import PushConsumer, ConsumeStatus
import time
import sys
topic = 'tigerweili-topic-01'
consumer_group_name = 'tigerweili-producer-group-01'
name_srv = '127.0.0.1:9876'


def callback(msg):
    print('consuming message', msg.id, msg.body,  msg.get_property('property'))
    return ConsumeStatus.CONSUME_SUCCESS

def start_consume_message():
    consumer = PushConsumer(consumer_group_name)
    consumer.set_name_server_address(name_srv)
    consumer.subscribe(topic, callback)
    print ('start consume message')
    consumer.start()

    while True:
        time.sleep(3600)

if __name__ == '__main__':
    if len(sys.argv) > 0:
        name_srv = sys.argv[1]
        
    start_consume_message()
