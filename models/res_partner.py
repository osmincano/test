# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.addons import decimal_precision as dp



class ResPartner(models.Model):
    _inherit = 'res.partner'

    nit = fields.Char(string='Nit', help="Nit.")
    vendedor = fields.Many2one('res.users',string='Vendedor')
