/*
 * pimegaDetector.h
 *
 *  Created on: 11 Dec 2018
 *      Author: Douglas Araujo
 */

// Standard includes
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <stdint.h>
#include <map>

// EPICS includes
#include <epicsThread.h>
#include <epicsEvent.h>
#include <epicsString.h>
#include <iocsh.h>
#include <epicsExport.h>

#include <epicsStdio.h>
#include <epicsMutex.h>
#include <cantProceed.h>
#include <epicsExit.h>

// Asyn driver includes
#include <asynOctetSyncIO.h>

// areaDetector includes
#include "ADDriver.h"

// pimega lib includes
#include <pimega.h>

#define MAX_FILENAME_LEN 300
#define MAX_BAD_PIXELS 100
/** Time to poll when reading from Labview */
#define ASYN_POLL_TIME .01

/** Time between checking to see if image file is complete */
#define FILE_READ_DELAY .01

#define DIMS 2
#define DEFAULT_POLL_TIME 2

#define N_DACS_OUTS 31

static const char *driverName = "pimegaDetector";

#define error(fmt, ...) asynPrint(pasynUserSelf, ASYN_TRACE_ERROR, \
        "%s:%d " fmt, __FILE__, __LINE__, __VA_ARGS__)
                                  
#define pimegaMedipixModeString         "MEDIPIX_MODE"
#define pimegaefuseIDString             "EFUSE_ID"
#define pimegaOmrOPModeString           "OMR_OP_MODE"
#define pimegaMedipixBoardString        "MEDIPIX_BOARD"
#define pimegaMedipixChipString         "MEDIPIX_CHIP"
#define pimegaPixeModeString            "PIXEL_MODE"
#define pimegaContinuosRWString         "CONTINUOUSRW"
#define pimegaPolarityString            "POLARITY"
#define pimegaDiscriminatorString       "DISCRIMINATOR"
#define pimegaTestPulseString           "TEST_PULSE"
#define pimegaCounterDepthString        "COUNTER_DEPTH"
#define pimegaEqualizationString        "EQUALIZATION"
#define pimegaGainString                "GAIN_MODE"
#define pimegaDacBiasString             "DAC_BIAS"
#define pimegaDacCasString              "CAS"
#define pimegaDacDelayString            "DELAY"
#define pimegaDacDiscString             "DISC"
#define pimegaDacDiscHString            "DISC_H"
#define pimegaDacDiscLString            "DISC_L"
#define pimegaDacDiscLSString           "DISC_LS"
#define pimegaDacFbkString              "FBK"
#define pimegaDacGndString              "GND"
#define pimegaDacIKrumString            "IKRUM"
#define pimegaDacPreampString           "PREAMP"
#define pimegaDacRpzString              "RPZ"
#define pimegaDacShaperString           "SHAPER"
#define pimegaThreshold0String          "THRESHOLD0"
#define pimegaThreshold1String          "THRESHOLD1"
#define pimegaDacTPBufferInString       "TP_BUFFER_IN"
#define pimegaDacTPBufferOutString      "TP_BUFFER_OUT"
#define pimegaDacTPRefString            "TP_REF"
#define pimegaDacTPRefAString           "TP_REF_A"
#define pimegaDacTPRefBString           "TP_REF_B"
#define pimegaResetString               "RESET"
#define pimegaReadCounterString         "READ_COUNTER"
#define pimegaSenseDacSelString         "SENSE_DAC_SEL"
#define pimegaDacOutSenseString         "DAC_OUT_SENSE"
#define pimegaDacsOutSenseString        "DACS_OUT_SENSE"
#define pimegaBackendBufferString       "BACK_BUFFER"
#define pimegaResetRDMABufferString     "RESET_RDMA_BUFFER"
#define pimegaSensorBiasString          "SENSOR_BIAS"
#define pimegaModuleString              "PIMEGA_MODULE"
#define pimegaAllModulesString          "ALL_MODULES"
#define pimegaBackendLSFRString         "BACK_LSFR"
#define pimegaSendImageString           "SEND_IMAGE"
#define pimegaSelSendImageString        "SEL_SEND_IMAGE"
#define pimegaSendDacDoneString         "SEND_DAC_DONE"
#define pimegaConfigDiscLString         "CONFIG_DISCL"

class pimegaDetector: public ADDriver
{
public:
    pimegaDetector(const char *portName, const char *address_module01, const char *address_module02,
                   const char *address_module03, const char *address_module04,
                   int port, int maxSizeX, int maxSizeY,
                   int detectorModel, int maxBuffers, size_t maxMemory, int priority, int stackSize);

