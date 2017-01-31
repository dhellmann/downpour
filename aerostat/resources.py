# -*- coding: utf-8 -*-

# Copyright 2010-2011 OpenStack Foundation
# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import munch


def load(filename):
    "Read the file and return the parsed data in a consistent format."

    # Ensure the return value has a basic set of keys representing the
    # types of resources we expect to find.
    to_return = munch.Munch(
        servers=[],
        volumes=[],
        images=[],
    )

    with open(filename, 'r', encoding='utf-8') as fd:
        contents = munch.Munch.fromYAML(fd.read())
    to_return.update(contents)

    # Ensure all entries have consistent sets of keys so the rest of
    # the app doesn't have to check every time it wants to use a
    # value.
    for s in to_return.servers:
        if 'save_state' not in s:
            s['save_state'] = True
    for s in to_return.volumes:
        if 'save_state' not in s:
            s['save_state'] = True

    return to_return