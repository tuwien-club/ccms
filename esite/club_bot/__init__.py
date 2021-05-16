# myapp/_init_.py
import os
import sys

if os.environ.get("RUN_MAIN", None) != "true" and (
    "manage.py" not in sys.argv or "runserver" in sys.argv
):
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    default_app_config = "esite.club_bot.apps.ClubBotConfig"

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2020 miraculix-org Florian Kleber
