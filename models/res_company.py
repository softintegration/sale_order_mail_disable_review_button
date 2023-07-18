# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class Company(models.Model):
    _inherit = 'res.company'

    disable_mail_review_button = fields.Boolean("Disable the Quotation mail review button")

