# -*- coding: utf-8 -*-

from odoo import api, models, fields


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    payment_form = fields.Selection(
        [("cash", "Efectivo"),
         ("bank", u"Cheque / Transferencia / Depósito"),
         ("card", u"Tarjeta Crédito / Débito"),
         ("credit", u"A Crédito"),
         ("swap", "Permuta"),
         ("bond", "Bonos o Certificados de Regalo"),
         ("others", "Otras Formas de Venta")],
        string="Forma de Pago", oldname="ipf_payment_type")

    @api.onchange("type")
    def onchange_type(self):
        if self.type != 'sale':
            self.ncf_control = False
