#!/usr/bin/env python3

###################################################
#
# file: plot_memusage.py
#
# @Author:   Iacovos G. Kolokasis
# @Version:  10-04-2024
# @email:    kolokasis@ics.forth.gr
#
# Plot the memory usage of a process including
# used and page cache memory
#
###################################################

import optparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import config
import os

# Parse input arguments
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage=usage)
parser.add_option("-i", "--input", dest="input", metavar="FILE", help="Input file")
parser.add_option("-o", "--outputPath", metavar="PATH", dest="outputPath", default="output.svg", help="Output Path")
(options, args) = parser.parse_args()

#if not os.path.exists(options.outputPath):
#    os.makedirs(options.outputPath)

# Open input file 
inputFile = open(options.input, 'r')

used_mem = []
page_cache_mem = []

for line in inputFile.readlines():
    # Split the line into individual columns based on whitespace
    columns = line.strip().split()

    if columns[0] == "total":
        continue

    if columns[0] == "Swap:":
        continue

    used_mem.append(int(columns[2]))
    page_cache_mem.append(int(columns[5]))

# Plot figure with fix size
fig, ax = plt.subplots(figsize=config.fullfigsize)

# Grid
plt.grid(True, linestyle='--', color='grey', zorder=0)

# Prepare x-axis data
time = range(1, len(used_mem) + 1)

plt.plot(time, used_mem, color=config.B_color_cycle[0],
         label='Used memory', zorder=2)
plt.plot(time, page_cache_mem, color=config.B_color_cycle[1],
         label='Page cache memory', zorder=2)

# Axis name
plt.ylabel('Memory (GB)', ha="center")
plt.xlabel('Time (s)')

# Legend
plt.legend(loc='upper right', bbox_to_anchor=(0.65, 1.25), ncol=2)


# Save figure
plt.savefig('%s/mem_usage.png' % options.outputPath, bbox_inches='tight')
