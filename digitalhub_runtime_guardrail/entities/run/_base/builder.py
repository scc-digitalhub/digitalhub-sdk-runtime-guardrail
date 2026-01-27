# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.builder import RunBuilder

from digitalhub_runtime_guardrail.entities._base.runtime_entity.builder import RuntimeEntityBuilderGuardrail
from digitalhub_runtime_guardrail.entities._commons.enums import EntityKinds
from digitalhub_runtime_guardrail.entities.run._base.entity import RunGuardrailRun
from digitalhub_runtime_guardrail.entities.run._base.spec import RunSpecGuardrailRun, RunValidatorGuardrailRun
from digitalhub_runtime_guardrail.entities.run._base.status import RunStatusGuardrailRun


class RunGuardrailRunBuilder(RunBuilder, RuntimeEntityBuilderGuardrail):
    """
    RunGuardrailRunBuilder runer.
    """

    ENTITY_CLASS = RunGuardrailRun
    ENTITY_SPEC_CLASS = RunSpecGuardrailRun
    ENTITY_SPEC_VALIDATOR = RunValidatorGuardrailRun
    ENTITY_STATUS_CLASS = RunStatusGuardrailRun
    ENTITY_KIND = EntityKinds.RUN_GUARDRAIL.value
