# Copyright 2025 - Upgraded to Odoo 19
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
# Migration notes (16.0 -> 19.0):
# - The 16.0 migration handled translation migration to JSONB format.
#   This was already completed in v16. No further translation migration needed.
# - account.invoice.report: _select()/_group_by() methods no longer use
#   @api.model decorator — handled in Python model code directly.
# - No structural database changes required for product.brand model in v17-v19.

import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """
    Post-migration script for product_brand module upgrade to 19.0.

    This migration runs after the module is loaded in the new version.
    The JSONB translation migration from v16 is already complete and
    does not need to be repeated here.
    """
    if not version:
        return
    _logger.info(
        "product_brand: post-migration to v19 complete "
        "(no data transformations required)"
    )
