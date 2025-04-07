# ParFlow-CoLM
**Twenty Years Later, All is Well: Coupling ParFlow with the Latest Common Land Model**  
**二十年别来无恙：耦合ParFlow与最新通用陆面模式CoLM**

## Quick Start on Unix/Linux

### Step 1: Setup

Decide where to install ParFlow and associated libraries.

Set the environment variable `PARFLOW_DIR` to the chosen location:

**For bash (an example on Princeton Della cluster):**

```shell
   export PARFLOW_VERSION=3.10
   export PARFLOW_INS=/home/cy15/pf-colm
   export PF_SRC=/home/cy15/pf-colm/parflow/

   module load cmake/3.18.2
   module load openmpi/gcc/4.1.6

   #export SILO_DIR=$PARFLOW_INS/silo-4.10.2
   export HYPRE_DIR=$PARFLOW_INS/hypre-2.18.2
   export PARFLOW_DIR=$PARFLOW_INS/parflow

   #export LD_LIBRARY_PATH=$SILO_DIR/lib:$LD_LIBRARY_PATH
   export LD_LIBRARY_PATH=$HYPRE_DIR/lib:$LD_LIBRARY_PATH
   export LD_LIBRARY_PATH=$PARFLOW_DIR/lib:$LD_LIBRARY_PATH

   #export PATH=$SILO_DIR/bin:$PATH
   export PATH=$PARFLOW_DIR/bin:$PATH

   export F90=mpif90
   export F77=mpif77
   export FC=mpif90
   export CC=mpicc
   export CXX=mpicxx
```   

### Step 2: Extract the Source

Extract the source files from the compressed tar file.

### Step 3: Running CMake to configure ParFlow

CMake is a utility that sets up makefiles for building ParFlow.  CMake
allows setting of compiler to use and other options.  First create a
directory for the build.  It is generally recommend to build outside
of the source directory to make it keep things clean.  For example,
restarting a failed build with a separate build directory simply
involves removing the build directory.

#### Building with the cmake command line

Building a parallel version of ParFlow requires the communications
layer to use must be set.  The most common option will be MPI.  Here
is a minimal example of an MPI build with CLM:

```shell
   cd parflow
   mkdir build
   cd build
   cmake  .. \
          -DPARFLOW_AMPS_LAYER=mpi1 \
	  -DPARFLOW_ENABLE_PYTHON=TRUE \
	  -DPARFLOW_AMPS_SEQUENTIAL_IO=TRUE \
	  -DHYPRE_ROOT=$HYPRE_DIR \
	  -DPARFLOW_ENABLE_TIMING=TRUE \
	  -DPARFLOW_HAVE_CLM=TRUE \
	  -DCMAKE_INSTALL_PREFIX=$PARFLOW_DIR \
	  -DPARFLOW_PYTHON_VIRTUAL_ENV=ON
```

### Step 4: Building and installing

Once CMake has configured and created a set of Makefiles; building is
easy:

```shell
   make 
   make install
```

### Step 5: Run 
An example in  
```shell
   parflow/pfsimulator/clm/example/
```
