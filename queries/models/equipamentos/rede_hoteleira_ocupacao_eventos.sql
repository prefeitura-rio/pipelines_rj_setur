SELECT
  TRIM(ano) as ano,
  SAFE_CAST(data_inicial as DATE FORMAT "DD/MM/YYYY") as data_inicial,
  SAFE_CAST(data_final as DATE FORMAT "DD/MM/YYYY") as data_final,
  TRIM(evento) as evento,
  ROUND(SAFE_CAST(REPLACE(tx_de_ocupacao_, ",", ".") AS FLOAT64)/100,4) as taxa_ocupacao,
FROM `rj-setur.turismo_fluxo_visitantes_staging.rede_hoteleira_ocupacao_grandes_eventos`