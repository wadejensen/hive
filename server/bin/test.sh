#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

REPO_ROOT="$(git rev-parse --show-toplevel)"
SERVER_HOME="${REPO_ROOT}/server"

main() {
  cd "${REPO_ROOT}"
  python3 "${SERVER_HOME}/tests/test.py"
}

main "$@"
