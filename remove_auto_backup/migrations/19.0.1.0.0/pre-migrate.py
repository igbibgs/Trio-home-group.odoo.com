# -*- coding: utf-8 -*-
# Pre-migration script: uninstall auto_backup before v19 upgrade.
# auto_backup (OCA server-tools) is not available for Odoo 19.
# Odoo.sh provides native backup functionality as a replacement.
#
# Uses odoo.upgrade.util.remove_module() - the official Odoo upgrade utility.

import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Uninstall auto_backup module cleanly before v19 upgrade."""
    try:
        from odoo.upgrade import util
        _logger.info("remove_auto_backup: using odoo.upgrade.util.remove_module()")
        util.remove_module(cr, 'auto_backup')
        _logger.info("remove_auto_backup: auto_backup removed via util.remove_module()")
    except Exception as e:
        # Fallback: direct SQL if util is not available
        _logger.warning("remove_auto_backup: util not available (%s), falling back to SQL", e)
        cr.execute("""
            DELETE FROM ir_module_module_dependency
            WHERE name = 'auto_backup';
        """)
        cr.execute("""
            UPDATE ir_module_module
            SET state = 'uninstalled'
            WHERE name = 'auto_backup';
        """)
        _logger.info("remove_auto_backup: auto_backup removed via SQL fallback")
