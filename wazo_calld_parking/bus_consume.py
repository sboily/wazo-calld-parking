# Copyright 2016-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from .events import (
    ParkedCallEvent,
    UnParkedCallEvent,
    ParkedCallGiveUpEvent,
    ParkedCallSwapEvent,
    ParkedCallTimeoutEvent
)


logger = logging.getLogger(__name__)


def camel_to_snake(s):
    exceptions = {
        "ParkeeCallerIDNum": "parkee_caller_id_num",
        "ParkeeCallerIDName": "parkee_caller_id_name"
    }

    if s in exceptions:
        return exceptions[s]

    snake = ""
    for char in s:
        if char.isupper():
            if snake:
                snake += "_"
            snake += char.lower()
        else:
            snake += char
    return snake

def convert_keys(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for k, v in obj.items():
            new_key = camel_to_snake(k)
            new_dict[new_key] = convert_keys(v)
        return new_dict
    elif isinstance(obj, list):
        new_list = []
        for item in obj:
            new_list.append(convert_keys(item))
        return new_list
    else:
        return obj


class ParkingBusEventHandler:

    def __init__(self, bus_publisher, confd):
        self.bus_publisher = bus_publisher
        self.confd = confd

    def subscribe(self, bus_consumer):
        bus_consumer.subscribe('ParkedCall', self._parked_call)
        bus_consumer.subscribe('UnParkedCall', self._unparked_call)
        bus_consumer.subscribe('ParkedCallGiveUp', self._parked_call_give_up)
        bus_consumer.subscribe('ParkedCallSwap', self._parked_call_swap)
        bus_consumer.subscribe('ParkedCallTimeOut', self._parked_call_timeout)

    def _parked_call(self, event):
        ev = convert_keys(event)
        tenant_uuid = self._extract_tenant_uuid(ev)
        bus_event = ParkedCallEvent(
            ev,
            tenant_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _unparked_call(self, event):
        ev = convert_keys(event)
        tenant_uuid = self._extract_tenant_uuid(ev)
        bus_event = UnParkedCallEvent(
            ev,
            tenant_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _parked_call_give_up(self, event):
        ev = convert_keys(event)
        tenant_uuid = self._extract_tenant_uuid(ev)
        bus_event = ParkedCallGiveUpEvent(
            ev,
            tenant_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _parked_call_swap(self, event):
        ev = convert_keys(event)
        tenant_uuid = self._extract_tenant_uuid(ev)
        bus_event = ParkedCallSwapEvent(
            ev,
            tenant_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _parked_call_timeout(self, event):
        ev = convert_keys(event)
        tenant_uuid = self._extract_tenant_uuid(ev)
        bus_event = ParkedCallTimeoutEvent(
            ev,
            tenant_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _extract_tenant_uuid(self, event):
        _, id_parking = event['parkinglot'].split('-')
        parkinglot = self.confd.parking_lots.get(id_parking)
        return parkinglot['tenant_uuid']
