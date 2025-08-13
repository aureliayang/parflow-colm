import sys
sys.path.append("/home/parflow/software/install_software/parflow-3.12/gnu9.4.0/parflow-3.12.0/py-env/lib/python3.8/site-packages")
import os
import numpy as np
from parflow import Run 
import shutil
from parflow.tools.fs import mkdir, cp, get_absolute_path, exists
from parflow.tools.settings import set_working_directory

# Name your ParFLow run -- note that all of your output files will have this prefix
runname = 'a2'

# Create a directory in the outputs folder for this run
run_dir = get_absolute_path(f'outputs/{runname}')
mkdir(run_dir)
print(run_dir)

# create your Parflow model object. For starters we are just goin to set the file version and the run directory we'll add more later
# note that the model will run from the run_dir so all input files should be in the run dir or paths should be specified relative to run_dir
model = Run(runname, run_dir)
model.FileVersion = 4

#copy the model inputs for the simulation into the run directory
#NOTE: you dont have to copy everything into the run directory if you don't want, you can also point to input files in other directories in a simulation if you prefer
input_dir= os.path.join(os.getcwd(), 'model_inputs')
files=os.listdir(input_dir)
for fname in files:
    shutil.copy(os.path.join(input_dir,fname), run_dir)

    # Processor topology: This is the way that the problem will be split across processors if you want to run in parallel
# The domain is divided in x,y and z dimensions by P, Q and R. The total number of processors is P*Q*R.
model.Process.Topology.P = 3
model.Process.Topology.Q = 2
model.Process.Topology.R = 1

#Locate the origin in the domain.
model.ComputationalGrid.Lower.X = 0.0
model.ComputationalGrid.Lower.Y = 0.0
model.ComputationalGrid.Lower.Z = 0.0

# Define the size of each grid cell. The length units are the same as those on hydraulic conductivity, here that is meters.
model.ComputationalGrid.DX = 961.7186994
model.ComputationalGrid.DY = 961.7186994
model.ComputationalGrid.DZ = 200.0

# Define the number of grid blocks in the domain.
model.ComputationalGrid.NX = 252
model.ComputationalGrid.NY = 146
model.ComputationalGrid.NZ = 11

#Declare the geometries that you will use for the problem
model.GeomInput.Names = "box_input indi_input"

#Define the solid_input geometry.  
#Note the naming convention here GeomInput.{GeomName}.key
model.GeomInput.box_input.InputType = "Box"
model.GeomInput.box_input.GeomName = "domain"
model.Geom.domain.Lower.X = 0.0
model.Geom.domain.Lower.Y = 0.0
model.Geom.domain.Lower.Z = 0.0
model.Geom.domain.Upper.X = 961.7186994*252
model.Geom.domain.Upper.Y = 961.7186994*146
model.Geom.domain.Upper.Z = 200.0*11

#First set the name for your `Domain` and setup the patches for this domain
model.Domain.GeomName = "domain"
model.Geom.domain.Patches = "left right front back bottom top"

model.GeomInput.indi_input.InputType =   "IndicatorField"
model.GeomInput.indi_input.GeomNames = "s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 g1 g2 g3 g4 g5 g6 g7 g8 g9 g10"
model.Geom.indi_input.FileName = "indicator_a2.pfb"

model.GeomInput.s1.Value =    1
model.GeomInput.s2.Value =    2
model.GeomInput.s3.Value =    3
model.GeomInput.s4.Value =    4
model.GeomInput.s5.Value =    5
model.GeomInput.s6.Value =    6
model.GeomInput.s7.Value =    7
model.GeomInput.s8.Value =    8
model.GeomInput.s9.Value =    9
model.GeomInput.s10.Value =   10
model.GeomInput.s11.Value =   11
model.GeomInput.s12.Value =   12
model.GeomInput.s13.Value =   13

model.GeomInput.g1.Value =    19
model.GeomInput.g2.Value =    20
model.GeomInput.g3.Value =    21
model.GeomInput.g4.Value =    22
model.GeomInput.g5.Value =    23
model.GeomInput.g6.Value =    24
model.GeomInput.g7.Value =    25
model.GeomInput.g8.Value =    26
model.GeomInput.g9.Value =    27
model.GeomInput.g10.Value =    28

model.Solver.Nonlinear.VariableDz = True
model.dzScale.GeomNames = "domain"
model.dzScale.Type = "nzList"
model.dzScale.nzListNumber = 11

