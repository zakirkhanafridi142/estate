{
    'name': "estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Zakir Afridi",
    'category': 'Category, Estate Business Features',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        # 'views/mymodule_view.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',

    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
