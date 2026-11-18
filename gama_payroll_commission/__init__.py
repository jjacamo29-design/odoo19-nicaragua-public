# -*- coding: utf-8 -*-
from . import models


def post_init_hook(env):
    """Crea (si no existen) las entradas de nómina y los parámetros de % que usan las reglas."""
    InputType = env["hr.payslip.input.type"]
    for code, name in (
        ("GAMA_RECUP", "GAMA - Recuperación de cartera cobrada (monto)"),
        ("GAMA_CONTADO", "GAMA - Venta de contado (monto)"),
    ):
        if not InputType.search([("code", "=", code)], limit=1):
            InputType.create({"code": code, "name": name})
    Param = env["hr.rule.parameter"]
    for code, name, value in (
        ("gama_com_recup", "GAMA - Comisión recuperación de cartera (%)", "4"),
        ("gama_com_contado", "GAMA - Comisión venta de contado (%)", "5"),
    ):
        if not Param.search([("code", "=", code)], limit=1):
            param = Param.create({"code": code, "name": name})
            env["hr.rule.parameter.value"].create({
                "rule_parameter_id": param.id,
                "date_from": "2024-01-01",
                "parameter_value": value,
            })
