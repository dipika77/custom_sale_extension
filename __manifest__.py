{
    'name': 'Custom Sale Extension',
    'version': '1.0',
    'summary': 'Add receipt fields and printable receipt for Sale Orders',
    'category': 'Sales',
    'author': 'Dipika',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/report_receipt_template.xml',
    ],
    'installable': True,
    'application': False,
}
