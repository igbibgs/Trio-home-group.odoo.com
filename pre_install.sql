-- Pre-install SQL script: runs before Odoo loads any modules
-- Removes auto_backup (OCA) which is not available for Odoo 19
-- Odoo.sh provides native backup functionality as a replacement

-- Remove dependencies on auto_backup
DELETE FROM ir_module_module_dependency
WHERE name = 'auto_backup';

-- Mark auto_backup as uninstalled so Odoo stops looking for it
UPDATE ir_module_module
SET state = 'uninstalled'
WHERE name = 'auto_backup';