# model.Cell._0.dzScale.Value = 1.5
# model.Cell._1.dzScale.Value = 0.5
# model.Cell._2.dzScale.Value = 0.25
# model.Cell._3.dzScale.Value = 0.125
# model.Cell._4.dzScale.Value = 0.05
# model.Cell._5.dzScale.Value = 0.025
# model.Cell._6.dzScale.Value = 0.005
# model.Cell._7.dzScale.Value = 0.003
# model.Cell._8.dzScale.Value = 0.0015
# model.Cell._9.dzScale.Value = 0.0005
model.Cell._0.dzScale.Value = 100/200
model.Cell._1.dzScale.Value = (3.4331-2.2961)/200
model.Cell._2.dzScale.Value = (2.2961-1.3828)/200
model.Cell._3.dzScale.Value = (1.3828-0.8289)/200
model.Cell._4.dzScale.Value = (0.8289-0.4929)/200
model.Cell._5.dzScale.Value = (0.4929-0.2891)/200
model.Cell._6.dzScale.Value = (0.2891-0.1655)/200
model.Cell._7.dzScale.Value = (0.1655-0.0906)/200
model.Cell._8.dzScale.Value = (0.0906-0.0451)/200
model.Cell._9.dzScale.Value = (0.0451-0.0175)/200
model.Cell._10.dzScale.Value = 0.0175/200

model.TopoSlopesX.Type = "PFBFile"
model.TopoSlopesX.GeomNames = "domain"
model.TopoSlopesX.FileName = "slopex_a2.pfb"

model.TopoSlopesY.Type = "PFBFile"
model.TopoSlopesY.GeomNames = "domain"
model.TopoSlopesY.FileName = "slopey_a2.pfb"

model.Geom.Perm.Names = "domain s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 g1 g2 g3 g4 g5 g6 g7 g8 g9 g10"

model.Geom.domain.Perm.Type = "Constant"
model.Geom.domain.Perm.Value = 0.02

model.Geom.s1.Perm.Type = "Constant"
model.Geom.s1.Perm.Value = 0.269022595

model.Geom.s2.Perm.Type = "Constant"
model.Geom.s2.Perm.Value = 0.043630356

model.Geom.s3.Perm.Type = "Constant"
model.Geom.s3.Perm.Value = 0.015841225

model.Geom.s4.Perm.Type = "Constant"
model.Geom.s4.Perm.Value = 0.007582087

model.Geom.s5.Perm.Type = "Constant"
model.Geom.s5.Perm.Value = 0.01818816

model.Geom.s6.Perm.Type = "Constant"
model.Geom.s6.Perm.Value = 0.005009435

model.Geom.s7.Perm.Type = "Constant"
model.Geom.s7.Perm.Value = 0.005492736

model.Geom.s8.Perm.Type = "Constant"
model.Geom.s8.Perm.Value = 0.004675077

model.Geom.s9.Perm.Type = "Constant"
model.Geom.s9.Perm.Value = 0.003386794

model.Geom.s10.Perm.Type = "Constant"
model.Geom.s10.Perm.Value = 0.004783973

model.Geom.s11.Perm.Type = "Constant"
model.Geom.s11.Perm.Value = 0.003979136

model.Geom.s12.Perm.Type = "Constant"
model.Geom.s12.Perm.Value = 0.006162952

model.Geom.s13.Perm.Type = "Constant"
model.Geom.s13.Perm.Value = 0.005009435

model.Geom.g1.Perm.Type = "Constant"
model.Geom.g1.Perm.Value = 5e-3

model.Geom.g2.Perm.Type = "Constant"
model.Geom.g2.Perm.Value = 1e-2

model.Geom.g3.Perm.Type = "Constant"
model.Geom.g3.Perm.Value = 2e-2

model.Geom.g4.Perm.Type = "Constant"
model.Geom.g4.Perm.Value = 3e-2

model.Geom.g5.Perm.Type = "Constant"
model.Geom.g5.Perm.Value = 4e-2

model.Geom.g6.Perm.Type = "Constant"
model.Geom.g6.Perm.Value = 5e-2

model.Geom.g7.Perm.Type = "Constant"
model.Geom.g7.Perm.Value = 6e-2

model.Geom.g8.Perm.Type = "Constant"
model.Geom.g8.Perm.Value = 8e-2

model.Geom.g9.Perm.Type = "Constant"
model.Geom.g9.Perm.Value = 0.1

model.Geom.g10.Perm.Type = "Constant"
model.Geom.g10.Perm.Value = 0.2

model.Perm.TensorType = "TensorByGeom"
model.Geom.Perm.TensorByGeom.Names = "domain"
model.Geom.domain.Perm.TensorValX = 1.0
model.Geom.domain.Perm.TensorValY = 1.0
model.Geom.domain.Perm.TensorValZ = 1.0

