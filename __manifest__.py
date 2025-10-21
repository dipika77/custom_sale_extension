{
    'name': 'Custom Sale Extension',
    'version': '1.0',
    'summary': 'Add receipt fields and printable receipt for Sale Orders',
    'category': 'Sales',
    'author': 'Dipika',
    #'depends': ['sale_management'],
    'depends': ['base', 'web', 'website'],
   # 'data': [
    #    'security/ir.model.access.csv',
     #   'views/sale_order_view.xml',
      #  'views/report_receipt_template.xml',
    #],
    'data': ['views/menu.xml'],
     'assets': {
        'web.assets_frontend': [
            'custom_sale_extension/static/src/js/form_app.js',
            'custom_sale_extension/static/src/xml/templates.xml',
        ],
    },
    'installable': True,
    'application': False,
}



