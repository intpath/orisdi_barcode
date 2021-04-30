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
        # using query instead of search for faster search result
        self.env.cr.execute("SELECT id FROM stock_picking WHERE origin = '%s' and (state = 'assigned' or state = 'confirmed')" % (barcode))
        # result are a list of records
        res = self.env.cr.fetchall()
        if res:
            # getting the id of the of first recode from the result
            return self.get_action(res[0][0])
        return False
