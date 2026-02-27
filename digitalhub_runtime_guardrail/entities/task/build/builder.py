# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.builder import TaskBuilder

from digitalhub_runtime_guardrail.entities._base.runtime_entity.builder import RuntimeEntityBuilderGuardrail
from digitalhub_runtime_guardrail.entities._commons.enums import EntityKinds
from digitalhub_runtime_guardrail.entities.task.build.entity import TaskGuardrailBuild
from digitalhub_runtime_guardrail.entities.task.build.spec import TaskSpecGuardrailBuild, TaskValidatorGuardrailBuild
from digitalhub_runtime_guardrail.entities.task.build.status import TaskStatusGuardrailBuild


class TaskGuardrailBuildBuilder(TaskBuilder, RuntimeEntityBuilderGuardrail):
    """
    TaskGuardrailBuild builder.
    """

    ENTITY_CLASS = TaskGuardrailBuild
    ENTITY_SPEC_CLASS = TaskSpecGuardrailBuild
    ENTITY_SPEC_VALIDATOR = TaskValidatorGuardrailBuild
    ENTITY_STATUS_CLASS = TaskStatusGuardrailBuild
    ENTITY_KIND = EntityKinds.TASK_GUARDRAIL_BUILD.value
