{
    'name': "Open HRMS GOSI",
    'version': '14.0.1.0.0',
    'summary': """GOSI Contribution for Saudi Government""",
    'description': """GOSI Contribution for Saudu Government From Employee and Company""",
    'category': 'Human Resource',
    'author': 'Cybrosys Techno solutions,Open HRMS',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.openhrms.com",
    'depends': ['base', 'hr', 'hr_payroll_community'],
    'data': [
             'views/gosi_view.xml',
             'views/sequence.xml',
             'data/rule.xml',
             'security/ir.model.access.csv',
            ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'installable': True,
    'application': True,
}
