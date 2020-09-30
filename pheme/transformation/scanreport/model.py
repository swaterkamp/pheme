# -*- coding: utf-8 -*-
# pheme/transformation/scanreport/model.py
# Copyright (C) 2020 Greenbone Networks GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# pylint: disable=W0614,W0511,W0401,C0103
from dataclasses import dataclass
from typing import Dict, List, Union


@dataclass
class NVTThreatCount:
    level: str
    count: int


@dataclass
class Equipment:
    os: str  # search for host.text and refs than os-detection
    ports: List[str]  # ports port host and ports port text


@dataclass
class HostResults:
    host: str
    equipment: Equipment
    results: List[Dict]


@dataclass
class NVTCount:
    oid: str
    amount: int
    name: str


@dataclass
class HostCount:
    ip: str
    amount: int
    name: str


@dataclass
class CountGraph:
    name: str
    chart: str
    counts: List[Union[NVTCount, HostCount]]


@dataclass
class SeverityCount:
    severity: str
    amount: int


@dataclass
class Overview:
    hosts: CountGraph
    nvts: CountGraph
    vulnerable_equipment: CountGraph


@dataclass
class Report:
    id: str
    name: str
    comment: str
    version: str
    start: str
    overview: Overview
    results: List[HostResults]


def descripe():
    return Report(
        id="str; identifier of a report",
        name="str; name of the scan",
        comment="str; comment of the scan",
        version="str; version of gvmd",
        start="str; datetime of a scan start",
        overview=Overview(
            hosts=CountGraph(
                name="host_top_ten",
                chart="str; link to chart image (base64 encoded datalink)",
                counts=[],
            ),
            nvts=CountGraph(
                name="nvt_overview",
                chart="str; link to chart image (base64 encoded datalink)",
                counts=[],
            ),
            vulnerable_equipment=CountGraph(
                name="vulnerable_equipment",
                chart="str; link to chart image (base64 encoded datalink)",
                counts=[],
            ),
        ),
        results=[
            HostResults(
                host="str; ip address of host",
                equipment=Equipment(
                    os="str; operating system", ports=["str; open ports"]
                ),
                results={
                    'nvt.oid': 'str; nvt.oid; optional',
                    'nvt.type': 'str; nvt.type; optional',
                    'nvt.name': 'str; nvt.name; optional',
                    'nvt.family': 'str; nvt.family; optional',
                    'nvt.cvss_base': 'str; nvt.cvss_base; optional',
                    'nvt.tags_interpreted': {
                        'name_of_tag': 'str; value of a tag ()',
                        'may_contain_multiple_tags': 'str; depends on xml',
                        'solution': 'str; solution the fix the problem',
                        'solution_type': 'str; solution type',
                        'insight': 'str; insight into the problem',
                        'vuldetect': 'str; ',
                        'cvss_base_vector': 'str, cvss base vector',
                    },
                    'nvt.refs.ref': [{'name_of_ref': ["str; ref_vallue"]}],
                    'nvt.solution.type': 'str; nvt.solution.type; optional',
                    'nvt.solution.text': 'str; nvt.solution.text; optional',
                    'port': 'str; port; optional',
                    'threat': 'str; severity class of nvt',
                    'severity': 'str; severity; optional',
                    'qod.value': 'str; qod.value; optional',
                    'qod.type': 'str; qod.type; optional',
                    'description': 'str; description; optional',
                },
            )
        ],
    )
