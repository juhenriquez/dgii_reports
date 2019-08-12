
# -*- coding: utf-8 -*-

import json
from datetime import datetime as dt

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class InvoiceServiceTypeDetail(models.Model):
    _name = 'invoice.service.type.detail'

    name = fields.Char()
    code = fields.Char(size=2)
    parent_code = fields.Char()

    _sql_constraints = [
        ('code_unique', 'unique(code)', _('Code must be unique')),
    ]


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    """
    ISR Percibido  --> Este campo se va con 12 espacios en 0 para el 606
    ITBIS Percibido --> Este campo se va con 12 espacios en 0 para el 606
    """
    payment_date = fields.Date(compute='_compute_taxes_fields', store=True)
    service_total_amount = fields.Monetary(compute='_compute_amount_fields',
                                           store=True,
                                           currency_field='company_currency_id')
    good_total_amount = fields.Monetary(compute='_compute_amount_fields',
                                        store=True,
                                        currency_field='company_currency_id')
    invoiced_itbis = fields.Monetary(compute='_compute_invoiced_itbis',
                                     store=True,
                                     currency_field='company_currency_id')
    withholded_itbis = fields.Monetary(compute='_compute_taxes_fields',
                                       store=True,
                                       currency_field='company_currency_id')
    proportionality_tax = fields.Monetary(compute='_compute_taxes_fields',
                                          store=True,
                                          currency_field='company_currency_id')
    cost_itbis = fields.Monetary(compute='_compute_taxes_fields', store=True,
                                 currency_field='company_currency_id')
    advance_itbis = fields.Monetary(compute='_compute_advance_itbis',
                                    store=True,
                                    currency_field='company_currency_id')
    isr_withholding_type = fields.Char(compute='_compute_isr_withholding_type',
                                       store=True, size=2)
    income_withholding = fields.Monetary(compute='_compute_taxes_fields',
                                         store=True,
                                         currency_field='company_currency_id')
    selective_tax = fields.Monetary(compute='_compute_taxes_fields', store=True,
                                    currency_field='company_currency_id')
    other_taxes = fields.Monetary(compute='_compute_taxes_fields', store=True,
                                  currency_field='company_currency_id')
    legal_tip = fields.Monetary(compute='_compute_taxes_fields', store=True,
                                currency_field='company_currency_id')
    payment_form = fields.Selection([
        ('01', 'Cash'),
        ('02', 'Check / Transfer / Deposit'),
        ('03', 'Credit Card / Debit Card'),
        ('04', 'Credit'),
        ('05', 'Swap'),
        ('06', 'Credit Note'),
        ('07', 'Mixed')],
        store=True,
    )
    third_withheld_itbis = fields.Monetary(compute='_compute_third_withheld',
                                           store=True,
                                           currency_field='company_currency_id')
    third_income_withholding = fields.Monetary(
        compute='_compute_third_withheld', store=True,
        currency_field='company_currency_id')
    is_exterior = fields.Boolean(compute='_compute_is_exterior', store=True)
    service_type = fields.Selection([
        ('01', 'Gastos de Personal'),
        ('02', 'Gastos por Trabajos, Suministros y Servicios'),
        ('03', 'Arrendamientos'),
        ('04', 'Gastos de Activos Fijos'),
        ('05', 'Gastos de Representación'),
        ('06', 'Gastos Financieros'),
        ('07', 'Gastos de Seguros'),
        ('08', 'Gastos por Regalías y otros Intangibles'),
    ])
    service_type_detail = fields.Many2one('invoice.service.type.detail')
    fiscal_status = fields.Selection([
        ('normal', 'Partial'),
        ('done', 'Reported'),
        ('blocked', 'Not Sent')], copy=False,
        help="* The \'Grey\' status means ...\n"
             "* The \'Green\' status means ...\n"
             "* The \'Red\' status means ...\n"
             "* The blank status means that the invoice have not been "
             "included in a report.",
    )
    income_type = fields.Selection([
        ('01', '01 - Ingresos por Operaciones (No Financieros)'),
        ('02', '02 - Ingresos Financieros'),
        ('03', '03 - Ingresos Extraordinarios'),
        ('04', '04 - Ingresos por Arrendamientos'),
        ('05', '05 - Ingresos por Venta de Activo Depreciable'),
        ('06', '06 - Otros Ingresos')],
        string='Tipo de Ingreso',
        default=lambda self: self._context.get('income_type', '01'),
    )
    
    @api.multi
    def get_dgii_values(self, invoice):
        result = {
            'selective_tax': 0.0,
            'other_taxes': 0.0,
            'legal_tip': 0.0,
            'proportionality_tax': 0.0,
            'cost_itbis': 0.0,
            'withholded_itbis': 0.0,
            'income_withholding': 0.0,
            'payment_date': False,
            'service_total_amount': 0.0,
            'good_total_amount': 0.0,
            'isr_withholding_type': 0.0,
            'invoiced_itbis': 0.0,
            'third_withheld_itbis': 0.0,
            'third_income_withholding': 0.0,
        }
        taxes_values = self._compute_taxes_fields(invoice)
        if taxes_values:
            result['selective_tax'] = taxes_values.get('selective_tax', 0.0)
            result['other_taxes'] = taxes_values.get('other_taxes', 0.0)
            result['legal_tip'] = taxes_values.get('legal_tip', 0.0)
            result['proportionality_tax'] = taxes_values.get(
                'proportionality_tax', 0.0)
            result['cost_itbis'] = taxes_values.get('cost_itbis', 0.0)
            result['withholded_itbis'] = taxes_values.get(
                'withholded_itbis', 0.0)
            result['income_withholding'] = taxes_values.get(
                'income_withholding', 0.0)
            result['payment_date'] = taxes_values.get('payment_date', False)

        amount_values = self._compute_amount_fields(invoice)
        if amount_values:
            result['service_total_amount'] = amount_values.get(
                'service_total_amount', 0)
            result['good_total_amount'] = amount_values.get(
                'good_total_amount', 0)

        isr_value = self._compute_isr_withholding_type(invoice)
        if isr_value:
            result['isr_withholding_type'] = isr_value.get(
                'isr_withholding_type', 0)

        invoiced_itbis_value = self._compute_invoiced_itbis(invoice)
        if invoiced_itbis_value:
            result['invoiced_itbis'] = invoiced_itbis_value.get(
                'invoiced_itbis', 0)

        invoiced_itbis = result.get('invoiced_itbis', 0.0)
        cost_itbis = result.get('cost_itbis', 0.0)
        result['advance_itbis'] = invoiced_itbis - cost_itbis

        third_withheld_values = self._compute_third_withheld(invoice)
        if third_withheld_values:
            result['third_withheld_itbis'] = third_withheld_values.get(
                'third_withheld_itbis', 0)
            result['third_income_withholding'] = third_withheld_values.get(
                'third_income_withholding', 0)

        result['is_exterior'] = self._compute_is_exterior(invoice)

        return result

    @api.onchange('journal_id')
    def ext_onchange_journal_id(self):
        self.service_type = False
        self.service_type_detail = False

    @api.onchange('state')
    def _onchange_invoce_state(self):
        for inv in self:
            if inv.state == 'paid':
                inv.compute_dgii_fields()

    @api.onchange('service_type')
    def onchange_service_type(self):
        self.service_type_detail = False
        return {
            'domain': {
                'service_type_detail': [
                    ('parent_code', '=', self.service_type)],
            },
        }

    def _get_invoice_payment_widget(self, invoice_id):
        j = json.loads(invoice_id.payments_widget)
        return j['content'] if j else []

    def _compute_invoice_payment_date(self):
        # payment_date = False
        for inv in self:
            if inv.state == 'paid':
                dates = [dt.strptime(payment['date'], '%Y-%m-%d')
                         for payment in inv._get_invoice_payment_widget(inv)]
                if dates:
                    inv.payment_date = max(dates)
        # return payment_date

    @api.multi
    @api.constrains('tax_line_ids')
    def _check_isr_tax(self):
        """Restrict one ISR tax per invoice"""
        for inv in self:
            line = [tax_line.tax_id.purchase_tax_type for tax_line in
                    inv.tax_line_ids
                    if tax_line.tax_id.purchase_tax_type in ['isr', 'ritbis']]
            if len(line) != len(set(line)):
                raise ValidationError(
                    _('An invoice cannot have multiple withholding taxes.'))

    def _convert_to_local_currency(self, inv, amount):
        sign = -1 if inv.type in ['in_refund', 'out_refund'] else 1
        if inv.currency_id != inv.company_id.currency_id:
            currency_id = inv.currency_id.with_context(date=inv.date_invoice)
            round_curr = currency_id.round
            amount = round_curr(currency_id.compute(amount, inv.company_id.currency_id))

        return amount * sign

    @api.model
    def _get_tax_line_ids(self, invoice):
        return invoice.tax_line_ids

    @api.multi
    @api.depends('tax_line_ids', 'tax_line_ids.amount', 'state')
    def _compute_taxes_fields(self):
        """Compute invoice common taxes fields"""
        res = {}
        for inv in self:
            fiscal_taxes = ['ISC', 'ITBIS', 'ISR', 'Propina']
            tax_line_ids = self._get_tax_line_ids(inv)

            if inv.state != 'draft':
                # Monto Impuesto Selectivo al Consumo
                inv.selective_tax = self._convert_to_local_currency(inv, sum(
                    tax_line_ids.filtered(
                        lambda tax: tax.tax_id.tax_group_id.name == 'ISC').mapped('amount')))

                # Monto Otros Impuestos/Tasas
                inv.other_taxes = self._convert_to_local_currency(inv, sum(
                    tax_line_ids.filtered(
                        lambda tax: tax.tax_id.purchase_tax_type not in [
                            'isr', 'ritbis'] and tax.tax_id.tax_group_id.name not in fiscal_taxes).mapped('amount')))

                # Monto Propina Legal
                inv.legal_tip = self._convert_to_local_currency(inv, sum(
                    tax_line_ids.filtered(
                        lambda tax: tax.tax_id.tax_group_id.name == 'Propina').mapped('amount')))

                # ITBIS sujeto a proporcionalidad
                inv.proportionality_tax = self._convert_to_local_currency(
                    inv, sum(tax_line_ids.filtered(
                        lambda tax: tax.account_id.account_fiscal_type == 'A29').mapped('amount')))

                # ITBIS llevado al Costo
                inv.cost_itbis = self._convert_to_local_currency(inv, sum(
                    tax_line_ids.filtered(
                        lambda tax: tax.account_id.account_fiscal_type == 'A51').mapped('amount')))

                if inv.type == 'in_invoice':
                    # Monto ITBIS Retenido
                    inv.withholded_itbis = self._convert_to_local_currency(
                        inv, sum(tax_line_ids.filtered(
                            lambda tax: tax.tax_id.purchase_tax_type == 'ritbis').mapped('amount')))

                    # Monto Retención Renta
                    inv.income_withholding = self._convert_to_local_currency(
                        inv, sum(tax_line_ids.filtered(
                            lambda tax: tax.tax_id.purchase_tax_type == 'isr').mapped('amount')))

                if inv.state == 'paid':
                    # Fecha Pago
                    inv.payment_date = self._compute_invoice_payment_date(inv)

    @api.multi
    @api.depends('invoice_line_ids', 'invoice_line_ids.product_id', 'state')
    def _compute_amount_fields(self):
        """Compute Purchase amount by product type"""
        res = {}
        for invoice in self:
            if invoice.type in ['in_invoice', 'in_refund'] and invoice.state != 'draft':
                service_amount = 0
                good_amount = 0

                for line in invoice.invoice_line_ids:
                    # Si la linea no tiene un producto
                    if not line.product_id:
                        service_amount += line.price_subtotal
                        continue
                    # Monto calculado en bienes
                    if line.product_id.type != 'service':
                        good_amount += line.price_subtotal
                    else:
                        # Monto calculado en servicio
                        service_amount += line.price_subtotal

                invoice.service_total_amount = self._convert_to_local_currency(
                    invoice, service_amount)
                invoice.good_total_amount = self._convert_to_local_currency(
                    invoice, good_amount)
        return res

    @api.multi
    @api.depends('invoice_line_ids', 'invoice_line_ids.product_id', 'state')
    def _compute_isr_withholding_type(self):
        """Compute ISR Withholding Type

        Keyword / Values:
        01 -- Alquileres
        02 -- Honorarios por Servicios
        03 -- Otras Rentas
        04 -- Rentas Presuntas
        05 -- Intereses Pagados a Personas Jurídicas
        06 -- Intereses Pagados a Personas Físicas
        07 -- Retención por Proveedores del Estado
        08 -- Juegos Telefónicos
        """
        res = {}
        for invoice in self:
            if invoice.type == 'in_invoice' and invoice.state != 'draft':
                isr = [tax_line.tax_id for tax_line in invoice.tax_line_ids if
                       tax_line.tax_id.purchase_tax_type == 'isr']
                if isr:
                    invoice.isr_withholding_type = isr.pop(0).isr_retention_type
        return res

    def _get_payment_string(self, invoice_id):
        """Compute Vendor Bills payment method string

        Keyword / Values:
        cash        -- Efectivo
        bank        -- Cheques / Transferencias / Depósitos
        card        -- Tarjeta Crédito / Débito
        credit      -- Compra a Crédito
        swap        -- Permuta
        credit_note -- Notas de Crédito
        mixed       -- Mixto
        """
        payments = []
        p_string = ""

        for payment in self._get_invoice_payment_widget(invoice_id):
            move_id = self.env['account.move'].browse(payment.get('move_id'))
            if move_id:
                if move_id.journal_id.type in ['cash', 'bank']:
                    p_string = move_id.journal_id.payment_form

            # If invoice is paid, but the payment doesn't come from
            # a journal, assume it is a credit note
            payment = p_string if move_id else 'credit_note'
            payments.append(payment)

        methods = {p for p in payments}
        if len(methods) == 1:
            return list(methods)[0]
        elif len(methods) > 1:
            return 'mixed'

    @api.multi
    def _compute_in_invoice_payment_form(self):
        for inv in self:
            if inv.state == 'paid':
                payment_dict = {
                    'cash': '01',
                    'bank': '02',
                    'card': '03',
                    'credit': '04',
                    'swap': '05',
                    'credit_note': '06',
                    'mixed': '07',
                }
                inv.payment_form = payment_dict.get(
                    self._get_payment_string(inv))
            else:
                inv.payment_form = '04'

    @api.multi
    @api.depends('tax_line_ids', 'tax_line_ids.amount', 'state')
    def _compute_invoiced_itbis(self):
        """Compute invoice invoiced_itbis taking into account the currency"""
        # res = {}
        for invoice in self:
            if invoice.state != 'draft':
                amount = 0
                itbis_taxes = ['ITBIS', 'ITBIS 18%']
                for tax in self._get_tax_line_ids(invoice):
                    if tax.tax_id.tax_group_id.name in itbis_taxes and \
                                    tax.tax_id.purchase_tax_type != 'ritbis':
                        amount += tax.amount
                    invoice.invoiced_itbis = self._convert_to_local_currency(
                        invoice, amount)
                print(amount)
                print(invoice.invoiced_itbis)
        # return res

    @api.multi
    @api.depends('state')
    def _compute_third_withheld(self):
        res = {}
        for invoice in self:
            if invoice.state == 'paid':
                for payment in self._get_invoice_payment_widget(invoice):
                    payment_id = self.env['account.payment'].browse(
                        payment.get('account_payment_id'))
                    if payment_id:
                        # ITBIS Retenido por Terceros
                        invoice.third_withheld_itbis = self._convert_to_local_currency(
                            invoice, sum([move_line.debit for move_line in payment_id.move_line_ids if move_line.account_id.account_fiscal_type == 'A36']))

                        # Retención de Renta por Terceros
                        invoice.third_income_withholding = self._convert_to_local_currency(
                            invoice, sum([move_line.debit
                                      for move_line in payment_id.move_line_ids
                                      if move_line.account_id.account_fiscal_type == 'ISR']))

    @api.multi
    @api.depends('invoiced_itbis', 'cost_itbis', 'state')
    def _compute_advance_itbis(self):
        for inv in self:
            if inv.state != 'draft':
                inv.advance_itbis = inv.invoiced_itbis - inv.cost_itbis

    @api.multi
    @api.depends('journal_id.purchase_type')
    def _compute_is_exterior(self):
        for inv in self:
            inv.is_exterior = True if inv.journal_id.purchase_type == 'exterior' else False

    @api.multi
    def invoice_filter(self):
        domain = [
            ('date_invoice', '=', '2019-05-06'),
            ('state', 'in', ['open', 'paid']),
        ]
        invoices = self.search(domain)
        _logger.info("=================================")
        _logger.info("Cantidad de facturas: %s" % len(invoices))
        _logger.info("=================================\n")
        return invoices
