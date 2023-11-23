# Copyright 2018-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging


class ParkingService:

    def __init__(self, amid, confd, ari):
        self.amid = amid
        self.confd = confd
        self.ari = ari

    def list_parking(self, tenant_uuid):
        self.confd.set_tenant(tenant_uuid)
        parking = self.confd.parking_lots.list()
        return parking

    def get_parked_calls(self, parking_name, tenant_uuid):
        if not self._check_parking_tenant_uuid(tenant_uuid, parking_name):
            return []

        parked_calls = self.amid.action('parkedcalls', {'ParkingLot': parking_name})
        p = []
        for park in parked_calls:
            if park.get('Event') == 'ParkedCall':
                print(park)
                p.append(self._parked_call(park))
        return p

    def park_call(self, parking_name, params, tenant_uuid):
        if not self._check_parking_tenant_uuid(tenant_uuid, parking_name):
            return []

        channel = self.ari.channels.get(channelId=params.get('call_id'))
        channel_name = channel.json['name']

        park_action = {
            'Parkinglot': parking_name,
            'Channel': channel_name,
            'AnnounceChannel': params.get('announce_channel'),
            'Timeout': params.get('timeout'),
            'TimeoutChannel': params.get('timeout_channel'),
        }
        parking = self.amid.action('park', park_action)
        return None

    def _check_parking_tenant_uuid(self, tenant_uuid, parking_name):
        self.confd.set_tenant(tenant_uuid)
        _, id_parking = parking_name.split('-')
        return self.confd.parking_lots.get(id_parking)

    def _parking(self, parking):
        return {
            'stop_space': parking.get('StopSpace'),
            'start_space': parking.get('StartSpace'),
            'timeout': parking.get('Timeout'),
            'name': parking.get('Name')
        }

    def _parked_call(self, parked_call):
        return {
            'parkee_priority': parked_call.get('ParkeePriority'),
            'parkee_connected_line_num': parked_call.get('ParkeeConnectedLineNum'),
            'parkee_connected_line_name': parked_call.get('ParkeeConnectedLineName'),
            'parkee_channel_state': parked_call.get('ParkeeChannelState'),
            'parkee_exten': parked_call.get('ParkeeExten'),
            'parkee_context': parked_call.get('ParkeeContext'),
            'parkee_account_code': parked_call.get('ParkeeAccountCode'),
            'parker_dial_string': parked_call.get('ParkerDialString'),
            'parkee_caller_id_num': parked_call.get('ParkeeCallerIDNum'),
            'parkee_caller_id_name': parked_call.get('ParkeeCallerIDName'),
            'parkee_unique_id': parked_call.get('ParkeeUniqueid'),
            'parking_lot': parked_call.get('Parkinglot'),
            'parkee_language': parked_call.get('ParkeeLanguage'),
            'parkee_channel': parked_call.get('ParkeeChannel'),
            'parkee_channel_state_desc': parked_call.get('ParkeeChannelStateDesc'),
            'parkee_linkedid': parked_call.get('ParkeeLinkedid'),
            'parkee_chan_variable': parked_call.get('ParkeeChanVariable'),
            'parking_timeout': parked_call.get('ParkingTimeout'),
            'parking_duration': parked_call.get('ParkingDuration'),
            'parking_space': parked_call.get('ParkingSpace'),
        }
