# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Protocol

from pydantic import BaseModel  # noqa: F401

from pyopenapi import webmethod  # noqa: F401


class Models(Protocol): ...
