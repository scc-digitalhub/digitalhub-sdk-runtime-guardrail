# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_guardrail.entities.run._base.entity import RunGuardrailRun

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata

    from digitalhub_runtime_guardrail.entities.run.build.spec import RunSpecGuardrailRunBuild
    from digitalhub_runtime_guardrail.entities.run.build.status import RunStatusGuardrailRunBuild


class RunGuardrailRunBuild(RunGuardrailRun):
    """
    RunGuardrailRunBuild class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: RunSpecGuardrailRunBuild,
        status: RunStatusGuardrailRunBuild,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: RunSpecGuardrailRunBuild
        self.status: RunStatusGuardrailRunBuild
