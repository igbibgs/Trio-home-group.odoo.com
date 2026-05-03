# Copyright 2018 Tecnativa - David Vidal
# Copyright 2025 - Upgraded to Odoo 19
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    product_brand_id = fields.Many2one(
        comodel_name="product.brand",
        string="Brand",
        readonly=True,
    )

    def _select(self):
        return (
            super()._select()
            + ", template.product_brand_id AS product_brand_id"
        )

    def _group_by(self):
        return super()._group_by() + ", template.product_brand_id"
