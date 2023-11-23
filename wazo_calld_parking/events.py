# Copyright 2016-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_bus.resources.common.event import TenantEvent


class ParkedCallEvent(UserEvent):
    service = 'calld'
    name = 'parking_parked_call'
    routing_key_fmt = 'calls.parking.parked_call'
    required_acl_fmt = 'events.calls.parking.parked_call'

    def __init__(self, content, tenant_uuid):
        super().__init__(content, tenant_uuid)

class UnParkedCallEvent(UserEvent):
    service = 'calld'
    name = 'parking_unparked_call'
    routing_key_fmt = 'calls.parking.unparked_call'
    required_acl_fmt = 'events.calls.parking.unparked_call'

    def __init__(self, content, tenant_uuid):
        super().__init__(content, tenant_uuid)


class ParkedCallGiveUpEvent(UserEvent):
    service = 'calld'
    name = 'parking_parked_call_give_up'
    routing_key_fmt = 'calls.parking.parked_call_give_up'
    required_acl_fmt = 'events.calls.parking.parked_call_give_up'

    def __init__(self, content, tenant_uuid):
        super().__init__(content, tenant_uuid)


class ParkedCallSwapEvent(UserEvent):
    service = 'calld'
    name = 'parking_parked_call_swap'
    routing_key_fmt = 'calls.parking.parked_call_swap'
    required_acl_fmt = 'events.calls.parking.parked_call_swap'

    def __init__(self, content, tenant_uuid):
        super().__init__(content, tenant_uuid)


class ParkedCallTimeoutEvent(UserEvent):
    service = 'calld'
    name = 'parking_parked_call_timeout'
    routing_key_fmt = 'calls.parking.parked_call_timeout'
    required_acl_fmt = 'events.calls.parking.parked_call_timeout'

    def __init__(self, content, tenant_uuid):
        super().__init__(content, tenant_uuid)
