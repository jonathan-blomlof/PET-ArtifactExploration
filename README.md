# Artifact exploration

## Background

This repository is forked from a [Fully homomorphic private segmented membership test implementation](https://github.com/tjungND/caoe-cerberus-query). Such homomorphic membership tests may genereate false positives, i.e. the protocol claims a set intersection exists when there is no such intersection.

This repository tests for how common such false positve errors are by producing situations inwhich no intersection exists and looks for how often the protocol states an intersection exists.

## Modifications
The dependecy script has been modified. The exact results of this modifcation is unkown to me, but it allows the dependency script to run on my WSL.

## Setup and run

This repository is only suitable for Linux-systems (WSL should work). 

First, gather all dependencies by running `sudo ./dependencies.sh`.

Then execute the test with `python examine_false_positve_rate.py [upperlimit]`.
The upperlimit is optional. If none are given the program runs until it is interuppted by the user.


## Noteworthy problems
In essence the repository is made for linux-systems. On my machine, Windows has a *terrible* routine of converting '\n' into '\r\n' which may break some scripts. 