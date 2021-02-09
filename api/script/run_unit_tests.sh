#! /usr/bin/env bash

# should be run from top-level directory in repo
main() {
  app_directory=$(pwd)/api
  test_directory="${app_directory}/test"
  PYTHONPATH="${app_directory}" python -m pytest "${test_directory}"
}

main