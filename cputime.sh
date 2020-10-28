#!/bin/bash

#This script returns the maximum CPU time for given job name, in case no job name is provided it return the longest CPU time.

#Checks if the Job Name was provided. If yes continues executing if statement - otherwise executes else statemenet. 
if [ ! -z $1 ] 
then
	#Given Job Name finds a maximum CPU time and assigns the output to a variable cpu_time.
	#Fist finds files containg the given job name, extracting the file name form the output.
	#Searches for CPU time data in the filtered files and sorts the time data. 
	#Chosses the longest CPU time, isolates the time data and stors the output to the variable cpu_time.
	cpu_time=$(grep $1 * | grep "Job Name: " | cut -d ":" -f1 | xargs cat | grep "cput" | sort | tail -1 | awk -F '[=,]' '{print $2}')
	echo "CPU time of " $cpu_time " for job " $1 
else
	#Searches and isolates the CPU time data. Sorts and assingns the longest time to the variable max_time.
	#Using the max_time searches for the belonging job name and saves it the the variable job_name_max. 
	max_time=$(grep 'cput' * | awk -F '[=,]' '{print $2}' | sort | tail -1)
	job_name_max=$(egrep -lr $max_time * | xargs  cat | grep "Job Name: " | cut -d ":" -f2)
	echo "Maximum CPU time of " $max_time " for job " $job_name_max
fi




