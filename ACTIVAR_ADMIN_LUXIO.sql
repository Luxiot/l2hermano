-- ===========================================
-- L2 HERMANOS - ACTIVAR MODO ADMIN PARA LUXIO
-- ===========================================
-- Este script activa el modo admin para el personaje "Luxio"
-- Niveles de acceso:
-- 0 = Jugador normal
-- 1 = GM (Game Master)
-- 2 = Admin
-- 3 = Super Admin
-- 4 = Head Admin
-- 5 = Owner
-- ===========================================

-- Verificar si el personaje Luxio existe
SELECT 
    char_name as 'Nombre del Personaje',
    accesslevel as 'Nivel de Acceso Actual',
    `level` as 'Nivel',
    classid as 'Clase ID',
    online as 'En Línea'
FROM characters 
WHERE char_name = 'Luxio';

-- Activar modo admin para Luxio (Nivel 5 = Owner)
UPDATE characters 
SET accesslevel = 5 
WHERE char_name = 'Luxio';

-- Verificar que se haya actualizado correctamente
SELECT 
    char_name as 'Nombre del Personaje',
    accesslevel as 'Nivel de Acceso Actual',
    `level` as 'Nivel',
    classid as 'Clase ID',
    online as 'En Línea'
FROM characters 
WHERE char_name = 'Luxio';

-- Mostrar mensaje de confirmación
SELECT '¡MODO ADMIN ACTIVADO PARA LUXIO!' as 'ESTADO',
       'Nivel de acceso: 5 (Owner)' as 'DETALLES',
       'Reinicia el servidor para aplicar cambios' as 'INSTRUCCIONES';

