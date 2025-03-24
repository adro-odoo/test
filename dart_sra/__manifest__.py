{
  'name': 'Dart-Show day and night checkbox with time',
  'category':'customizations',
  'author':'Odoo PSIN',
  'version': '1.0',
  'license' : 'LGPL-3',
  'depends': ['mrp','base_automation'],
  'data':[
        'data/x_time_mrp_production.xml',
        'data/x_time_mrp_production_split.xml',
        'data/x_time_mrp_production_split_line.xml',
        'data/base_automation.xml',
        'views/mrp_production_view.xml',
        'views/wizard_view.xml',
        ],
  'installable': True,
  'application':False,
}