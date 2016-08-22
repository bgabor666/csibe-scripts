#!/bin/bash

#source /home/bgabor/.bashrc

export PATH=/home/bgabor/work/csibe/sandbox/cmake/cmake-3.5.2/bin:$PATH

echo `which cmake` > /home/bgabor/work/csibe/sandbox/clang-trunk/build/csibe-cron-job.log

cd /home/bgabor/work/csibe/sandbox/clang-trunk/build

/home/bgabor/work/csibe/sandbox/clang-trunk/build/create-and-upload-csibe-results.py > /home/bgabor/work/csibe/sandbox/clang-trunk/build/create-and-upload-csibe-results.log 2>&1
