# Copyright (C) 2014-2015  Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class ResPartner(models.Model):
    """Partner with birth date in date format."""
    _inherit = "res.partner"

    birthdate_date = fields.Date("Fecha de nacimiento")
    age = fields.Char(compute='_partner_age', string='Edad del Cliente',
                      help="Muestra la edad del Cliente en años (a), meses (m) y días (d).")

    @api.multi
    def _partner_age(self):
        def compute_age_from_dates(patient_dob):
            now = datetime.now()
            if (patient_dob):
                dob = datetime.strptime(str(patient_dob), '%Y-%m-%d')
                delta = relativedelta(now, dob)
                years_months_days = str(delta.years) + "a " + str(delta.months) + "m " + str(
                    delta.days) + "d"
            else:
                years_months_days = "No DoB !"

            return years_months_days

        self.age = compute_age_from_dates(self.birthdate_date)
