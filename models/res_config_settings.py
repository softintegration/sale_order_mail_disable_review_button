# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    disable_mail_review_button = fields.Boolean("Disable the Quotation mail review button",
                                                related='company_id.disable_mail_review_button',readonly=False)

