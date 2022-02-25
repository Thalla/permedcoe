#!/usr/bin/env bash

data_dir=$1
solver_name=$2
penalty=$3
tol=$4
maxtime=$5
outfile=$6
outfile2=$7

tmp_dir=$(mktemp -d)
cp -R ${data_dir}/* ${tmp_dir}/
/opt/miniconda/bin/python /opt/carnival/carnivalpy/carnival.py $tmp_dir --solver $solver_name --penalty $penalty --maxtime $maxtime --tol $tol --export ${tmp_dir}/solution.csv
Rscript --vanilla /opt/export.R $tmp_dir $outfile $outfile2