model.SpecificStorage.Type = "Constant"
model.SpecificStorage.GeomNames = "domain"
model.Geom.domain.SpecificStorage.Value = 0.0001

model.Geom.Porosity.GeomNames = "domain s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13"

model.Geom.domain.Porosity.Type = "Constant"
model.Geom.domain.Porosity.Value = 0.33

model.Geom.s1.Porosity.Type = "Constant"
model.Geom.s1.Porosity.Value = 0.375

model.Geom.s2.Porosity.Type = "Constant"
model.Geom.s2.Porosity.Value = 0.39

model.Geom.s3.Porosity.Type = "Constant"
model.Geom.s3.Porosity.Value = 0.387

model.Geom.s4.Porosity.Type = "Constant"
model.Geom.s4.Porosity.Value = 0.439

model.Geom.s5.Porosity.Type = "Constant"
model.Geom.s5.Porosity.Value = 0.489

model.Geom.s6.Porosity.Type = "Constant"
model.Geom.s6.Porosity.Value = 0.399

model.Geom.s7.Porosity.Type = "Constant"
model.Geom.s7.Porosity.Value = 0.384

model.Geom.s8.Porosity.Type = "Constant"
model.Geom.s8.Porosity.Value = 0.482

model.Geom.s9.Porosity.Type = "Constant"
model.Geom.s9.Porosity.Value = 0.442

model.Geom.s10.Porosity.Type = "Constant"
model.Geom.s10.Porosity.Value = 0.385

model.Geom.s11.Porosity.Type = "Constant"
model.Geom.s11.Porosity.Value = 0.481

model.Geom.s12.Porosity.Type = "Constant"
model.Geom.s12.Porosity.Value = 0.459

model.Geom.s13.Porosity.Type = "Constant"
model.Geom.s13.Porosity.Value = 0.399

model.Phase.RelPerm.Type =              "VanGenuchten"
model.Phase.RelPerm.GeomNames =     "domain s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13"

model.Geom.domain.RelPerm.Alpha =    1.0
model.Geom.domain.RelPerm.N =        3.0

model.Geom.s1.RelPerm.Alpha =        3.548
model.Geom.s1.RelPerm.N =            4.162

model.Geom.s2.RelPerm.Alpha =        3.467
model.Geom.s2.RelPerm.N =            2.738

model.Geom.s3.RelPerm.Alpha =        2.692
model.Geom.s3.RelPerm.N =            2.445

model.Geom.s4.RelPerm.Alpha =        0.501
model.Geom.s4.RelPerm.N =            2.659

model.Geom.s5.RelPerm.Alpha =        0.661
model.Geom.s5.RelPerm.N =            2.659

model.Geom.s6.RelPerm.Alpha =        1.122
model.Geom.s6.RelPerm.N =            2.479

model.Geom.s7.RelPerm.Alpha =        2.089
model.Geom.s7.RelPerm.N =            2.318

model.Geom.s8.RelPerm.Alpha =        0.832
model.Geom.s8.RelPerm.N =            2.514

model.Geom.s9.RelPerm.Alpha =        1.585
model.Geom.s9.RelPerm.N =            2.413

model.Geom.s10.RelPerm.Alpha =        3.311
model.Geom.s10.RelPerm.N =            2.202

model.Geom.s11.RelPerm.Alpha =        1.622
model.Geom.s11.RelPerm.N =            2.318

model.Geom.s12.RelPerm.Alpha =        1.514
model.Geom.s12.RelPerm.N =            2.259

model.Geom.s13.RelPerm.Alpha =        1.122
model.Geom.s13.RelPerm.N =            2.479

model.Phase.Saturation.Type =             "VanGenuchten"
model.Phase.Saturation.GeomNames =         "domain s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13"

model.Geom.domain.Saturation.Alpha =        1.0
model.Geom.domain.Saturation.N =            3.0
model.Geom.domain.Saturation.SRes =         0.001
model.Geom.domain.Saturation.SSat =         1.0

model.Geom.s1.Saturation.Alpha =        3.548
model.Geom.s1.Saturation.N =            4.162
model.Geom.s1.Saturation.SRes =         0.0001
model.Geom.s1.Saturation.SSat =         1.0

model.Geom.s2.Saturation.Alpha =        3.467
model.Geom.s2.Saturation.N =            2.738
model.Geom.s2.Saturation.SRes =         0.0001
model.Geom.s2.Saturation.SSat =         1.0

model.Geom.s3.Saturation.Alpha =        2.692
model.Geom.s3.Saturation.N =            2.445
model.Geom.s3.Saturation.SRes =         0.0001
model.Geom.s3.Saturation.SSat =         1.0

