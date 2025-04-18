#!../../bin/linux-x86_64/pimegaApp
< envPaths

errlogInit(20000)

dbLoadDatabase("$(TOP)/dbd/pimegaApp.dbd")
pimegaApp_registerRecordDeviceDriver(pdbbase)

# Prefix for all records
epicsEnvSet("PREFIX", "PITEC:D:RAD800k:")
# The port name for the detector
epicsEnvSet("PORT",   "PIMEGA")
# The detector model (0:mobipix; 1:pimega45D; 2:pimega135DL; 3:pimega135D; 4:pimega540D; 5:pimega450D; 6:pimega450DS, 7:RAD400k, 8:RAD800k)
epicsEnvSet("DMODEL", "8");
# The queue size for all plugins
epicsEnvSet("QSIZE",  "20")
# The maximim image width; used for row profiles in the NDPluginStats plugin
epicsEnvSet("XSIZE",  "1536")
# The maximim image height; used for column profiles in the NDPluginStats plugin
epicsEnvSet("YSIZE",  "512")
# Number of Elements
epicsEnvSet("NELEMENTS", "786432")
# The maximum number of time seried points in the NDPluginStats plugin
epicsEnvSet("NCHANS", "2048")
# The maximum number of frames buffered in the NDPluginCircularBuff plugin
epicsEnvSet("CBUFFS", "10000")
# The IP address of the Pimega system
epicsEnvSet("PIMEGA_MODULE01_IP", "10.255.255.2")
epicsEnvSet("PIMEGA_MODULE02_IP", "10.255.255.6")
epicsEnvSet("PIMEGA_MODULE03_IP", "127.0.0.1")
epicsEnvSet("PIMEGA_MODULE04_IP", "127.0.0.1")
epicsEnvSet("PIMEGA_MODULE05_IP", "127.0.0.1")
epicsEnvSet("PIMEGA_MODULE06_IP", "127.0.0.1")
epicsEnvSet("PIMEGA_MODULE07_IP", "127.0.0.1")
epicsEnvSet("PIMEGA_MODULE08_IP", "127.0.0.1")
epicsEnvSet("PIMEGA_MODULE09_IP", "127.0.0.1")
epicsEnvSet("PIMEGA_MODULE10_IP", "127.0.0.1")

# The IP port for the command socket
epicsEnvSet("PIMEGA_PORT", "60000")
# The search path for database files
epicsEnvSet("EPICS_DB_INCLUDE_PATH", "$(ADCORE)/db")

# This need to be set also on the terminal used for monitoring the IOC
# Calculated as 1536*512*4*100 = 314572800
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "314572800")

epicsEnvSet("PIMEGA_NUM_MODULES_X", "1")
epicsEnvSet("PIMEGA_NUM_MODULES_Y", "2")

# pimegaDetectorConfig(
#              portName,           # The name of the asyn port to be created
#              address, 	       # The ip address of the pimega detector
#              port,               # the number port of pimega detector
#              maxSizeX,           # The size of the pimega detector in the X direction.
#              maxSizeY,           # The size of the pimega detector in the Y direction.
#			   detectorModel,      # Detector model, 0:mobipix; 1:pimega540D.
#              maxBuffers,         # The maximum number of NDArray buffers that the NDArrayPool for this driver is
#                                    allowed to allocate. Set this to 0 to allow an unlimited number of buffers.
#              maxMemory,          # The maximum amount of memory that the NDArrayPool for this driver is
#                                    allowed to allocate. Set this to 0 to allow an unlimited amount of memory.
#              priority,           # The thread priority for the asyn port driver thread if ASYN_CANBLOCK is set in asynFlags.
#              stackSize,          # The stack size for the asyn port driver thread if ASYN_CANBLOCK is set in asynFlags.
#              simulate            # If set to 1, simulation mode is activated
#              backendOn           # Run the IOC without connecting to the backend. Obviously, there will be no images received.
#              logFileEnable       # enable disable logging
#              BackendPort         # select the backend port for commands and status
#              BackendPortFrame    # select the backend port for frame receiving
#              IntAcqResetRDMA     # Reset the RDMA buffer before the acquisition (true -> 1 or false - > 0)

pimegaDetectorConfig("$(PORT)",$(PIMEGA_MODULE01_IP),$(PIMEGA_MODULE02_IP),$(PIMEGA_MODULE03_IP),$(PIMEGA_MODULE04_IP),$(PIMEGA_MODULE05_IP),$(PIMEGA_MODULE06_IP),$(PIMEGA_MODULE07_IP),$(PIMEGA_MODULE08_IP),$(PIMEGA_MODULE09_IP),$(PIMEGA_MODULE10_IP),$(PIMEGA_PORT), $(XSIZE), $(YSIZE), $(DMODEL), 0, 0, 0, 0, 0, 1, 1, 5418, 6467, 1, $(PIMEGA_NUM_MODULES_X), $(PIMEGA_NUM_MODULES_Y))

dbLoadRecords("$(ADPIMEGA)/db/pimega.template","P=$(PREFIX),R=cam1:,PORT=$(PORT),ADDR=0,TIMEOUT=1")
dbLoadRecords("$(ADPIMEGA)/db/NDFile.template","P=$(PREFIX),R=cam1:,PORT=$(PORT),ADDR=0,TIMEOUT=1")

# Load asynRecord record
dbLoadRecords("$(ASYN)/db/asynRecord.db", "P=${PREFIX}, R=asyn1,PORT=$(PORT),ADDR=0,OMAX=256,IMAX=256")
asynSetTraceMask($(PORT), 0, 0x00)

# Create a standard arrays plugin, set it to get data from pimega driver.
NDStdArraysConfigure("Image1", "$(QSIZE)", 0, "$(PORT)", 0, 0)

dbLoadRecords("$(ADCORE)/db/NDStdArrays.template", "P=$(PREFIX),R=image1:,PORT=Image1,ADDR=0,TIMEOUT=1,NDARRAY_PORT=$(PORT),TYPE=Int32,FTVL=LONG,NELEMENTS=$(NELEMENTS)")

# Load all other plugins using commonPlugins.cmd
< commonPlugins.cmd
set_requestfile_path("$(ADPIMEGA)/pimegaApp/Db")


iocInit()

dbpf(${PREFIX}cam1:FilePath,"${PIMEGA_PSS}/database/acquisitions")
dbpf(${PREFIX}cam1:FileName,"test")
dbpf(${PREFIX}cam1:FileTemplate,"%s%s_%3.3d.hdf5")
# dbpf(${PREFIX}cam1:dac_defaults_files,"${PIMEGA_PSS}/ioc/epics/iocs/pimegaIOC/iocBoot/iocPimega/config/RAD800k.ini")
dbpf(${PREFIX}cam1:ImgChipNumberID, 1)
dbpf(${PREFIX}image1:EnableCallbacks, 1)
dbpf(${PREFIX}Stats2:EnableCallbacks, 1)

# save things every thirty seconds
#create_monitor_set("auto_settings.req", 30,"P=$(PREFIX)")
