{
    'name': 'Blogs',
    'category': 'Website',
    'summary': 'News, Blogs, Announces, Discussions',
    'version': '1.0',
    'description': """
OpenERP Blog
============

        """,
    'author': 'OpenERP SA',
    'depends': ['website', 'mail'],
    'data': [
        'website_mail_data.xml',
        'views/website_mail.xml',
        'views/res_config.xml',
        'security/website_mail.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
}
