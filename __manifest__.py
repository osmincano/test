# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name" : "Xetechs Example",
    "version" : "1.0",
    "depends" : ["sale"],
    "category" : "Sale",
    "description": """
Modulo de Ejemplo.
""",
    "init_xml" : [],
    "demo_xml" : [],
    "data": ["views/test_views.xml",
             "views/sale_views.xml",
             "views/res_partner_view.xml"],
    "active": False,
    "installable": True
}
