-- ===========================================
-- OPTIMIZACIÓN ÉPICA DEL SERVIDOR - MEJOR SERVIDOR L2
-- ===========================================
-- Scripts SQL para optimizar el mejor servidor L2

-- Optimizar configuración de la base de datos
SET GLOBAL innodb_buffer_pool_size = 1073741824; -- 1GB
SET GLOBAL innodb_log_file_size = 268435456; -- 256MB
SET GLOBAL innodb_flush_log_at_trx_commit = 2;
SET GLOBAL innodb_flush_method = O_DIRECT;

-- Crear tabla para eventos épicos
CREATE TABLE IF NOT EXISTS eventos_epicos (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    nombre_evento VARCHAR(100) NOT NULL,
    tipo_evento VARCHAR(50) NOT NULL,
    tiempo_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tiempo_fin TIMESTAMP NULL,
    esta_activo BOOLEAN DEFAULT FALSE,
    participantes INT DEFAULT 0,
    recompensas_dadas INT DEFAULT 0
);

-- Crear tabla para estadísticas épicas
CREATE TABLE IF NOT EXISTS estadisticas_epicas (
    id_jugador INT PRIMARY KEY,
    nombre_jugador VARCHAR(35) NOT NULL,
    kills_totales INT DEFAULT 0,
    muertes_totales INT DEFAULT 0,
    daño_total BIGINT DEFAULT 0,
    curacion_total BIGINT DEFAULT 0,
    puntos_epicos INT DEFAULT 0,
    ultima_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Crear tabla para recompensas épicas
CREATE TABLE IF NOT EXISTS recompensas_epicas (
    id_recompensa INT AUTO_INCREMENT PRIMARY KEY,
    id_jugador INT NOT NULL,
    tipo_recompensa VARCHAR(50) NOT NULL,
    cantidad_recompensa INT NOT NULL,
    fecha_recompensa TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nombre_evento VARCHAR(100) NOT NULL
);

-- Insertar datos épicos iniciales para L2 Hermanos
INSERT INTO eventos_epicos (nombre_evento, tipo_evento, esta_activo) VALUES
('L2 HERMANOS - EVENTO ÉPICO DE BOSSES', 'BOSS', FALSE),
('L2 HERMANOS - EVENTO ÉPICO DE PVP', 'PVP', FALSE),
('L2 HERMANOS - EVENTO ÉPICO DE DROPS', 'DROP', FALSE);

-- Optimizar índices para mejor rendimiento
CREATE INDEX idx_estadisticas_epicas_jugador ON estadisticas_epicas(id_jugador);
CREATE INDEX idx_recompensas_epicas_jugador ON recompensas_epicas(id_jugador);
CREATE INDEX idx_recompensas_epicas_fecha ON recompensas_epicas(fecha_recompensa);
CREATE INDEX idx_eventos_epicos_activo ON eventos_epicos(esta_activo);

-- Crear procedimiento para limpiar datos antiguos
DELIMITER //
CREATE PROCEDURE LimpiarDatosEpicos()
BEGIN
    DELETE FROM recompensas_epicas WHERE fecha_recompensa < DATE_SUB(NOW(), INTERVAL 30 DAY);
    DELETE FROM estadisticas_epicas WHERE ultima_actualizacion < DATE_SUB(NOW(), INTERVAL 90 DAY);
    OPTIMIZE TABLE eventos_epicos, estadisticas_epicas, recompensas_epicas;
END //
DELIMITER ;

-- Crear evento para limpieza automática
CREATE EVENT IF NOT EXISTS limpieza_epica_automatica
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP
DO
  CALL LimpiarDatosEpicos();

-- Habilitar el scheduler de eventos
SET GLOBAL event_scheduler = ON;

-- Optimizar configuración de MySQL para el mejor servidor
SET GLOBAL query_cache_size = 134217728; -- 128MB
SET GLOBAL query_cache_type = ON;
SET GLOBAL max_connections = 1000;
SET GLOBAL thread_cache_size = 16;
SET GLOBAL table_open_cache = 4000;
SET GLOBAL tmp_table_size = 67108864; -- 64MB
SET GLOBAL max_heap_table_size = 67108864; -- 64MB

-- Crear tabla para logs épicos
CREATE TABLE IF NOT EXISTS epic_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    log_type VARCHAR(50) NOT NULL,
    log_message TEXT NOT NULL,
    log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    player_id INT NULL,
    event_id INT NULL
);

-- Insertar log inicial
INSERT INTO epic_logs (log_type, log_message) VALUES
('SYSTEM', 'EPIC SERVER OPTIMIZATION COMPLETED - MEJOR SERVIDOR L2 DE LA HISTORIA');

-- Crear vista para estadísticas épicas
CREATE VIEW epic_player_stats AS
SELECT 
    p.char_name,
    es.total_kills,
    es.total_deaths,
    es.epic_points,
    es.last_update
FROM characters p
LEFT JOIN epic_stats es ON p.obj_Id = es.player_id
WHERE p.online = 1;

