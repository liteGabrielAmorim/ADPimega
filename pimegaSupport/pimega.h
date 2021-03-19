

#ifndef _PIMEGA_H_INCLUDED_
#define _PIMEGA_H_INCLUDED_

#include <inttypes.h>
#include <pthread.h>
#include <stdio.h>
#include <sys/time.h>

#if __GNUC__ >= 4
#pragma GCC visibility push(default)
#endif

#ifdef __cplusplus
extern "C" {
#endif

#define PIMEGA_SUCCESS 0
#define PIMEGA_NAME_ERROR -1
#define PIMEGA_READ_MSG_ERROR -2
#define PIMEGA_COMMAND_FAILED -3
#define PIMEGA_DAC_FAILED -4
#define PIMEGA_DAC_VALUE_FAILED -5
#define PIMEGA_DATA_SERVER_DISCONNECTED -6
#define PIMEGA_INVALID_MODULE -7
#define PIMEGA_DATA_SERVER_PARSE_ERROR -8
#define PIMEGA_INVALID_BIT_RATE -9
#define PIMEGA_INVALID_IMAGE_COUNT -10
#define	PIMEGA_OMR_FAILED -11
#define	PIMEGA_OMR_VALUE_FAILED -12
#define PIMEGA_INVALID_ERROR_ID -13

#define PIMEGA_SIZE_SEND_MSG 512
#define PIMEGA_SIZE_READ_MSG 512
#define PIMEGA_SIZE_RESULT 1024

#define PIMEGA_TIMEOUT 600000000UL
#define DATA_SERVER_TIMEOUT 300000000UL
#define PIMEGA_MAX_FILE_NAME 300

#define PIMEGA_MIN_GAP 2e-5f

#define PIMEGA_MAX_TEMPERATURE 120
#define PIMEGA_MIN_TEMPERATURE 20

#define PIMEGA_BIASVOLTAGE 60.0
#define PIMEGA_BIAS_STEP 1.0
#define PIMEGA_BIAS_DELAY 0.1
#define PIMEGA_MIN_BIASVOLTAGE 0
#define PIMEGA_MB_SENSOR_TEMPERATURE 16

#define SERIAL 0
#define ETHERNET 1
#define COMMUNICATION ETHERNET

//TODO: Put this struct in another file 
/* Backend Structs*/

#define STRUCT_SIZE 400
#define MODULE1 0
#define MODULE2 1
#define MODULE3 2
#define MODULE4 3

#define SEL_IMMD_DATA 1
#define RDMA_CADENCE 1
#define FRAME_SIZE_540D 3072UL * 3072UL

#define RETURN_RC_ON_ERROR(x, y) x; if (rc != 0) { fprintf(stderr, "%s\n", y); return rc; };
#define RETURN_ON_ERROR(x, ...) if (x != 0) { fprintf(stderr, ##__VA_ARGS__); return -1; };



#define RESET   "\033[0m"
#define BLACK   "\033[30m"      /* Black */
#define RED     "\033[31m"      /* Red */
#define GREEN   "\033[32m"      /* Green */
#define YELLOW  "\033[33m"      /* Yellow */
#define BLUE    "\033[34m"      /* Blue */
#define MAGENTA "\033[35m"      /* Magenta */
#define CYAN    "\033[36m"      /* Cyan */
#define WHITE   "\033[37m"      /* White */
#define BOLDBLACK   "\033[1m\033[30m"      /* Bold Black */
#define BOLDRED     "\033[1m\033[31m"      /* Bold Red */
#define BOLDGREEN   "\033[1m\033[32m"      /* Bold Green */
#define BOLDYELLOW  "\033[1m\033[33m"      /* Bold Yellow */
#define BOLDBLUE    "\033[1m\033[34m"      /* Bold Blue */
#define BOLDMAGENTA "\033[1m\033[35m"      /* Bold Magenta */
#define BOLDCYAN    "\033[1m\033[36m"      /* Bold Cyan */
#define BOLDWHITE   "\033[1m\033[37m"      /* Bold White */



#define VVV   0
#define VV    1
#define V     1





#define warn_print(fmt, ...) \
            do {		struct timeval curTime; \
						gettimeofday(&curTime, NULL); \
						char text[2000] = BOLDMAGENTA "[%02d:%02d:%02d.%06d] " RESET; \
						struct tm *readable = localtime(&curTime.tv_sec); \
						strcat(text, fmt); \
                        fprintf(stdout, text, readable->tm_hour, readable->tm_min, readable->tm_sec, curTime.tv_usec,##__VA_ARGS__); \
            } while (0)

#define vvv_print(fmt, ...) \
            do {    if (VVV) { \
						struct timeval curTime; \
						gettimeofday(&curTime, NULL); \
						char text[2000] = GREEN "[%02d:%02d:%02d.%06d] " RESET; \
						struct tm *readable = localtime(&curTime.tv_sec); \
						strcat(text, fmt); \
						fprintf(stdout, text, readable->tm_hour, readable->tm_min, readable->tm_sec, curTime.tv_usec,##__VA_ARGS__); \
                    } \
            } while (0)

#define err_print(fmt, ...) \
            do {    struct timeval curTime; \
					gettimeofday(&curTime, NULL); \
					char text[2000] = RED "[%02d:%02d:%02d.%06d] " RESET; \
					struct tm *readable = localtime(&curTime.tv_sec); \
					strcat(text, fmt); \
					fprintf(stdout, text, readable->tm_hour, readable->tm_min, readable->tm_sec, curTime.tv_usec,##__VA_ARGS__); \
            } while (0)

#define vv_print(fmt, ...) \
            do {    if (VV) { \
						struct timeval curTime; \
						gettimeofday(&curTime, NULL); \
						char text[2000] = GREEN "[%02d:%02d:%02d.%06d] " RESET; \
						struct tm *readable = localtime(&curTime.tv_sec); \
						strcat(text, fmt); \
						fprintf(stdout, text, readable->tm_hour, readable->tm_min, readable->tm_sec, curTime.tv_usec,##__VA_ARGS__); \
                    } \
            } while (0)

#define v_print(fmt, ...) \
            do {    if (V) { \
						struct timeval curTime; \
						gettimeofday(&curTime, NULL); \
						char text[2000] = GREEN "[%02d:%02d:%02d.%06d] " RESET; \
						struct tm *readable = localtime(&curTime.tv_sec); \
						strcat(text, fmt); \
						fprintf(stdout, text, readable->tm_hour, readable->tm_min, readable->tm_sec, curTime.tv_usec,##__VA_ARGS__); \
                    } \
            } while (0)			


/* Backend structures */
enum requestTypesEnum {
    INIT_ARGS = 0,
    ACQUIRE_ARGS = 1,
    ACQUIRE_STATUS = 2,
    SAVE_STATUS = 3,
    ABORT_SAVE = 4,
    STOP_ACQUIRE = 5,
    ARRAY_DATA = 6,
    GEOMETRY = 7
};

enum bulkProcessingEnum {
    BULKPROCESSING_AUTO = 0,
    BULKPROCESSING_ON = 1,
    BULKPROCESSING_OFF = 2
};

enum OperationTypesEnum {
    ACK = 0,
    NAK,
    DONE,
    NOT_DONE,
    ERROR
};

enum returnTypesEnum {
    INVALID_SAVE_PATH,
    INVALID_AQUISITION_MODE,
    INVALID_NUM_OF_ACQUISITIONS,
    INVALID_GEOMETRY,
    INVALID_INDEX_ID,
    STILL_SAVING
};

enum saveModeEnum {
    SAVE_AFTER = 2,
    SAVE_DURING = 1,
    NO_SAVE = 0
};


enum aquisitionModeEnum {
    B12 = 0,
    B24 = 1,
    DUALENERGY = 2
};

enum IndexSendMode {
    SEND_FRAME = 0,
    SEND_VOLUME = 1
};

#define STRUCT_SIZE 400

//Size 2
typedef struct __attribute__((__packed__)){
    uint8_t  type;
    uint8_t  error;
    uint8_t reserved[STRUCT_SIZE-2];
} simpleArgs;

typedef struct __attribute__((__packed__)){
    uint8_t  type;
    char     jsonfile[300];
    uint8_t reserved[STRUCT_SIZE-301];
} geometryArgs;

//Size 353
typedef struct __attribute__((__packed__)){
    uint8_t                type;
    uint64_t               noOfAquisitions;
    char                   savefile[300];
    bool                   useLFSR;
    uint8_t                saveMode;
    uint8_t                aquisitionMode;
    bool                   resetRDMABuffer;
    double                 detectorDistance;
    bool                   bulkProcessing;
    uint8_t                indexSendMode;
    char                   indexDestinationID[30];
    bool                   indexEnable;
    uint8_t                reserved[STRUCT_SIZE-354];
} acqArgs;


//Size 143
typedef struct __attribute__((__packed__)){
    uint8_t                type;
    uint64_t               noOfFrames[4]; /* This contains the number of frames acquired */
    uint64_t               noOfAquisitions[4]; /* This contains the number of aquisitions */
    float                  bufferUsed[4]; /* This contains a percentage of the buffer usage */
    bool                   moduleError[4]; /* Reception errors are indicated here */
    bool                   indexError;
    uint64_t               lostFrameCnt[4];
    uint8_t                done;
    uint64_t               savedFrameNum;
    uint64_t               savedAquisitionNum;
    uint64_t               indexSentAquisitionNum;
    uint8_t                reserved[STRUCT_SIZE-143];
} acqStatusArgs;

//Size 31
typedef struct __attribute__((__packed__)){
    uint8_t                type;
    uint8_t                done;
    uint8_t                moduleError[4];
    bool                   indexError;
    uint64_t               savedFrameNum;
    uint64_t               savedAquisitionNum;
    uint64_t               indexSentAquisitionNum;    
    uint8_t                reserved[STRUCT_SIZE-31];
} saveStatusArgs;

//Size 261
typedef struct __attribute__((__packed__)){
    uint8_t                type;
    uint8_t                be_gid[4][16];
    uint8_t                fe_gid[4][16];
    uint64_t               fe_mac[4];
    uint64_t               be_mac[4];
    uint64_t               vaddr[4];
    uint32_t               rkey[4];
    uint32_t               qpn[4];
    uint32_t               bufferSize;
    uint8_t                reserved[STRUCT_SIZE-261];
} initArgs;

struct array_data
{
    pthread_mutex_t * mutex;
    int32_t * sample_frame;
};

typedef enum backend_status_t
{
	BACKEND_OFF = 0,
	BACKEND_ON = 1
} backend_status_t;

struct guess_end_context{
    struct timespec  sample_time;
    acqStatusArgs    cached_status;
    uint64_t         acquire_time_us;
    uint64_t         reqAcquisitions;
};


typedef enum pimega_sensor_type_t{
	silicon300um = 0, silicon675um = 1, cdte1mm = 2 ,
} pimega_sensor_type_t;

typedef enum pimega_detector_model_t{
	mobipix = 0, pimega45D = 1, pimega135D = 2 , pimega540D = 3,
} pimega_detector_model_t;

typedef enum pimega_thread_t {
	PIMEGA_THREAD_MAIN = 4,
	PIMEGA_THREAD_MODULE1 = 0,
	PIMEGA_THREAD_MODULE2 = 1, 
	PIMEGA_THREAD_MODULE3 = 2,
	PIMEGA_THREAD_MODULE4 = 3 
} pimega_thread_t;

typedef enum pimega_operation_mode_t {
	PIMEGA_READ_COUNTER_L = 0,
	PIMEGA_READ_COUNTER_H,
	PIMEGA_LOAD_COUNTER_L,
	PIMEGA_LOAD_COUNTER_H,
	PIMEGA_LOAD_DACS,
	PIMEGA_LOAD_CTPR,
	PIMEGA_READ_DACS,
	PIMEGA_READ_OMR,
	PIMEGA_OPERATION_MODE_ENUM_END,
} pimega_operation_mode_t;

typedef enum pimega_crw_srw_t {
	PIMEGA_CRW_SRW_MODE_SEQUENTIAL = 0,
	PIMEGA_CRW_SRW_MODE_CONTINUOUS,
	PIMEGA_CRW_SRW_MODE_ENUM_END,
} pimega_crw_srw_t;

typedef enum pimega_polarity_t {
	PIMEGA_POLARITY_ELECTRON = 0,
	PIMEGA_POLARITY_HOLES,
	PIMEGA_POLARITY_ENUM_END,
} pimega_polarity_t;

typedef enum pimega_dataout_t {
	PIMEGA_DATA_OUT_0 = 0,
	PIMEGA_DATA_OUT_2,
	PIMEGA_DATA_OUT_4,
	PIMEGA_DATA_OUT_8,
	PIMEGA_DATA_OUT_ENUM_END,
} pimega_dataout_t;

typedef enum pimega_discriminator_t {
	PIMEGA_DISCRIMINATOR_LOW = 0,
	PIMEGA_DISCRIMINATOR_HIGH,
	PIMEGA_DISCRIMINATOR_ENUM_END,
} pimega_discriminator_t;

typedef enum pimega_counterDepth_t {
	PIMEGA_COUNTERDEPTH_1BIT   = 0,
	PIMEGA_COUNTERDEPTH_12BITS,
	PIMEGA_COUNTERDEPTH_6BITS,
	PIMEGA_COUNTERDEPTH_24BITS,
	PIMEGA_COUNTERDEPTH_ENUM_END,
} pimega_counterDepth_t;

typedef enum pimega_spectroscopic_mode_t {
	PIMEGA_COLOUR_MODE_FINE_PITCH = 0,
	PIMEGA_COLOUR_MODE_SPECTROSCOPIC,
	PIMEGA_COLOUR_MODE_ENUM_END,
} pimega_spectroscopic_mode_t;

typedef enum pimega_pixel_mode_t {
	PIMEGA_PIXEL_MODE_SINGLE_PIXEL = 0,
	PIMEGA_PIXEL_MODE_CHARGE_SUMMING,
	PIMEGA_PIXEL_MODE_ENUM_END,
} pimega_pixel_mode_t;

typedef enum pimega_gain_mode_t {
	PIMEGA_GAIN_MODE_SUPER_HIGH = 0,
	PIMEGA_GAIN_MODE_LOW,
	PIMEGA_GAIN_MODE_HIGH,
	PIMEGA_GAIN_MODE_SUPER_LOW,
	PIMEGA_GAIN_MODE_ENUM_END,
} pimega_gain_mode_t;

typedef enum pimega_omr_operation_t {
	OMR_OP_READ=0,
	OMR_OP_WRITE,
	OMR_OP_READ_ALLSENSORS,
	OMR_OP_WRITE_ALLSENSORS,
	OMR_OP_READ_ALL_OMRS_ONESENSOR,
	OMR_OP_ENUM_END,
} pimega_omr_operation_t;

typedef enum pimega_omr_t {
	OMR_M=0,
	OMR_CRW_SRW,
	OMR_Polarity,
	OMR_PS,
	OMR_Disc_CSM_SPM,
	OMR_EnableTP,
	OMR_CountL,
	OMR_CollumBLock,
	OMR_CollumBLock_Sel,
	OMR_RowBlock,
	OMR_RowBlock_Sel,
	OMR_Equalization,
	OMR_Colour_Mode,
	OMR_CSM_SPM,
	OMR_Info_Header,
	OMR_Fuse_Sel,
	OMR_Fuse_Pulse_Width,
	OMR_Gain_Mode,
	OMR_Sense_DAC,
	OMR_Ext_DAC,
	OMR_Ext_BG_Sel,
	OMR_ENUM_END,
} pimega_omr_t;

typedef enum pimega_read_dac_t {
	DIGITAL_READ_SINGLE_DAC = 0,
	DIGITAL_READ_ALL_SENSORS = 2,
	DIGITAL_READ_ALL_DACS = 4,
	ANALOG_READ_SINGLE_DAC = 6,
	ANALOG_READ_ALL_DACS = 7,
	ANALOG_READ_ALL_SENSORS = 8,
} pimega_read_dac_t;

typedef enum pimega_write_dac_t {
	WRITE_SINGLE_DAC=1,
	WRITE_ALL_SENSORS=3,
	WRTIE_ALL_DACS=5,
} pimega_write_dac_t;

typedef enum pimega_dac_t {
    DAC_ThresholdEnergy0=1,     //1
    DAC_ThresholdEnergy1,       //2
	DAC_ThresholdEnergy2,		//3
	DAC_ThresholdEnergy3,		//4
	DAC_ThresholdEnergy4,		//5
	DAC_ThresholdEnergy5,       //6
	DAC_ThresholdEnergy6,		//7
	DAC_ThresholdEnergy7,		//8
    DAC_Preamp,					//9
    DAC_IKrum,                  //10
    DAC_Shaper,                 //11
    DAC_Disc,                   //12
    DAC_DiscLS,				    //13
    DAC_ShaperTest,             //14
    DAC_DiscL,                  //15
    DAC_Delay,                  //16
    DAC_TPBufferIn,             //17
    DAC_TPBufferOut,            //18
    DAC_RPZ,                    //19
    DAC_GND,                    //20
    DAC_TPRef,                  //21
    DAC_FBK,                    //22
    DAC_CAS,                    //23
    DAC_TPRefA,                 //24
    DAC_TPRefB,                 //25
	DAC_BandGapOutput,
	DAC_BandGapTemperature,
	DAC_DACBias,
	DAC_DACCascodeBias,
    DAC_Test,					//30
    DAC_DiscH,                  //31
	DAC_ENUM_END,
} pimega_dac_t;


typedef enum pimega_trigger_mode_t {
	PIMEGA_TRIGGER_MODE_INTERNAL = 0,
	PIMEGA_TRIGGER_MODE_EXTERNAL_POS_EDGE,
	PIMEGA_TRIGGER_MODE_EXTERNAL_NEG_EDGE,
	PIMEGA_TRIGGER_MODE_ENUM_END,
}pimega_trigger_mode_t;

//0: Cascate disabled, an internal trigger for each module (Default)
//1: Cascade enabled, internal trigger from master module, trigger output set by shutter time
//2: Cascade enabled, internal trigger from master module, trigger output set by acquisition time
//3: Cascade enabled, external trigger with positive edge at master module, trigger output set by shutter time
//4: Cascade enabled, external trigger with positive edge at master module, trigger output set by acquisition time



typedef enum pimega_trigger_out_t {
	PIMEGA_TRIGGER_OUT_DISABLE = 0,
	PIMEGA_TRIGGER_OUT_BOTH = 1,
	PIMEGA_TRIGGER_OUT_SW = 2,
	PIMEGA_TRIGGER_OUT_EXTERNAL = 3,
	PIMEGA_TRIGGER_OUT_SHUTTER_MBA = 4,
	PIMEGA_TRIGGER_OUT_SHUTTER_MBB = 5,
	PIMEGA_TRIGGER_OUT_SHUTTER_MBC = 6,
	PIMEGA_TRIGGER_OUT_SHUTTER_MBALL = 7,
	PIMEGA_TRIGGER_OUT_ACQ_MBA = 8,
	PIMEGA_TRIGGER_OUT_ACQ_MBB = 9,
	PIMEGA_TRIGGER_OUT_ACQ_MBC = 10,
	PIMEGA_TRIGGER_OUT_ACQ_MBALL = 11,
	PIMEGA_TRIGGER_OUT_ENUM_END = 12,
}pimega_trigger_out_t;


typedef enum pimega_read_counter_t {
	PIMEGA_COUNTER_LOW = 0,
	PIMEGA_COUNTER_HIGH,
	//PIMEGA_COUNTER_BOTH,
	PIMEGA_READ_COUNTER_ENUM_END,
} pimega_read_counter_t;


typedef enum pimega_column_t {
	PIMEGA_COLUMN_0 = 0,
	PIMEGA_COLUMN_4,
	PIMEGA_COLUMN_2,
	PIMEGA_COLUMN_6,
	PIMEGA_COLUMN_1,
	PIMEGA_COLUMN_5,
	PIMEGA_COLUMN_3,
	PIMEGA_COLUMN_7,
	PIMEGA_COLUMN_ENUM_END,
} pimega_column_t;

typedef enum pimega_row_count_t {
	PIMEGA_1_ROW = 0,
	PIMEGA_16_ROWS,
	PIMEGA_4_ROWS,
	PIMEGA_64_ROWS,
	PIMEGA_2_ROWS,
	PIMEGA_32_ROWS,
	PIMEGA_8_ROWS,
	PIMEGA_128_ROWS,
	PIMEGA_ROW_COUNT_ENUM_END,
} pimega_row_count_t;


typedef enum pimega_image_mode_t
{
	PIMEGA_IMAGE_MODE_SINGLE = 0,
	PIMEGA_IMAGE_MODE_MULTIPLE,
	PIMEGA_IMAGE_MODE_CONTINUOUS,
	PIMEGA_IMAGE_MODE_THRESHOLD,
	PIMEGA_IMAGE_MODE_TESTPULSE,
	PIMEGA_IMAGE_MODE_ENUM_END,
} pimega_image_mode_t;

typedef enum pimega_test_pulse_pattern_t {
	PIMEGA_TEST_PULSE_CLEAR = 0,
	PIMEGA_TEST_PULSE_SET,
	PIMEGA_TEST_PULSE_EVEN_COLUMNS,
	PIMEGA_TEST_PULSE_ODD_COLUMNS,
} pimega_test_pulse_pattern_t;

typedef enum pimega_medipix_mode_t {
	PIMEGA_MEDIPIX_MODE_DEFAULT = 0,			// Sequential (1x12-bit)
	//PIMEGA_MEDIPIX_MODE_CSM,					// not available 
	PIMEGA_MEDIPIX_MODE_CRW = 1,					// Continuous (2x12-bit)
	PIMEGA_MEDIPIX_MODE_24BITS = 2,					// Sequential (1x24-bit)
	PIMEGA_MEDIPIX_MODE_DUAL_ENERGY = 3,			// not available
	PIMEGA_MEDIPIX_MODE_ENUM_END,
} pimega_medipix_mode_t;

typedef struct pimega_params_t {
	pimega_detector_model_t detModel;
	pimega_dac_t dac;							//US_Set/Get DAC
	pimega_trigger_mode_t trigger_mode;			//US_TriggerMode
	bool discard_data;							//US_DiscardData
	float bias_voltage[2];						//US_SensorBias_RBV (Flex Low (0) and flex high (1))
	pimega_read_counter_t read_counter;
	pimega_image_mode_t image_mode;
	float mb_temperature[4][48];
	float mb_sensor_temp;
	float chip_temperature;
	float allchip_temperature[4][36];
	float avg_chip_temperature[4];
	char efuseID[8];
	bool software_trigger;						//US_SotwareTrigger
	bool external_band_gap;
	float extBgIn;								//US_ImgChip_ExtBgIN
	float dacOutput;							//US_ImgChipDACOUTSense_RBV
	pimega_trigger_out_t trigger_out;
} pimega_params_t;

typedef struct pimega_omr {
	pimega_operation_mode_t operation_mode;		//US_OmrOMSelec
	pimega_crw_srw_t crw_srw_mode;			    //US_ContinuousRW
	pimega_polarity_t polarity;					//US_Polarity
	pimega_dataout_t dataout; 					//US_OmrPSSelect
	pimega_discriminator_t discriminator;		//US_Discriminator
	bool enable_testPulse;						//US_TestPulse
	pimega_counterDepth_t counterDepth_mode; 	//US_CounterDepth (CountL - Medipix)
	bool equalization;							//US_Equalization
	pimega_spectroscopic_mode_t colour_mode; 	//US_SpectroscopicMode - ColourMode medipix (bit 20 OMR)
	pimega_pixel_mode_t pixel_mode;				//US_PixelMode
	pimega_gain_mode_t gain_mode;				//US_Gain
	uint8_t sense_dacSel;						//US_SenseDacSel
} pimega_omr;


typedef enum acquire_status_t{
	IDLE = 0,
    DONE_ACQ = 1,
	ACQUIRING = 2,
	BUFFER_OVERFLOW = 3,
    STOPPED = 4,
	DONE_BCK_ACQ = 5,
} acquire_status_t;

typedef struct pimega_acquire_params_t {
	uint32_t numImages;						//US_NumImages
	uint32_t numImagesCounter;				//US_NumImagesCounter_RBV
	uint32_t numExposures;					//US_NumExposures
	float acquireTime;						//US_AcquireTime
	float acquirePeriod;
	bool acquireState;						//US_Acquire_RBV
	char detectorState[512];				//US_DetectorState_RBV
	float timeRemaining;					//US_TimeRemaining_RBV
	uint32_t numExposuresCounter;
	uint32_t numExposuresTotal;				//US_NumExposuresCounter_RBV
	int numCapture;
	acquire_status_t acquireStatus;
} pimega_acquire_params_t;

enum moduleLoc{
    UP_LT = 0,
    UP_RT = 1,
    LW_LT = 2,
    LW_RT = 3,
    ALL   = 4,
    SINGLE = 5,
};

typedef enum pimega_send_to_all_t
{
	PIMEGA_SEND_ONE_CHIP_ONE_MODULE = 0,
	PIMEGA_SEND_ALL_CHIPS_ONE_MODULE,
	PIMEGA_SEND_ONE_CHIP_ALL_MODULES,
	PIMEGA_SEND_ALL_CHIPS_ALL_MODULES,
} pimega_send_to_all_t;

typedef enum pimega_send_mb_flex_t
{
	PIMEGA_ONE_MB_ONE_FLEX = 0,
	PIMEGA_ONE_MB_BOTH_FLEX,
	PIMEGA_ALL_MBS_ONE_FLEX,
	PIMEGA_ALL_MBS_BOTH_FLEX,
	PIMEGA_ALL_MBS_FLEX_BOTH_ALL_MODULES,
} pimega_send_mb_flex_t;

typedef enum pimega_mb_flex_t
{
	PIMEGA_MB_FLEX_LOW = 0,
	PIMEGA_MB_FLEX_HIGH,
	PIMEGA_MB_FLEX_ENUM_END,
} pimega_mb_flex_t;



typedef struct sensor {
    enum moduleLoc module;
    int mb;
    int chipId;
	int sensorPos;
} sensor;

extern struct sensor decoder540D[144];

typedef struct pimega_t {
	uint8_t max_num_modules; // Modules (135D)
	uint8_t max_num_boards;  // MFB Boards
	uint8_t max_num_chips;	 // Chips by mfb
	uint8_t num_all_chips;	 // All chips by module 
	uint8_t num_mb_tsensors;
	int pimega_interface;
	uint8_t pimega_module;
	int fd[4];
	int backend_socket;
	FILE *debug_out;
	pimega_omr omr;
	pimega_params_t pimegaParam;
	pimega_acquire_params_t acquireParam;
	int digital_dac_values[36][DAC_ENUM_END];
	float analog_dac_values[36][DAC_ENUM_END];
	int omr_values[OMR_ENUM_END];
	char file_template[PIMEGA_MAX_FILE_NAME];
	initArgs init_args;
	simpleArgs ack;
	saveStatusArgs saveargs;
    acqArgs acq_args;
    acqStatusArgs acq_status_return;
	sensor sensor_pos;
	pthread_mutex_t        backend_socket_mutex; 
	struct array_data      adata;
	int                    simulate;
	int mb_reg[5];
	uint32_t frame_size;
    int32_t *sample_frame;
	pimega_detector_model_t detModel;
	bool sensor_disabled[4][36];
	pimega_sensor_type_t sensor_type;
	uint32_t max_bias;
	uint8_t num_mb_sources;
	int     backendOn;
} pimega_t;

typedef struct dac_scan_t {
	pimega_dac_t dac;
	int initial;
	int final;
	int step;
	float acquireTime;
} dac_scan_t;

typedef struct pimega_dac_write_context
{
	dac_scan_t * scan_rq;
	pimega_t *pimega;
	pimega_thread_t owner;
} pimega_dac_write_context;

typedef struct pimega_temperature_context
{
	pimega_t *pimega;
	pimega_thread_t owner;
} pimega_temperature_context;

pimega_t *pimega_new(pimega_detector_model_t detModel);

int write_dac_all_modules(pimega_t *pimega, pimega_dac_t dac, int value);
int write_dac_all_modules_serial(pimega_t *pimega, pimega_dac_t dac, int value);


int US_DetectorState_RBV(pimega_t *pimega);
int efuseid_rbv(pimega_t *pimega);
int US_TimeRemaining_RBV(pimega_t *pimega);
int pimega_reset(pimega_t *pimega);
int pimega_reset_and_init(pimega_t *pimega, const char *file);
int US_Acquire(pimega_t *pimega, bool  action);
int US_Acquire_RBV(pimega_t *pimega);
int US_NumImages(pimega_t *pimega, unsigned num_images);
int US_NumImages_RBV(pimega_t *pimega);
int US_NumExposures(pimega_t *pimega, int num_exposures);
int US_NumExposures_RBV(pimega_t *pimega);
int US_NumExposuresCounter_RBV(pimega_t *pimega);

int US_Load_Equalization(pimega_t *pimega, uint8_t cfg_number, uint8_t sensor);
int US_ConfigDiscL(pimega_t *pimega, uint32_t value, pimega_send_to_all_t send_to);
int pixel_load(pimega_t *pimega, uint8_t sensor, uint32_t value);
int send_image(pimega_t *pimega, uint8_t send_to_all, uint8_t pattern);
int Set_Trigger(pimega_t *pimega, bool set_trigger);
int Set_Trigger_RBV(pimega_t *pimega);
int select_board(pimega_t *pimega, int board_id);
int select_board_rbv(pimega_t *pimega);
int select_chipNumber(pimega_t *pimega, int chip_id);
// ---------------------------------------------------------------------------------

// -------------- OMR Prototypes ---------------------------------------------------
int set_omr(pimega_t *pimega, pimega_omr_t omr, int value, pimega_send_to_all_t send_to);
int get_omr(pimega_t *pimega);
int US_OmrOMSelec(pimega_t *pimega, pimega_operation_mode_t operation_mode);
int US_OmrOMSelec_RBV(pimega_t *pimega);
int US_ContinuousRW(pimega_t *pimega, pimega_crw_srw_t crw_srw_mode);
int US_ContinuousRW_RBV(pimega_t *pimega);
int US_Polarity(pimega_t *pimega, pimega_polarity_t polarity);
int US_Polarity_RBV(pimega_t *pimega);
int US_OmrPSSelec(pimega_t *pimega, pimega_dataout_t dataout);
int US_OmrPSSelec_RBV(pimega_t *pimega);
int US_Discriminator(pimega_t *pimega, pimega_discriminator_t discriminator);
int US_Discriminator_RBV(pimega_t *pimega);
int US_TestPulse(pimega_t *pimega, bool test_pulse);
int US_TestPulse_RBV(pimega_t *pimega);
int US_CounterDepth(pimega_t *pimega, pimega_counterDepth_t mode);
int US_CounterDepth_RBV(pimega_t *pimega);
int US_Equalization(pimega_t *pimega, bool equalization);
int US_Equalization_RBV(pimega_t *pimega);
int US_Equalization_Default(pimega_t *pimega);
int US_Equalization_Region(pimega_t *pimega);
int US_SpectroscopicMode(pimega_t *pimega, pimega_spectroscopic_mode_t colour_mode);
int US_PixelMode(pimega_t *pimega, pimega_pixel_mode_t mode);
int US_PixelMode_RBV(pimega_t *pimega);
int US_Gain(pimega_t *pimega, pimega_gain_mode_t gain_mode);
int US_Gain_RBV(pimega_t *pimega);
int US_SenseDacSel(pimega_t *pimega, uint8_t dac);
int US_SenseDacSel_RBV(pimega_t *pimega);
// ----------------------------------------------------------------------------------

// ---------------- DAC Prototypes -------------------------------------------
int set_dac(pimega_t *pimega, pimega_dac_t dac, int value, pimega_send_to_all_t send_to);
int get_dac(pimega_t *pimega, pimega_read_dac_t read_mode, pimega_dac_t dac);
int Set_DAC_Defaults(pimega_t *pimega);

int US_Set_DAC_Variable(pimega_t *pimega, pimega_dac_t dac, int value, pimega_send_to_all_t send_to);
int US_Get_DAC_Variable(pimega_t *pimega, pimega_dac_t dac);
int US_DACBias_RBV(pimega_t *pimega);
int set_OptimizedDiscL(pimega_t *pimega);


// --------------------------------------------------------------------------

int US_ImgChipDACOUTSense_RBV(pimega_t *pimega);
int US_ImgChip_ExtBgIn(pimega_t *pimega, float voltage);
int US_ImgChip_ExtBgIn_RBV(pimega_t *pimega);
int US_BandGapOutput_RBV(pimega_t *pimega);
int US_BandGapTemperature_RBV(pimega_t *pimega);
int US_CascodeBias_RBV(pimega_t *pimega);

int setSensorBias(pimega_t *pimega, uint8_t source_sel, float voltage, pimega_send_mb_flex_t send_to);
int getSensorBias(pimega_t *pimega);
int US_SensorBias(pimega_t *pimega, uint8_t source_sel, float bias_voltage);
int US_SensorBias_RBV(pimega_t *pimega, uint8_t source_sel);

int US_AcquireTime(pimega_t *pimega, float acquire_time_s);
int US_AcquireTime_RBV(pimega_t *pimega);
int US_AcquirePeriod(pimega_t *pimega, float acq_period_time_s);
int US_AcquirePeriod_RBV(pimega_t *pimega);

int US_TriggerMode(pimega_t *pimega, pimega_trigger_mode_t trigger_mode);
int US_TriggerMode_RBV(pimega_t *pimega);
int US_SoftawareTrigger(pimega_t *pimega, bool software_trigger);
int US_SoftawareTrigger_RBV(pimega_t *pimega);

int US_ImgChipNumberID_RBV(pimega_t *pimega);

int US_ReadCounter(pimega_t *pimega, pimega_read_counter_t counter);
int US_ReadCounter_RBV(pimega_t *pimega);
int US_ImageMode(pimega_t *pimega, uint8_t image_mode);
int US_ImageMode_RBV(pimega_t *pimega);
int US_DiscardData(pimega_t *pimega, bool discard_data);
int US_DiscardData_RBV(pimega_t *pimega);
int getMB_Temperatures(pimega_t *pimega);
int get_SensorMB_Temperature(pimega_t *pimega, uint8_t sensorMB);
int getMedipixSensor_Temperature(pimega_t *pimega, int module);
int get_TemperatureSensorAvg(pimega_t *pimega);
int US_TemperatureChip(pimega_t *pimega);

int pimega_connect(pimega_t *pimega, const char *address[4], unsigned short *port);
int pimega_connect_backend(pimega_t *pimega, const char *address, unsigned short port);
void pimega_disconnect(pimega_t *pimega);
void pimega_disconnect_backend(pimega_t *pimega);
void pimega_delete(pimega_t *pimega);
int prepare_pimega(pimega_t *pimega);

int define_master_module(pimega_t *pimega, uint8_t module, bool ext_trigger, pimega_trigger_mode_t trigger_mode);
int select_module(pimega_t *pimega, int module);
int set_acquireTime(pimega_t *pimega, float acquire_time_s);
int set_periodTime(pimega_t *pimega, float period_time_s);
int set_numberExposures(pimega_t *pimega, int num_exposures);

int US_DAC_Scan(pimega_t *pimega, pimega_dac_t dac, int initial, int final, int step,
				pimega_send_to_all_t send_to);

int trigger_out(pimega_t *pimega, pimega_trigger_out_t trigger_out_mode);
int trigger_out_get(pimega_t *pimega);



// -------- Backend functions -----------------------------------
int receive_initArgs_fromBackend(pimega_t *pimega, int sockfd);
int send_allinitArgs(pimega_t *pimega, int module);
int send_allinitArgs_allModules(pimega_t *pimega);
int send_acqArgs_toBackend(pimega_t *pimega);
int get_acqStatus_fromBackend(pimega_t *pimega);
int get_saveStatus_fromBackend(pimega_t *pimega, uint64_t *savedAcquisitions); 
int send_stopAcquire_toBackend(pimega_t *pimega);
int update_backend_acqArgs(pimega_t *pimega, uint8_t aquisitionMode, bool useLFSR,
					uint8_t saveMode, bool resetRDMABuffer, bool bulkProcessing,
					enum IndexSendMode indexSendMode, const char *indexDestinationID,
					bool indexEnable);
int init_array_data(pimega_t *pimega);
void get_array_data(pimega_t *pimega);
void decode_backend_error(uint8_t ret, char *error);
bool evaluateBulkProcessing(enum bulkProcessingEnum bulkProcessing, float acquirePeriod, float acquireTime, bool externalTrigger, uint64_t capture);
int abort_save(pimega_t *pimega);
// ---------------------------------------------------------

int check_and_disable_sensors(pimega_t *pimega);

int execute_acquire(pimega_t *pimega);
int stop_acquire(pimega_t *pimega);
int status_acquire(pimega_t *pimega);
int set_file_name_template(pimega_t *pimega, const char *name);
int set_medipix_mode(pimega_t *pimega, pimega_medipix_mode_t medipix_mode);

const char *pimega_error_string(int error);
void pimega_set_debug_stream(pimega_t *pimega, FILE *stream);

typedef int (*method)(pimega_t *pimega, pimega_dac_t, int);
int run_dacs_all_chips(pimega_t *pimega, pimega_dac_t dac, int value, method _method);
int configure_module_dacs_with_file(pimega_t *pimega, const char * dac_file_ini);
#ifdef __cplusplus
} /* extern "C" */
#endif

#if __GNUC__ >= 4
#pragma GCC visibility pop
#endif

#endif /* _PIMEGA_H_INCLUDED_ */
