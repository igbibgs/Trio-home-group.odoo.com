# -*- coding: utf-8 -*-
# Dummy module - satisfies auto_backup dependency during v19 upgrade
# The real OCA auto_backup is not available for Odoo 19.
# Odoo.sh provides native backup functionality as a replacement.
{
    'name': 'Auto Backup (Stub)',
    'version': '19.0.1.0.0',
    'summary': 'Stub module to satisfy auto_backup dependency during v19 upgrade',
    'author': 'Trio Home Group',
    'license': 'LGPL-3',
    'depends': ['base'],
    'installable': True,
    'auto_install': False,
}
