# -*- coding: utf-8 -*-
{
    "name": "GAMA · Comisiones de vendedores en nómina",
    "version": "19.0.1.0.0",
    "category": "Human Resources/Payroll",
    "summary": "Calcula automáticamente la comisión de recuperación de cartera y de venta de contado "
               "desde Facturación (pedido de venta → factura → abono) y la carga en el recibo de nómina.",
    "description": """
Comisiones GAMA en nómina
=========================
* Recuperación de cartera: abonos aplicados en el periodo a facturas de crédito
  (conciliaciones de la factura con pagos o líneas de extracto; excluye notas de crédito
  y diferencial cambiario).
* Venta de contado: facturas de contado publicadas en el periodo (menos sus notas de crédito).
* Quién cobra el abono: 1) cobrador del recibo digital (si existe), 2) vendedor asignado a la
  ruta del cliente, 3) vendedor del pedido de venta (Vendedor Portal) o vendedor de la factura.
* El detalle queda guardado por recibo de nómina y alimenta las entradas
  GAMA_RECUP y GAMA_CONTADO, que usan las reglas salariales.
* Un abono o factura ya comisionado en otra nómina no se vuelve a comisionar.
""",
    "author": "SGINIC",
    "license": "LGPL-3",
    "depends": ["hr_payroll_account", "sale", "account"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_payroll_structure_views.xml",
        "views/hr_payslip_views.xml",
        "views/gama_commission_line_views.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
}
