#!/usr/bin/python3
# -*- coding: utf-8 -*-


import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
 
def test_grafana_http(host):
	cmd = host.run("curl -v http://127.0.0.1:3000")
	assert cmd.succeeded
	assert "/login" in cmd.stdout
	assert "Found" in cmd.stdout

def test_influxdb(host) :
	def run(command) :
		cmd = host.run(command)
		assert cmd.succeeded
	run("influx -version")
	run("influx -execute 'CREATE DATABASE apollo13'")
	run("influx -database apollo13 -execute 'INSERT thermo,location=space temperature=22 5'")
	run("influx -database apollo13 -execute 'INSERT thermo,location=space temperature=23 6'")
	cmd = host.run("influx -database apollo13 -execute 'SELECT * FROM thermo;'")
	assert cmd.succeeded
	lines = cmd.stdout.split("\n")
	print(lines)
	def assert_line(loc, time, temperature) :
		loc, time, temperature = str(loc), str(time), str(temperature)
		for line in lines :
			if loc in line and time in line and temperature in line : return
		assert False
	assert_line('space', 5, 22)
	assert_line('space', 6, 23)
