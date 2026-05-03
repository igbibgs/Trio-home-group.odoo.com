# -*- coding: utf-8 -*-
# Post-migration: uninstall the auto_backup stub after v19 upgrade completes.
# The real OCA auto_backup is not available for Odoo 19.
# Odoo.sh provides native backup functionality as a replacement.

import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Mark auto_backup as uninstalled after upgrade completes."""
    _logger.info("auto_backup stub: marking auto_backup as uninstalled post-upgrade")
    cr.execute("""
        DELETE FROM ir_module_module_dependency
        WHERE name = 'auto_backup';
    """)
    cr.execute("""
        UPDATE ir_module_module
        SET state = 'uninstalled'
        WHERE name = 'auto_backup';
    """)
    _logger.info("auto_backup stub: done - auto_backup uninstalled cleanly")
