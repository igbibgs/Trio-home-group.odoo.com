-- Pre-install SQL script: runs before Odoo loads any modules
-- Removes auto_backup (OCA) which is not available for Odoo 19
-- Odoo.sh provides native backup functionality as a replacement

-- Remove all dependencies pointing to auto_backup
DELETE FROM ir_module_module_dependency
WHERE name = 'auto_backup';

-- Remove all dependencies that auto_backup itself had
DELETE FROM ir_module_module_dependency
WHERE module_id = (
    SELECT id FROM ir_module_module WHERE name = 'auto_backup'
);

-- Remove any ir.cron entries belonging to auto_backup
DELETE FROM ir_cron
WHERE id IN (
    SELECT res_id FROM ir_model_data
    WHERE module = 'auto_backup'
    AND model = 'ir.cron'
);

-- Remove all ir.model.data records for auto_backup
DELETE FROM ir_model_data
WHERE module = 'auto_backup';

-- Finally mark auto_backup as uninstalled
UPDATE ir_module_module
SET state = 'uninstalled'
WHERE name = 'auto_backup';
