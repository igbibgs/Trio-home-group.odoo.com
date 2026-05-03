# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
# Upgraded to Odoo 19 - 2025

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AdvancePayment(models.TransientModel):
    _name = 'advance.payment'
    _description = 'Advance Payment'

    journal_id = fields.Many2one(
        comodel_name='account.journal',
        string="Payment Journal",
        required=True,
        domain=[('type', 'in', ['cash', 'bank'])],
    )
    pay_amount = fields.Float(
        string="Payable Amount",
        required=True,
    )
    # Changed from Datetime to Date: account.payment.date expects a Date field (v17+)
    date_planned = fields.Date(
        string="Advance Payment Date",
        index=True,
        default=fields.Date.today,
        required=True,
    )

    @api.constrains('pay_amount')
    def check_amount(self):
        for rec in self:
            if rec.pay_amount <= 0:
                raise ValidationError(_("Please Enter a Positive Amount"))

    def make_payment(self):
        payment_obj = self.env['account.payment']
        purchase_ids = self.env.context.get('active_ids')
        if purchase_ids:
            payment_vals = self._get_payment_vals(purchase_ids)
            payment = payment_obj.create(payment_vals)
            payment.action_post()
        return {'type': 'ir.actions.act_window_close'}

    def _get_payment_vals(self, purchase_ids):
        """Build account.payment create values for v19.

        Key changes vs v16:
        - payment_method_line_id replaces payment_method_id (renamed in v17)
          It now points to account.payment.method.line on the journal, not
          account.payment.method directly.
        - date is now a Date field (not Datetime)
        """
        purchase = self.env['purchase.order'].browse(purchase_ids[0])

        # Resolve the correct payment method line for 'manual outbound'
        # on the selected journal (v17+ requirement)
        payment_method_line = self.journal_id.outbound_payment_method_line_ids.filtered(
            lambda l: l.code == 'manual'
        )[:1]

        return {
            'payment_type': 'outbound',
            'partner_id': purchase.partner_id.id,
            'partner_type': 'supplier',
            'journal_id': self.journal_id.id,
            'company_id': purchase.company_id.id,
            'currency_id': purchase.currency_id.id,
            'date': self.date_planned,
            'amount': self.pay_amount,
            'purchase_id': purchase.id,
            'payment_method_line_id': payment_method_line.id,
        }
