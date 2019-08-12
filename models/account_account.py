# -*- coding: utf-8 -*-

from odoo import api, models, fields


class AccountAccount(models.Model):
    _inherit = 'account.account'

    account_fiscal_type = fields.Selection(
        [('A08', 'A08 - Otras Operaciones (Positivas)'),
         ('A09', 'A09 - Otras Operaciones (Negativas)'),
         ('A19', 'A19 - Ingresos por Operaciones (No Financieros)'),
         ('A20', 'A20 - Ingresos Financieros'),
         ('A21', 'A21 - Ingresos Extraordinarios'),
         ('A22', 'A22 - Ingresos por Arrendamientos'),
         ('A23', 'A23 - Ingresos por Ventas de Activos Depreciables'),
         ('A24', 'A24 - Otros Ingresos'),
         ('A26', 'A26 - ITBIS Pagado en Importaciones'),
         ('A27', 'A27 - ITBIS Pagado en Importaciones para la Producción de Bienes Exentos'),
         ('A29', 'A29 - ITBIS en Bienes o Servicios sujetos a Proporcionalidad'),
         ('A30', 'A30 - ITBIS en Importaciones sujetos a Proporcionalidad'),
         ('A34', 'A34 - Pagos Computables por Retenciones (N08-04)'),
         ('A35', 'A35 - Pagos Computables por Boletos Aéreos (N02-05) (BSP-IATA)'),
         ('A36', 'A36 - Pagos Computables por otras Retenciones (N02-05)'),
         ('A37', 'A37 - Pagos Computables por Paquetes de Alojamiento y Ocupación'),
         ('A38', 'A38 - Crédito por retención realizada por Entidades del Estado'),
         ('A41', 'A41 - Dirección Técnica (N07-07)'),
         ('A42', 'A42 - Contrato de Administración (N07-07)'),
         ('A43', 'A43 - Asesorías / Honorarios'),
         ('A46', 'A46 - Ventas de Bienes en Concesión'),
         ('A47', 'A47 - Ventas de Servicios en Nombre de Terceros'),
         ('A50', 'A50 - Total Notas de Crédito emitidas con más de 30 días'),
         ('A51', 'A51 - ITBIS llevado al Costo'),
         ('I02', 'I02 - Ingresos por Exportaciones de Bienes o Servicios'),
         ('I03', 'I03 - Ingresos por ventas locales de bienes o servicios exentos'),
         ('I04', 'I04 - Ingresos por ventas de bienes o servicios exentos por destino'),
         ('I13', 'I13 - Operaciones gravadas por ventas de Activos Depreciables (categoría 2 y 3)'),
         ('I28', 'I28 - Saldos Compensables Autorizados (Otros Impuestos) y/o Reembolsos'),
         ('I35', 'I35 - Recargos'),
         ('I36', 'I36 - Interés Indemnizatorio'),
         ('I39', 'I39 - Servicios sujetos a Retención Personas Físicas'),
         ('ISR', 'Retención de Renta por Terceros')],
         string='Account Fiscal Type', copy=False,
    )

    income_type = fields.Selection(
        [('01', '01 - Ingresos por operaciones (No financieros)'),
         ('02', '02 - Ingresos Financieros'),
         ('03', '03 - Ingresos Extraordinarios'),
         ('04', '04 - Ingresos por Arrendamientos'),
         ('05', '05 - Ingresos por Venta de Activo Depreciable'),
         ('06', '06 - Otros Ingresos')],
        string='Tipo de Ingreso')

    expense_type = fields.Selection(
        [('01', '01 - Gastos de Personal'),
         ('02', '02 - Gastos por Trabajo, Suministros y Servicios'),
         ('03', '03 - Arrendamientos'),
         ('04', '04 - Gastos de Activos Fijos'),
         ('05', u'05 - Gastos de Representación'),
         ('06', '06 - Otras Deducciones Admitidas'),
         ('07', '07 - Gastos Financieros'),
         ('08', '08 - Gastos Extraordinarios'),
         ('09', '09 - Compras y Gastos que forman parte del Costo de Venta'),
         ('10', '10 - Adquisiciones de Activos'),
         ('11', '11 - Gastos de Seguros')],
        string="Tipo de Costos y Gastos")

    @api.onchange('user_type_id')
    def onchange_user_type_id(self):
        self.income_type = False
        self.expense_type = False


class AccountTax(models.Model):
    _inherit = 'account.tax'

    isr_retention_type = fields.Selection(
        [('01', 'Alquileres'),
         ('02', 'Honorarios por Servicios'),
         ('03', 'Otras Rentas'),
         ('04', 'Rentas Presuntas'),
         ('05', u'Intereses Pagados a Personas Jurídicas'),
         ('06', u'Intereses Pagados a Personas Físicas'),
         ('07', u'Retención por Proveedores del Estado'),
         ('08', u'Juegos Telefónicos')],
        string="Tipo de Retención en ISR"
    )