model.Geom.s4.Saturation.Alpha =        0.501
model.Geom.s4.Saturation.N =            2.659
model.Geom.s4.Saturation.SRes =         0.1
model.Geom.s4.Saturation.SSat =         1.0

model.Geom.s5.Saturation.Alpha =        0.661
model.Geom.s5.Saturation.N =            2.659
model.Geom.s5.Saturation.SRes =         0.0001
model.Geom.s5.Saturation.SSat =         1.0

model.Geom.s6.Saturation.Alpha =        1.122
model.Geom.s6.Saturation.N =            2.479
model.Geom.s6.Saturation.SRes =         0.0001
model.Geom.s6.Saturation.SSat =         1.0

model.Geom.s7.Saturation.Alpha =        2.089
model.Geom.s7.Saturation.N =            2.318
model.Geom.s7.Saturation.SRes =         0.0001
model.Geom.s7.Saturation.SSat =         1.0

model.Geom.s8.Saturation.Alpha =        0.832
model.Geom.s8.Saturation.N =            2.514
model.Geom.s8.Saturation.SRes =         0.0001
model.Geom.s8.Saturation.SSat =         1.0

model.Geom.s9.Saturation.Alpha =        1.585
model.Geom.s9.Saturation.N =            2.413
model.Geom.s9.Saturation.SRes =         0.0001
model.Geom.s9.Saturation.SSat =         1.0

model.Geom.s10.Saturation.Alpha =        3.311
model.Geom.s10.Saturation.N =            2.202
model.Geom.s10.Saturation.SRes =         0.0001
model.Geom.s10.Saturation.SSat =         1.0

model.Geom.s11.Saturation.Alpha =        1.622
model.Geom.s11.Saturation.N =            2.318
model.Geom.s11.Saturation.SRes =         0.0001
model.Geom.s11.Saturation.SSat =         1.0

model.Geom.s12.Saturation.Alpha =        1.514
model.Geom.s12.Saturation.N =            2.259
model.Geom.s12.Saturation.SRes =         0.0001
model.Geom.s12.Saturation.SSat =         1.0

model.Geom.s13.Saturation.Alpha =        1.122
model.Geom.s13.Saturation.N =            2.479
model.Geom.s13.Saturation.SRes =         0.0001
model.Geom.s13.Saturation.SSat =         1.0

model.Mannings.Type = "PFBFile"
model.Mannings.GeomNames = "domain"
model.Mannings.FileName = "mannings_a2.pfb"

# Phases
model.Phase.Names = "water"
model.Phase.water.Density.Type = "Constant"
model.Phase.water.Density.Value = 1.0
model.Phase.water.Viscosity.Type = "Constant"
model.Phase.water.Viscosity.Value = 1.0
model.Phase.water.Mobility.Type = "Constant"
model.Phase.water.Mobility.Value = 1.0

# Contaminants
model.Contaminants.Names = ""

# Gravity
model.Gravity = 1.0

#Wells
model.Wells.Names = ""

# Phase Sources
model.PhaseSources.water.Type = "Constant"
model.PhaseSources.water.GeomNames = "domain"
model.PhaseSources.water.Geom.domain.Value = 0.0

model.TimingInfo.BaseUnit = 1.0
model.TimingInfo.StartCount = 0 # restart
model.TimingInfo.StartTime = 0.0 # restart
model.TimingInfo.StopTime = 8760.0 #restart
model.TimingInfo.DumpInterval = 1.0
model.TimeStep.Type = "Constant"
model.TimeStep.Value = 1.0

#Time cycles
model.Cycle.Names ="constant"
model.Cycle.constant.Names = "alltime"
model.Cycle.constant.alltime.Length = 1
model.Cycle.constant.Repeat = -1

# An alternate approach defining rainfall and recession time periods are defined here
# rain for 1 hour, recession for 2 hours
# model.Cycle.Names ="constant rainrec"
# model.Cycle.rainrec.Names = "rain rec"
# model.Cycle.rainrec.rain.Length = 1
# model.Cycle.rainrec.rec.Length = 5000000
# model.Cycle.rainrec.Repeat = -1

model.BCPressure.PatchNames = "left right front back bottom top"

model.Patch.left.BCPressure.Type = "FluxConst"
model.Patch.left.BCPressure.Cycle = "constant"
model.Patch.left.BCPressure.alltime.Value = 0.0

model.Patch.right.BCPressure.Type = "FluxConst"
model.Patch.right.BCPressure.Cycle = "constant"
model.Patch.right.BCPressure.alltime.Value = 0.0

model.Patch.front.BCPressure.Type = "FluxConst"
model.Patch.front.BCPressure.Cycle = "constant"
model.Patch.front.BCPressure.alltime.Value = 0.0

