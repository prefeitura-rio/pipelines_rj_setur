  SELECT
    CASE
        WHEN ferramenta_turistica = "cristo_redentor" THEN "Cristo Redentor"
        WHEN ferramenta_turistica = "pao_de_acucar" THEN "Pão de Açúcar"
        WHEN ferramenta_turistica = "selaron" THEN "Escadaria Selarón"
        WHEN ferramenta_turistica = "ccbb_correios" THEN "CCBB Correios"
        WHEN ferramenta_turistica = "praia_de_copacabana_leme" THEN "Praias de Copacabana e Leme"
        WHEN ferramenta_turistica = "jardim_botanico" THEN "Jardim Botânico"
        WHEN ferramenta_turistica = "catedral_metropolitana" THEN "Catedral Metropolitana"
        WHEN ferramenta_turistica = "maracana" THEN "Maracanã"
        WHEN ferramenta_turistica = "pequena_africa" THEN "Centro Cultural Pequena África"    
        ELSE ferramenta_turistica 
    END nome,
    `rj-setur.turismo_fluxo_visitantes`.geolocate_sight(ferramenta_turistica)[0] as latitude,
    `rj-setur.turismo_fluxo_visitantes`.geolocate_sight(ferramenta_turistica)[1] as longitude,
    ST_GEOGPOINT(`rj-setur.turismo_fluxo_visitantes`.geolocate_sight(ferramenta_turistica)[1], `rj-setur.turismo_fluxo_visitantes`.geolocate_sight(ferramenta_turistica)[0]) as ferramenta_turistica_coordenadas
FROM `rj-setur.turismo_fluxo_visitantes_staging.claro_atrativos`