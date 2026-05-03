# -*- coding: utf-8 -*-
# Post-migration: confirm auto_backup is fully uninstalled.

import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Ensure auto_backup is fully uninstalled after v19 upgrade."""
    cr.execute("""
        UPDATE ir_module_module
        SET state = 'uninstalled'
        WHERE name = 'auto_backup'
        AND state != 'uninstalled'
    """)
    if cr.rowcount:
        _logger.info("remove_auto_backup: auto_backup forcibly set to uninstalled")
    else:
        _logger.info("remove_auto_backup: auto_backup already uninstalled")
