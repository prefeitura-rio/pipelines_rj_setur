SELECT
  SAFE_CAST(mes_ano AS DATE FORMAT "DD/MM/YYYY") as data,
  ROUND(SAFE_CAST(REPLACE(tx_de_ocupacao_, ",", ".") AS FLOAT64)/100,4) as taxa_ocupacao
FROM `rj-setur.turismo_fluxo_visitantes_staging.rede_hoteleira_ocupacao_geral`