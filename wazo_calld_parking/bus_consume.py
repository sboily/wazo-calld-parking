# Copyright 2016-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from .event import ArbitraryEvent


logger = logging.getLogger(__name__)


class ParkingBusEventHandler(object):

    def __init__(self, bus_publisher):
        self.bus_publisher = bus_publisher

    def subscribe(self, bus_consumer):
        bus_consumer.subscribe('ParkedCall', self._parked_call)
        bus_consumer.subscribe('UnParkedCall', self._unparked_call)
        bus_consumer.subscribe('ParkedCallGiveUp', self._parked_call_give_up)
        bus_consumer.subscribe('ParkedCallSwap', self._parked_call_swap)
        bus_consumer.subscribe('ParkedCallTimeout', self._parked_call_timeout)

    def _parked_call(self, event):
        bus_event = ArbitraryEvent(
            name='parking_parked_call',
            body=event,
            required_acl='events.parking'
        )
        bus_event.routing_key = 'parking.parked_call'
        self.bus_publisher.publish(bus_event)

    def _unparked_call(self, event):
        bus_event = ArbitraryEvent(
            name='parking_unparked_call',
            body=event,
            required_acl='events.parking'
        )
        bus_event.routing_key = 'parking.unparked_call'
        self.bus_publisher.publish(bus_event)

    def _parked_call_give_up(self, event):
        bus_event = ArbitraryEvent(
            name='parking_parked_call_give_up',
            body=event,
            required_acl='events.parking'
        )
        bus_event.routing_key = 'parking.parked_call_give_up'
        self.bus_publisher.publish(bus_event)

    def _parked_call_swap(self, event):
        bus_event = ArbitraryEvent(
            name='parking_parked_call_swap',
            body=event,
            required_acl='events.parking'
        )
        bus_event.routing_key = 'parking.parked_call_swap'
        self.bus_publisher.publish(bus_event)

    def _parked_call_timeout(self, event):
        bus_event = ArbitraryEvent(
            name='parking_parked_call_timeout',
            body=event,
            required_acl='events.parking'
        )
        bus_event.routing_key = 'parking.parked_call_timeout'
        self.bus_publisher.publish(bus_event)