model.Patch.back.BCPressure.Type = "FluxConst"
model.Patch.back.BCPressure.Cycle = "constant"
model.Patch.back.BCPressure.alltime.Value = 0.0

model.Patch.bottom.BCPressure.Type = "FluxConst"
model.Patch.bottom.BCPressure.Cycle = "constant"
model.Patch.bottom.BCPressure.alltime.Value = 0.0

model.Patch.top.BCPressure.Type = "OverlandKinematic"
model.Patch.top.BCPressure.Cycle = "constant"
model.Patch.top.BCPressure.alltime.Value = 0.0

model.ICPressure.Type = "PFBFile"
model.ICPressure.GeomNames = "domain"
model.Geom.domain.ICPressure.RefPatch = "top"
model.Geom.domain.ICPressure.FileName = "press_init_a2.pfb" # restart

model.Solver.LSM = "CLM"

# outputs
model.Solver.CLM.CLMFileDir = "clm_output/"
model.Solver.CLM.Print1dOut = False
model.Solver.BinaryOutDir = False #Solver: Field BinaryOutDir is not part of the expected schema <class 'parflow.tools.database.generated.Solver'>
model.Solver.CLM.DailyRST = True
# model.Solver.CLM.WriteLastRST = True
model.Solver.CLM.CLMDumpInterval = 1

# forcing files
model.Solver.CLM.MetFileName = "E5L" 
model.Solver.CLM.MetFilePath = "/home/sunaoqi/E5L"
model.Solver.CLM.MetForcing = "3D"
model.Solver.CLM.MetFileNT = 24
model.Solver.CLM.IstepStart = 1 # restart: 转储序列+1

# physical properties
model.Solver.CLM.EvapBeta = "Linear"
model.Solver.CLM.VegWaterStress = "Saturation"
model.Solver.CLM.ResSat = 0.1
model.Solver.CLM.WiltingPoint = 0.12
model.Solver.CLM.FieldCapacity = 0.98
model.Solver.CLM.IrrigationType = "none"

model.Solver.CLM.RootZoneNZ = 10
model.Solver.CLM.SoiLayer = 10

model.Solver.PrintSubsurfData = True
model.Solver.PrintPressure = True
model.Solver.PrintSaturation = True
model.Solver.PrintMask = True
model.Solver.PrintVelocities = False
model.Solver.PrintEvapTrans = True
model.Solver.CLM.SingleFile = True
model.Solver.PrintSlopes = True
model.Solver.PrintMannings = True

model.Solver.WriteCLMBinary = False
model.Solver.PrintCLM = True

# Solver types
model.Solver = "Richards"
model.Solver.TerrainFollowingGrid = True
model.Solver.TerrainFollowingGrid.SlopeUpwindFormulation = "Upwind" 
model.Solver.Linear.Preconditioner = "PFMG"
#model.Solver.Linear.Preconditioner.PCMatrixType = "FullJacobian"
model.Solver.Linear.Preconditioner.PCMatrixType = "PFSymmetric"

# Exact solution
model.KnownSolution = "NoKnownSolution"

# Solver settings
model.Solver.MaxIter = 250000
# model.Solver.Drop = 1e-20
model.Solver.AbsTol = 1e-10
model.Solver.MaxConvergenceFailures = 50
model.Solver.Nonlinear.MaxIter = 250
model.Solver.Nonlinear.ResidualTol = 1e-5
model.Solver.Nonlinear.EtaChoice =  "EtaConstant"
model.Solver.Nonlinear.EtaValue = 0.01
model.Solver.Nonlinear.UseJacobian = True
# model.Solver.Nonlinear.DerivativeEpsilon = 1e-16
model.Solver.Nonlinear.StepTol = 1e-15
model.Solver.Nonlinear.Globalization = "LineSearch"
model.Solver.Linear.KrylovDimension = 500
model.Solver.Linear.MaxRestarts = 8

# Distribute input files
# slope files are 2D (i.e. they only have one layer) so you need to set NZ to 1 before you distribute them
# Make sure to set it back to your actual NZ before distributing 3D files or running your model
model.ComputationalGrid.NZ = 1
model.dist("slopex_a2.pfb")
model.dist("slopey_a2.pfb")
model.dist("mannings_a2.pfb")

model.ComputationalGrid.NZ = 11 #the rest of the inputs shoul dbe distributed over 3D space
model.dist("indicator_a2.pfb")
model.dist("press_init_a2.pfb") # restart

# write
model.write()
model.write(file_format='yaml')
model.write(file_format='json')

#run
model.run()