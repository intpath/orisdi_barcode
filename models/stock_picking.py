# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        """
            When receipt is validated change the responsible id field to current user.
        """
        
        for record in self:
            record.user_id = self.env.user
        res = super(StockPicking, self).button_validate()
        return res
