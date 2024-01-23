#!/bin/bash

pyinstaller \
  --distpath release \
  --workpath build \
  --noconfirm \
  --clean \
  --onefile \
  --name GRPSlave \
  grp_slave/__main__.py