    virtual asynStatus writeFloat64(asynUser *pasynUser, epicsFloat64 value);
    virtual asynStatus writeInt32(asynUser *pasynUser, epicsInt32 value);
    virtual asynStatus readInt32(asynUser *pasynUser, epicsInt32 *value);
    virtual asynStatus readFloat64(asynUser *pasynUser, epicsFloat64 *value);
    virtual asynStatus readFloat32Array(asynUser *pasynUser, epicsFloat32 *value, size_t nElements, size_t *nIn);

    virtual void report(FILE *fp, int details);
    virtual void acqTask(void);
    virtual void generateImage(void);

    // Debugging routines
    asynStatus initDebugger(int initDebug);
    asynStatus debugLevel(const std::string& method, int onOff);
    asynStatus debug(const std::string& method, const std::string& msg);
    asynStatus debug(const std::string& method, const std::string& msg, int value);
    asynStatus debug(const std::string& method, const std::string& msg, double value);
    asynStatus debug(const std::string& method, const std::string& msg, const std::string& value);

protected:
    int PimegaReset;
    #define FIRST_PIMEGA_PARAM PimegaReset
    int PimegaMedipixMode;
    int PimegaefuseID;
    int PimegaOmrOPMode;
    int PimegaMedipixBoard;
    int PimegaMedipixChip;
    int PimegaContinuosRW;
    int PimegaPolarity;
    int PimegaDiscriminator;
    int PimegaPixelMode;
    int PimegaTestPulse;
    int PimegaCounterDepth;
    int PimegaEqualization;
    int PimegaGain;
    int PimegaDacBias;
    int PimegaCas;
    int PimegaDelay;
    int PimegaDisc;
    int PimegaDiscH;
    int PimegaDiscL;
    int PimegaDiscLS;
    int PimegaFbk;
    int PimegaGnd;
    int PimegaIkrum;
    int PimegaPreamp;
    int PimegaRpz;
    int PimegaShaper;
    int PimegaThreshold0;
    int PimegaThreshold1;
    int PimegaTpBufferIn;
    int PimegaTpBufferOut;
    int PimegaTpRef;
    int PimegaTpRefA;
    int PimegaTpRefB;
    int PimegaReadCounter;
    int PimegaSenseDacSel;
    int PimegaDacOutSense;
    int PimegaDacsOutSense;
    int PimegaBackBuffer;
    int PimegaResetRDMABuffer;
    int PimegaBackLSFR;
    int PimegaModule;
    int PimegaAllModules;
    int PimegaSendImage;
    int PimegaSelSendImage;
    int PimegaSendDacDone;
    int PimegaConfigDiscL;
    int PimegaSensorBias;
    #define LAST_PIMEGA_PARAM PimegaSensorBias

private:

    // debug map
    std::map<std::string, int>         debugMap_;

    // ***** poller control variables ****
    double pollTime_;
    int forceCallback_;
    // ***********************************

    epicsEventId startEventId_;
    epicsEventId stopEventId_;

    pimega_t *pimega;
    pimega_detector_model_t detModel;

    int p_imageSize = 256;
    uint32_t *pimega_image; 
    int arrayCallbacks;
    size_t dims[2];
    int itemp;

    epicsFloat32 *PimegaDacsOutSense_;

    void panic(const char *msg);
    void connect(const char *address[4], unsigned short port);
    void createParameters(void);
    void setParameter(int index, const char *value);
    void setParameter(int index, int value);
    void setParameter(int index, double value);
    void getParameter(int index, int maxChars, char *value);
    void getParameter(int index, int *value);
    void getParameter(int index, double *value);

    void getDacsValues(void);
    
    void setDefaults(void);
    asynStatus getDacsOutSense(void);
    asynStatus startAcquire();

    asynStatus selectModule(uint8_t module);
    asynStatus medipixMode(uint8_t mode);
    asynStatus configDiscL(int value);
    asynStatus triggerMode(int trigger);
    asynStatus reset(short action);
    asynStatus setDACValue(pimega_dac_t dac, int value, int parameter);
    asynStatus setOMRValue(pimega_omr_t dac, int value, int parameter);
    asynStatus imgChipID(uint8_t chip_id);
    asynStatus medipixBoard(uint8_t board_id);
    asynStatus numExposures(unsigned number);
    asynStatus pixelMode(int mode);
    asynStatus continuosRW(int mode);
    asynStatus polarity(int mode);
    asynStatus discriminator(int mode);
    asynStatus enableTP(int mode);
    asynStatus counterDepth(int mode);
    asynStatus equalization(int mode);
    asynStatus gainMode(int mode);
    asynStatus acqTime(float acquire_time_s);
    asynStatus omrOpMode(int mode);
    asynStatus sensorBias(float voltage);
    asynStatus readCounter(int counter);
    asynStatus senseDacSel(u_int8_t dac);
    asynStatus imageMode(u_int8_t mode);
    asynStatus sendImage(void);

};

#define NUM_pimega_PARAMS (&LAST_pimega_PARAM - &FIRST_pimega_PARAM + 1)



