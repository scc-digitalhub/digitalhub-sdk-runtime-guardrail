# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_guardrail.entities.run._base.entity import RunGuardrailRun

if typing.TYPE_CHECKING:
    from digitalhub_runtime_guardrail.entities.run.serve.spec import RunSpecGuardrailRunServe
    from digitalhub_runtime_guardrail.entities.run.serve.status import RunStatusGuardrailRunServe


class RunGuardrailRunServe(RunGuardrailRun):
    """
    RunGuardrailRunServe class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecGuardrailRunServe
        self.status: RunStatusGuardrailRunServe
