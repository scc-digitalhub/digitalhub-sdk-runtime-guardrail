# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.runtime_entity.builder import RuntimeEntityBuilder
from digitalhub.entities._commons.utils import map_actions

from digitalhub_runtime_guardrail.entities._commons.enums import Actions, EntityKinds


class RuntimeEntityBuilderGuardrail(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_GUARDRAIL.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_GUARDRAIL_BUILD.value,
                Actions.BUILD.value,
            ),
            (
                EntityKinds.TASK_GUARDRAIL_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_GUARDRAIL_BUILD.value,
                Actions.BUILD.value,
            ),
            (
                EntityKinds.RUN_GUARDRAIL_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
