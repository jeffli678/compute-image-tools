#!/usr/bin/env python2
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import debian


class UbuntuTests(debian.DebianTests):
  def GetGoogleAptSource(self):
    return 'gce.archive.ubuntu.com'

  def GetSshdConfig(self):
    # They know what they are doing. No need to check for PermitRootLogin
    return {
        'PasswordAuthentication': 'no',
    }

  def GetCmdlineConfigs(self):
    # Analysing if {'console': ['ttyS0', '38400n8'],} should be here or not.
    # Because it fails!
    return {
        'scsi_mod.use_blk_mq': ['Y'],
    }
