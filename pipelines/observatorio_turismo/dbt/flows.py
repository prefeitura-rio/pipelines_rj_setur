# -*- coding: utf-8 -*-
"""
DBT-related flows.
"""

from copy import deepcopy

from prefect.run_configs import KubernetesRun
from prefect.storage import GCS
from prefeitura_rio.pipelines_utils.prefect import set_default_parameters
from prefeitura_rio.pipelines_utils.state_handlers import (
    handler_initialize_sentry,
    handler_inject_bd_credentials,
)

from pipelines.constants import constants
from pipelines.observatorio_turismo.dbt.schedules import (
    setur_seeketing_daily_update_schedule,
)
from prefeitura_rio.pipelines_templates.run_dbt_model.flows import templates__run_dbt_model__flow as utils_run_dbt_model_flow

dbt_setur_seeketing = deepcopy(utils_run_dbt_model_flow)
dbt_setur_seeketing.name = "SETUR: Seeketing - Materializar tabelas"
dbt_setur_seeketing.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
dbt_setur_seeketing.run_config = KubernetesRun(image=constants.DOCKER_IMAGE.value)

setur_seeketing_default_parameters = {
    "dataset_id": "turismo_fluxo_visitantes",
    "upstream": True,
}
dbt_setur_seeketing = set_default_parameters(
    dbt_setur_seeketing,
    default_parameters=setur_seeketing_default_parameters,
)

dbt_setur_seeketing.schedule = setur_seeketing_daily_update_schedule
