# -*- coding: utf-8 -*-
{
    'name': "car_story",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/explore_template.xml',
        'views/snippets/s_story.xml',
        'views/snippets/options.xml',
    ],
    'assets': {
      'web.assets_frontend': [
          '/car_story/static/src/scss/options.scss',
          '/car_story/static/src/js/new_story.js',
      ]
    },
    'demo': [
        'demo/demo.xml',
    ],
}

