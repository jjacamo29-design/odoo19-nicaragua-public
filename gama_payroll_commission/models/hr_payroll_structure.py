# -*- coding: utf-8 -*-
from odoo import fields, models


class HrPayrollStructure(models.Model):
    _inherit = "hr.payroll.structure"

    gama_commission = fields.Boolean(
        string="Calcular comisiones de ventas",
        help="Al calcular el recibo, trae desde Facturación la recuperación de cartera y la "
             "venta de contado del vendedor en el periodo y llena las entradas GAMA_RECUP y GAMA_CONTADO.",
    )
    gama_cash_term_ids = fields.Many2many(
        "account.payment.term",
        "gama_struct_cash_term_rel", "struct_id", "term_id",
        string="Plazos de pago de contado",
        default=lambda self: self.env.ref("account.account_payment_term_immediate", raise_if_not_found=False),
        help="Las facturas con estos plazos se comisionan como venta de contado. "
             "Las demás se comisionan cuando se cobran (recuperación de cartera).",
    )
    gama_base = fields.Selection(
        [("total", "Monto total (con impuestos)"), ("untaxed", "Monto sin impuestos")],
        string="Base de la comisión", default="total", required=True,
    )
    gama_use_route = fields.Boolean(
        string="Atribuir cobros al vendedor de la ruta del cliente", default=True,
        help="Si el cliente tiene ruta con vendedor asignado, el abono se le comisiona a ese vendedor "
             "aunque la factura la haya hecho otro.",
    )
