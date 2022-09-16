




# Preguntas:
###########################
-- Año con más carreras
###########################

SELECT COUNT(raceId) as cantVeces, `year`, raceId
	FROM races
	GROUP BY `year`
    ORDER BY 1 DESC
    LIMIT 1;

########################################################
-- Piloto con mayor cantidad de primeros puestos
########################################################
-- CONVERSION DE VARCHAR A INT
ALTER TABLE `qualify` CHANGE `position` `position` INT NOT NULL;

SELECT dri.name,COUNT(dri.driverId) as cantidad, qua.position
    FROM drivers dri
    JOIN qualify qua
	ON (dri.driverId = qua.driverId)
    WHERE qua.position = 1;

SELECT COUNT(qualifyId) as cant FROM qualify GROUP BY qualify.position ORDER BY cant DESC;

#####################################
-- Nombre del circuito más corrido
#####################################

-- CONVERSION DE VARCHAR A INT
-- ALTER TABLE `races` CHANGE `round` `round`INT(2) NOT NULL;
-- SELECT * FROM qualify;

SELECT ci.name, MAX(ra.round) as maxCantidad
	FROM races ra
	JOIN circuits ci
    ON (ra.circuitId = ci.circuitId);
-- 'Albert Park Grand Prix Circuit', '23'

#############################################################################################################
-- Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
##############################################################################################################
-- CONVERSION DE UNIDADES
-- ALTER TABLE `results` CHANGE `points` `points`DECIMAL NOT NULL;


-- LIMPIEZA DE STRINGS
-- UPDATE `drivers` SET `name` = REPLACE(name,"{'forename': '","");
-- UPDATE `drivers` SET `name` = REPLACE(name,"'}","");
-- UPDATE `drivers` SET `name` = REPLACE(name,"', 'surname': '"," ");
-- SELECT DISTINCT(points) FROM results;
-- SELECT * FROM drivers;

SELECT MAX(re.points) as max_cant_points, dri.name, co.nationality
	FROM results re
    JOIN constructors co
    ON (re.constructorId = co.constructorId)
    JOIN drivers dri
    ON (re.driverId = dri.driverId)
	WHERE co.nationality IN ('American','British')
    ORDER BY re.points DESC;
-- 'Lewis Hamilton'

