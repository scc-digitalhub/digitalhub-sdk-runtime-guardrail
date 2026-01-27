# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from digitalhub_runtime_guardrail.entities._commons.enums import EntityKinds
from digitalhub_runtime_guardrail.entities.function.guardrail.builder import FunctionGuardrailBuilder
from digitalhub_runtime_guardrail.entities.run.serve.builder import RunGuardrailRunServeBuilder
from digitalhub_runtime_guardrail.entities.task.serve.builder import TaskGuardrailServeBuilder

entity_builders = (
    (EntityKinds.FUNCTION_GUARDRAIL.value, FunctionGuardrailBuilder),
    (EntityKinds.TASK_GUARDRAIL_SERVE.value, TaskGuardrailServeBuilder),
    (EntityKinds.RUN_GUARDRAIL_SERVE.value, RunGuardrailRunServeBuilder),
)

try:
    from digitalhub_runtime_guardrail.runtimes.builder import RuntimeGuardrailBuilder

    runtime_builders = ((kind, RuntimeGuardrailBuilder) for kind in [e.value for e in EntityKinds])
except ImportError:
    runtime_builders = tuple()
