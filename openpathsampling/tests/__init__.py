import os

from openpathsampling.storage import Storage

import openpathsampling.engines.openmm as peng

import mdtraj as md

from test_helpers import data_filename

def setup_package():
    # this should generate the trajectory.nc file which we'll use for
    # everything else
    mdtrajectory = md.load(data_filename("ala_small_traj.pdb"))

    snapshot = peng.snapshot_from_pdb(data_filename("ala_small_traj.pdb"))

    # print snapshot.__dict__
    # print snapshot.engine.__dict__

    # once we have a template configuration (coordinates to not really matter)
    # we can create a storage. We might move this logic out of the dynamics engine
    # and keep sotrage and engine generation completely separate!

    storage = Storage(
        filename=data_filename("ala_small_traj.nc"),
        template=snapshot,
        mode='w'
    )

    mytraj = peng.trajectory_from_mdtraj(mdtrajectory, simple_topology=True)
    storage.trajectories.save(mytraj)

    storage.close()


def teardown_package():
    if os.path.isfile(data_filename("ala_small_traj.nc")):
        os.remove(data_filename("ala_small_traj.nc"))
