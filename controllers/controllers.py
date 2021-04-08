# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.stock_barcode.controllers.main import StockBarcodeController
from odoo.exceptions import UserError

class CustomOnBarcodeController(StockBarcodeController):  # Inherit in your custom class

    # @http.route('/stock_barcode/scan_from_main_menu', type='json', auth='user')
    def try_open_picking(self, barcode):
        """ If barcode represents a picking, open it
        """
        corresponding_picking = request.env['stock.picking'].search([
            ('origin', '=', barcode),
            ('state', 'in', ['assigned', 'confirmed'] )
        ], limit=1)
        if corresponding_picking:
            return self.get_action(corresponding_picking.id)
        return False
