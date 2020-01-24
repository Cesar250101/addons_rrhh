# -*- coding: utf-8 -*-
{
    'name': "Addons Recursos Humanos",

    'summary': """
        Localización para el sistema de recursos humanos de Odoo 11""",

    'description': """
            En primera instancia se construye reporte de Contrato de Trabajo
    """,

    'author': "Method",
    'website': "http://www.openmethod.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_cl_hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/contrato_trabajo.xml',
        'reports/contrato_trabajo_template.xml',
        'reports/comprobante_ausencia.xml',
        'reports/comprobante_ausencia_template.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}