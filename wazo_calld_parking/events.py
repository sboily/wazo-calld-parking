# Copyright 2016-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_bus.resources.common.event import TenantEvent


class ParkedCallEvent(TenantEvent):
    service = 'calld'
    name = 'parking_parked_call'
    routing_key_fmt = 'calls.parking.parked_call'
    required_acl_fmt = 'events.calls.me'

    def __init__(self, content, tenant_uuid):
        super().__init__(content, tenant_uuid)

class UnParkedCallEvent(TenantEvent):
    service = 'calld'
    name = 'parking_unparked_call'
    routing_key_fmt = 'calls.parking.unparked_call'
    required_acl_fmt = 'events.calls.me'

    def __init__(self, content, tenant_uuid):
        super().__init__(content, tenant_uuid)


class ParkedCallGiveUpEvent(TenantEvent):
    service = 'calld'
    name = 'parking_parked_call_give_up'
    routing_key_fmt = 'calls.parking.parked_call_give_up'
    required_acl_fmt = 'events.calls.me'

    def __init__(self, content, tenant_uuid):
        super().__init__(content, tenant_uuid)


class ParkedCallSwapEvent(TenantEvent):
    service = 'calld'
    name = 'parking_parked_call_swap'
    routing_key_fmt = 'calls.parking.parked_call_swap'
    required_acl_fmt = 'events.calls.me'

    def __init__(self, content, tenant_uuid):
        super().__init__(content, tenant_uuid)


class ParkedCallTimeoutEvent(TenantEvent):
    service = 'calld'
    name = 'parking_parked_call_timeout'
    routing_key_fmt = 'calls.parking.parked_call_timeout'
    required_acl_fmt = 'events.calls.me'

    def __init__(self, content, tenant_uuid):
        super().__init__(content, tenant_uuid)
