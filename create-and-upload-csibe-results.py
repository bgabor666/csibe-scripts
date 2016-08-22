#!/usr/bin/env python

import os
import shutil
import subprocess
import time

csibe_buildbot_base_dir = "/home/bgabor/work/csibe/sandbox/clang-trunk"
csibe_base_dir = os.path.join(csibe_buildbot_base_dir, "csibe")
build_dir = os.path.join(csibe_buildbot_base_dir, "build")
results_dir = os.path.join(build_dir, "build")
upload_dir = os.path.join(results_dir, "csibe-results")


# Build directories.
x86_64_build_dir = os.path.join(build_dir, "build/clang-trunk-native")
cortex_m0_build_dir = os.path.join(build_dir, "build/clang-trunk-cortex-m0")
cortex_m4_build_dir = os.path.join(build_dir, "build/clang-trunk-cortex-m4")

build_directories = [x86_64_build_dir, cortex_m0_build_dir, cortex_m4_build_dir]

# Clean the previous build
for build_directory in build_directories:
    shutil.rmtree(build_directory, ignore_errors=True)


# Call csibe.py
subprocess.call(
    [os.path.join(csibe_base_dir, "csibe.py"),
     "clang-trunk-native",
     "clang-trunk-cortex-m0",
     "clang-trunk-cortex-m4",
     "CSiBE-v2.1.1",
     "--build-dir {}".format(results_dir)])

# Result directories
x86_64_base_dir = os.path.join(build_dir, "build/csibe-results/clang-trunk-x86_64")
cortex_m0_base_dir = os.path.join(build_dir, "build/csibe-results/clang-trunk-cortex-m0")
cortex_m4_base_dir = os.path.join(build_dir, "build/csibe-results/clang-trunk-cortex-m4")

target_directories = [x86_64_base_dir, cortex_m0_base_dir, cortex_m4_base_dir]

# Create benchmark directories for the current date
date_dir = time.strftime("%Y/%m")
date_file = time.strftime("%Y-%m-%d")

for target_dir in target_directories:
    if not os.path.isdir(os.path.join(target_dir, date_dir)):
        os.makedirs(os.path.join(target_dir, date_dir))

# Copy result files with date and target in the name of the new file
shutil.copyfile(os.path.join(x86_64_build_dir, "all_results.csv"),
                os.path.join(x86_64_base_dir, date_dir, "{}-clang-trunk-x86_64-results.csv".format(date_file)))

shutil.copyfile(os.path.join(cortex_m0_build_dir, "all_results.csv"),
                os.path.join(cortex_m0_base_dir, date_dir, "{}-clang-trunk-cortex-m0-results.csv".format(date_file)))

shutil.copyfile(os.path.join(cortex_m4_build_dir, "all_results.csv"),
                os.path.join(cortex_m4_base_dir, date_dir, "{}-clang-trunk-cortex-m4-results.csv".format(date_file)))


subprocess.call(
    ["git",
     "-C",
     upload_dir,
     "add",
     "--all"])

subprocess.call(
    ["git",
     "-C",
     upload_dir,
     "commit",
     "-m",
     "Add {} results".format(date_file)])

subprocess.call(
    ["git",
     "-C",
     upload_dir,
     "push"])

