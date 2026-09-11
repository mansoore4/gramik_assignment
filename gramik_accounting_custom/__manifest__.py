{
    'name': 'Gramik Accounting Custom',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Custom accounting features for Gramik',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
