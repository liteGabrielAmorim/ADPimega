TOP=../..

include $(TOP)/configure/CONFIG

# -------------------------------
# Build an Support Module
# -------------------------------

USR_INCLUDES +=-I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include
USR_INCLUDES +=-I/usr/local/epics/synApps/support/areaDetector-R3-7/ADPimega/pimegaSupport

#INC += pimegaDetector.h

LIBRARY_IOC_Linux += pimegaDetector

LIB_SRCS += pimegaDetector.cpp

LIB_SYS_LIBS_Linux += pimega
# ------------------------
# Build the Area Detector Derived Library
# ------------------------
DBD += pimega.dbd

USR_CXXFLAGS += -O0 -g
USR_CFLAGS += -O0 -g

include $(ADCORE)/ADApp/commonLibraryMakefile

include $(TOP)/configure/RULES
