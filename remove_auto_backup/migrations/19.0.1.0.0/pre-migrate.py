# -*- coding: utf-8 -*-
# Pre-migration script: uninstall auto_backup before v19 upgrade.
# auto_backup (OCA server-tools) is not available for Odoo 19.
# Odoo.sh provides native backup functionality as a replacement.

import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Uninstall auto_backup module cleanly before v19 upgrade."""
    cr.execute("""
        SELECT id FROM ir_module_module
        WHERE name = 'auto_backup'
        AND state NOT IN ('uninstalled', 'uninstallable')
    """)
    row = cr.fetchone()
    if row:
        _logger.info("remove_auto_backup: marking auto_backup for uninstall")
        cr.execute("""
            UPDATE ir_module_module
            SET state = 'to remove'
            WHERE name = 'auto_backup'
        """)
        _logger.info("remove_auto_backup: auto_backup marked as 'to remove'")
    else:
        _logger.info("remove_auto_backup: auto_backup not found or already uninstalled, skipping")
