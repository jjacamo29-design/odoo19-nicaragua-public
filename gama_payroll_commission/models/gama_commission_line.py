# -*- coding: utf-8 -*-
from odoo import fields, models


class GamaCommissionLine(models.Model):
    _name = "gama.commission.line"
    _description = "Detalle de comisión de vendedor (nómina)"
    _order = "payslip_id, commission_type, date, id"

    payslip_id = fields.Many2one("hr.payslip", string="Recibo de nómina", required=True,
                                 ondelete="cascade", index=True)
    payslip_state = fields.Selection(related="payslip_id.state", string="Estado nómina", store=True)
    employee_id = fields.Many2one(related="payslip_id.employee_id", store=True, string="Vendedor")
    company_id = fields.Many2one(related="payslip_id.company_id", store=True)
    currency_id = fields.Many2one(related="company_id.currency_id")
    commission_type = fields.Selection(
        [("recovery", "Recuperación de cartera"), ("cash", "Venta de contado")],
        string="Tipo", required=True)
    date = fields.Date(string="Fecha")
    invoice_id = fields.Many2one("account.move", string="Factura / NC", index=True)
    partner_id = fields.Many2one("res.partner", string="Cliente")
    sale_order_id = fields.Many2one("sale.order", string="Pedido de venta")
    payment_move_id = fields.Many2one("account.move", string="Abono (asiento)")
    partial_id = fields.Many2one("account.partial.reconcile", string="Conciliación", index=True,
                                 ondelete="set null")
    collector_source = fields.Selection(
        [("receipt", "Recibo de cobro"), ("route", "Ruta del cliente"), ("seller", "Vendedor de la venta")],
        string="Atribuido por")
    base_amount = fields.Monetary(string="Base", currency_field="currency_id")
    rate = fields.Float(string="%")
    commission_amount = fields.Monetary(string="Comisión", currency_field="currency_id")
