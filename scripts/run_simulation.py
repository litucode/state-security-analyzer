#!/usr/bin/env python
# Script to run simulations from the command line

import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import and run the simulation
from core.simulation.engine import run_simulation

if __name__ == '__main__':
    run_simulation()