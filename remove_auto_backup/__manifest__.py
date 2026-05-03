# -*- coding: utf-8 -*-
{
    'name': 'Remove Auto Backup',
    'version': '19.0.1.0.0',
    'summary': 'Uninstalls auto_backup module during v19 upgrade',
    'description': 'Helper module to cleanly remove auto_backup (OCA) '
                   'which is not available for v19. '
                   'Odoo.sh provides built-in backup functionality.',
    'author': 'Trio Home Group',
    'license': 'LGPL-3',
    'depends': ['base'],
    'installable': True,
    'auto_install': False,
}
