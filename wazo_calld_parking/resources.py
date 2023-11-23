# Copyright 2018-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from flask import request
from xivo.tenant_flask_helpers import Tenant

from wazo_calld.auth import required_acl
from wazo_calld.http import AuthResource

from .schema import (
    parking_list_schema,
    park_schema,
)


class ParkingListResource(AuthResource):

    def __init__(self, parking_service):
        self._parking_service = parking_service

    @required_acl('calld.users.me.parking.read')
    def get(self):
        tenant = Tenant.autodetect()
        parking_list = self._parking_service.list_parking(tenant.uuid)

        return parking_list, 200


class ParkingResource(AuthResource):

    def __init__(self, parking_service):
        self._parking_service = parking_service

    @required_acl('calld.users.me.parking.{parking_name}.read')
    def get(self, parking_name):
        tenant = Tenant.autodetect()
        parking = self._parking_service.get_parked_calls(parking_name, tenant.uuid)

        return parking, 200

    @required_acl('calld.users.me.parking.{parking_name}.park.create')
    def post(self, parking_name):
        tenant = Tenant.autodetect()
        request_body = park_schema.load(request.get_json(force=True))
        result = self._parking_service.park_call(parking_name, request_body, tenant.uuid)

        return result, 201
