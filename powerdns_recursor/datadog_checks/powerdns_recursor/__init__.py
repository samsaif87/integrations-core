# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from .__about__ import __version__
from .powerdns_recursor import PowerDNSRecursorCheck

__all__ = ['PowerDNSRecursorCheck', '__version__']
