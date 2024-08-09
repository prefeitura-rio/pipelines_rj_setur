SELECT
  SAFE_CAST(ano AS INT64) as ano,
  SAFE_CAST(categoria as STRING) as categoria,
  SAFE_CAST(SAFE_CAST(admitidos AS FLOAT64) AS INT64) as admitidos,
  SAFE_CAST(SAFE_CAST(desligados AS FLOAT64) AS INT64) as desligados,
  SAFE_CAST(SAFE_CAST(saldo AS FLOAT64) AS INT64) as saldo,
  SAFE_CAST(obs as STRING) as observacao
FROM `rj-setur.turismo_fluxo_visitantes_staging.caged`