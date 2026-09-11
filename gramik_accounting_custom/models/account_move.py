from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    business_segment = fields.Selection(
        selection=[
            ('b2b_distributor', 'B2B – Distributor'),
            ('b2b_retailer', 'B2B – Retailer'),
            ('b2c', 'B2C'),
        ],
        string='Business Segment',
    )
