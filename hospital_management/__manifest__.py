# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital Management',
    'version': '1.0',
    'sequence': -100,
    'summary': 'Hospital Management Software',
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml'
        ],
    'demo':[],
    'qweb':[],
    'installable': True,
    'application': True,
    'auto_install':False,
}
