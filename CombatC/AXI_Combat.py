# AXI Combat
# Copyright (C) 2020 Louis Zhang
# Copyright (C) 2020 AgentX Industries
# AXI Combat is released under the GNU General Public License v3 or above.

import multiprocessing as mp
import OpsConv
import Multi

if __name__ == "__main__":
    mp.freeze_support()
    OpsConv.genInfo()
    Multi.run()
