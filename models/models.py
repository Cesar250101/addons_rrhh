# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class NewModule(models.Model):
    _inherit = 'hr.contract'
    trabajo_pesado = fields.Boolean(string='Trabajo Pesado?')

class EntradasNomina(models.Model):
    _inherit = 'hr.payslip.input'

    fecha_desde = fields.Date(string="Fecha Desde", required=False, related="payslip_id.date_from")
    fecha_hasta = fields.Date(string="Fecha Hasta", required=False, related="payslip_id.date_to")

