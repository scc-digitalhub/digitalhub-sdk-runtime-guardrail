# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

import requests
from digitalhub.utils.exceptions import EntityError

from digitalhub_runtime_guardrail.entities.run._base.entity import RunGuardrailRun

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata

    from digitalhub_runtime_guardrail.entities.run.serve.spec import RunSpecGuardrailRunServe
    from digitalhub_runtime_guardrail.entities.run.serve.status import RunStatusGuardrailRunServe


class RunGuardrailRunServe(RunGuardrailRun):
    """
    RunGuardrailRunServe class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: RunSpecGuardrailRunServe,
        status: RunStatusGuardrailRunServe,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: RunSpecGuardrailRunServe
        self.status: RunStatusGuardrailRunServe