# -*- coding: utf-8 -*-
"""
Schedules for the database dump pipeline
"""

from datetime import datetime, timedelta

from prefect.schedules import Schedule
from prefect.schedules.clocks import IntervalClock
import pytz

from pipelines.constants import constants
from prefeitura_rio.pipelines_utils.io import untuple_clocks as untuple

from pipelines_rj_setur.pipelines.observatorio_turismo.dbt.utils import generate_dbt_schedules

#####################################
#
# SETUR Seeketing Schedules
#
#####################################

setur_observatorio_turismo_parameters = {
    "aeroportos": {
        "dataset_id": "equipamentos",
    },
    "rodoviaria": {
        "dataset_id": "equipamentos",
    },
    "museus_visitas": {
        "dataset_id": "equipamentos",
    },
    "rede_hoteleira_ocupacao_geral": {
        "dataset_id": "equipamentos",
    },
    "rede_hoteleira_ocupacao_grandes_eventos": {
        "dataset_id": "equipamentos",
        "materialize_to_datario": True,
    },
    "pontos_turisticos_visitas": {
        "dataset_id": "equipamentos",
    },
    "pontos_turisticos": {
        "dataset_id": "dados_mestres",
    },
    # "origem_visitacao": {
    #     "dataset_id": "equipamentos",
    # },
    # "atrativos_turistas": {
    #     "dataset_id": "equipamentos",
    # },
    # "atrativos_visitantes": {
    #     "dataset_id": "equipamentos",
    # },
    "caged": {
        "dataset_id": "receita",
    },
    "empregos_turismo": {
        "dataset_id": "receita",
    },
    "iss_turistico": {
        "dataset_id": "receita",
    },
}

setur_seeketing_clocks = generate_dbt_schedules(
    interval=timedelta(days=1),
    runs_interval_minutes=1,
    start_date=datetime(2023, 3, 28, 17, 30, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_SETUR_AGENT_LABEL.value,
    ],
    table_parameters=setur_observatorio_turismo_parameters,
)

setur_seeketing_daily_update_schedule = Schedule(clocks=untuple(setur_seeketing_clocks))
