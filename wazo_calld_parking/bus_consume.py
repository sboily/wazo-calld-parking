# Copyright 2016-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from .events import (
    ParkedCallEvent
    UnParkedCallEvent
    ParkedCallGiveUp
    ParkedCallSwap
    ParkedCallTimeout
)


logger = logging.getLogger(__name__)


class ParkingBusEventHandler:

    def __init__(self, bus_publisher, confd):
        self.bus_publisher = bus_publisher
        self.confd = confd

    def subscribe(self, bus_consumer):
        bus_consumer.subscribe('ParkedCall', self._parked_call)
        bus_consumer.subscribe('UnParkedCall', self._unparked_call)
        bus_consumer.subscribe('ParkedCallGiveUp', self._parked_call_give_up)
        bus_consumer.subscribe('ParkedCallSwap', self._parked_call_swap)
        bus_consumer.subscribe('ParkedCallTimeout', self._parked_call_timeout)

    def _parked_call(self, event):
        tenant_uuid = self._extract_tenant_uuid(event)
        bus_event = ParkedCallEvent(
            event,
            tenant_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _unparked_call(self, event):
        tenant_uuid = self._extract_tenant_uuid(event)
        bus_event = UnParkedCallEvent(
            event,
            tenant_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _parked_call_give_up(self, event):
        tenant_uuid = self._extract_tenant_uuid(event)
        bus_event = ParkedCallGiveUpEvent(
            event,
            tenant_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _parked_call_swap(self, event):
        tenant_uuid = self._extract_tenant_uuid(event)
        bus_event = ParkedCallSwapEvent(
            event,
            tenant_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _parked_call_timeout(self, event):
        tenant_uuid = self._extract_tenant_uuid(event)
        bus_event = ParkedCallTimeoutEvent(
            event,
            tenant_uuid
        )
        self.bus_publisher.publish(bus_event)

    def _extract_tenant_uuid(self, event):
        _, id_parking = event['data']['Parkinglot'].split('-')
        parkinglot = self.confd.parkinglots.get(id_parking)
        return parkinglot['tenant_uuid']
