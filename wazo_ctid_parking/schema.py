# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from marshmallow import (
    fields,
    Schema,
)
from marshmallow.validate import Length

from xivo_ctid_ng.helpers.mallow import StrictDict


class ParkingListSchema(Schema):
    name = fields.Str(validate=Length(min=1))
    start_space = fields.Integer()
    stop_space = fields.Integer()
    timeout = fields.Integer()

    class Meta:
        strict = True


class ParkSchema(Schema):
    parking_name = fields.Str(validate=Length(min=1))
    channel = fields.Str()
    announce_channel = fields.Str()
    timeout = fields.Integer()
    timeout_channel = fields.Integer()


parking_list_schema = ParkingListSchema()
park_schema = ParkSchema()
