# Copyright (c) 2016 OpenStack Foundation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from oslo_config import cfg

from dragonflow._i18n import _

df_active_port_detection_opts = [
    cfg.IntOpt('detection_interval_time',
               default=30,
               help=_("Interval time of sending detection arp packets."))
]


def register_opts():
    cfg.CONF.register_opts(df_active_port_detection_opts,
                           group='df_active_port_detection')


def list_opts():
    return {'df_active_port_detection': df_active_port_detection_opts}
