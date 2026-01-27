# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum


class EntityKinds(Enum):
    """
    Entity kinds.
    """

    FUNCTION_GUARDRAIL = "guardrail"
    TASK_GUARDRAIL_BUILD = "guardrail+build"
    TASK_GUARDRAIL_SERVE = "guardrail+serve"
    RUN_GUARDRAIL_BUILD = "guardrail+build:run"
    RUN_GUARDRAIL_SERVE = "guardrail+serve:run"


class Actions(Enum):
    """
    Task actions.
    """

    BUILD = "build"
    SERVE = "serve"
