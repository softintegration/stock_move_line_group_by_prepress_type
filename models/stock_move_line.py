# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    prepress_type = fields.Many2one('prepress.type', 'Type',related='product_id.prepress_type',store=True,
                               readonly=True,index=True)