-- Crear vista para eventos activos
CREATE VIEW epic_active_events AS
SELECT 
    event_name,
    event_type,
    start_time,
    participants,
    rewards_given
FROM epic_events
WHERE is_active = TRUE;

-- Optimizar tabla de characters para mejor rendimiento
ALTER TABLE characters ADD INDEX idx_char_online (online);
ALTER TABLE characters ADD INDEX idx_char_level (level);
ALTER TABLE characters ADD INDEX idx_char_class (classid);

-- Optimizar tabla de items para mejor rendimiento
ALTER TABLE items ADD INDEX idx_item_owner (owner_id);
ALTER TABLE items ADD INDEX idx_item_type (item_type);

-- Crear tabla para configuración épica
CREATE TABLE IF NOT EXISTS epic_config (
    config_key VARCHAR(100) PRIMARY KEY,
    config_value TEXT NOT NULL,
    config_type VARCHAR(50) DEFAULT 'STRING',
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insertar configuración épica inicial
INSERT INTO epic_config (config_key, config_value, config_type) VALUES
('EPIC_RATES_XP', '20.0', 'FLOAT'),
('EPIC_RATES_SP', '20.0', 'FLOAT'),
('EPIC_RATES_ADENA', '15.0', 'FLOAT'),
('EPIC_RATES_DROP', '12.0', 'FLOAT'),
('EPIC_STARTING_ADENA', '1000000', 'INT'),
('EPIC_STARTING_AA', '100000', 'INT'),
('EPIC_REGEN_MULTIPLIER', '300', 'INT'),
('EPIC_WYVERN_SPEED', '200', 'INT'),
('EPIC_STRIDER_SPEED', '180', 'INT'),
('EPIC_PVP_ZONE', '2', 'INT'),
('EPIC_GLOBAL_CHAT', 'GLOBAL', 'STRING'),
('EPIC_TRADE_CHAT', 'ON', 'STRING'),
('EPIC_HIGH_RATE_DROPS', 'TRUE', 'BOOLEAN'),
('EPIC_MULTIPLE_DROPS', 'TRUE', 'BOOLEAN');

-- Crear procedimiento para obtener configuración épica
DELIMITER //
CREATE PROCEDURE GetEpicConfig(IN config_key VARCHAR(100))
BEGIN
    SELECT config_value, config_type FROM epic_config WHERE config_key = config_key;
END //
DELIMITER ;

-- Crear procedimiento para actualizar configuración épica
DELIMITER //
CREATE PROCEDURE UpdateEpicConfig(IN config_key VARCHAR(100), IN config_value TEXT)
BEGIN
    INSERT INTO epic_config (config_key, config_value) 
    VALUES (config_key, config_value)
    ON DUPLICATE KEY UPDATE config_value = config_value;
END //
DELIMITER ;

-- Crear tabla para rankings épicos
CREATE TABLE IF NOT EXISTS epic_rankings (
    ranking_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    player_name VARCHAR(35) NOT NULL,
    ranking_type VARCHAR(50) NOT NULL,
    ranking_value INT NOT NULL,
    ranking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_ranking (player_id, ranking_type)
);

-- Crear índices para rankings
CREATE INDEX idx_epic_rankings_type ON epic_rankings(ranking_type);
CREATE INDEX idx_epic_rankings_value ON epic_rankings(ranking_value);
CREATE INDEX idx_epic_rankings_date ON epic_rankings(ranking_date);

-- Crear procedimiento para actualizar rankings
DELIMITER //
CREATE PROCEDURE UpdateEpicRanking(IN player_id INT, IN player_name VARCHAR(35), IN ranking_type VARCHAR(50), IN ranking_value INT)
BEGIN
    INSERT INTO epic_rankings (player_id, player_name, ranking_type, ranking_value) 
    VALUES (player_id, player_name, ranking_type, ranking_value)
    ON DUPLICATE KEY UPDATE ranking_value = ranking_value, ranking_date = CURRENT_TIMESTAMP;
END //
DELIMITER ;

-- Crear vista para top rankings
CREATE VIEW epic_top_rankings AS
SELECT 
    ranking_type,
    player_name,
    ranking_value,
    ranking_date
FROM epic_rankings
ORDER BY ranking_type, ranking_value DESC;

-- Optimizar configuración final
SET GLOBAL innodb_adaptive_hash_index = ON;
SET GLOBAL innodb_change_buffering = all;
SET GLOBAL innodb_io_capacity = 2000;
SET GLOBAL innodb_read_io_threads = 8;
SET GLOBAL innodb_write_io_threads = 8;

-- Insertar log de finalización
INSERT INTO epic_logs (log_type, log_message) VALUES
('SYSTEM', 'EPIC SERVER DATABASE OPTIMIZATION COMPLETED - MEJOR SERVIDOR L2 DE LA HISTORIA x20');

-- Mostrar resumen de optimización
SELECT 'EPIC SERVER OPTIMIZATION COMPLETED' AS Status,
       'MEJOR SERVIDOR L2 DE LA HISTORIA x20' AS Description,
       NOW() AS Completion_Time;
