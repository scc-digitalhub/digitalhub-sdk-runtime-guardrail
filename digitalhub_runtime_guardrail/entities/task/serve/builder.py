# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.builder import TaskBuilder

from digitalhub_runtime_guardrail.entities._base.runtime_entity.builder import RuntimeEntityBuilderGuardrail
from digitalhub_runtime_guardrail.entities._commons.enums import EntityKinds
from digitalhub_runtime_guardrail.entities.task.serve.entity import TaskGuardrailServe
from digitalhub_runtime_guardrail.entities.task.serve.spec import TaskSpecGuardrailServe, TaskValidatorGuardrailServe
from digitalhub_runtime_guardrail.entities.task.serve.status import TaskStatusGuardrailServe


class TaskGuardrailServeBuilder(TaskBuilder, RuntimeEntityBuilderGuardrail):
    """
    TaskGuardrailServeBuilder serveer.
    """

    ENTITY_CLASS = TaskGuardrailServe
    ENTITY_SPEC_CLASS = TaskSpecGuardrailServe
    ENTITY_SPEC_VALIDATOR = TaskValidatorGuardrailServe
    ENTITY_STATUS_CLASS = TaskStatusGuardrailServe
    ENTITY_KIND = EntityKinds.TASK_GUARDRAIL_SERVE.value
