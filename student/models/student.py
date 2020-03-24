from odoo import models, fields
from odoo import api


class Student(models.Model):
    _name = 'student.information'

    @api.depends('age')
    def compute_set_age_group(self):
        for rec in self:
            if rec.age:
                if rec.age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    @api.depends('physics','chemistry','maths')
    def compute_percentage(self):
        for rec in self:
                rec.percentage = (rec.physics + rec.chemistry + rec.maths)/3

    @api.onchange('name')
    def _onchange_name(self):
        self.display_name = 'Hello' + self.name if self.name else ''            

    name = fields.Char(string="Student Name")
    birth_date = fields.Date()
    age_group = fields.Selection([('major','Major'),('minor','Minor')], string="Age Group", compute='compute_set_age_group')
    # physics = fields.Selection([('physics_marks', 'p')], string = "Physics Marks", compute='calculate')
    # chemistry = fields.Selection([('chemistry_marks', 'c')], string = "Chemistry Marks", compute='calculate')
    # maths = fields.Selection([('maths_marks', 'm')], string = "Maths Marks", compute='calculate')
    physics = fields.Float()
    chemistry = fields.Float()
    maths = fields.Float()
    age = fields.Integer()
    sports_enthusiastic = fields.Boolean(string='Sports Enthusiastic?')
    sem_strt = fields.Datetime(string='Starting Of Semester')
    percentage = fields.Float(string='12th Grade Percentage', compute='compute_percentage')
    display_name = fields.Char()

