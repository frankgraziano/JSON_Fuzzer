#!/bin/bash

#This is just a basic test harness to show how you can feed the output of the fuzzer directly into a JSON parser of your choice.
while true;
do
	python ./json_fuzzer.py | ./jsonparser
done
