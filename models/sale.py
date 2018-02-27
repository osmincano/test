# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    telefono = fields.Char(string='Telefono', help="Numero de telefono.")
    cliente = fields.Many2one('res.partner',string='Cliente destino')
