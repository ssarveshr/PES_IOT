/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.7 */

#ifndef PB_SHADOW_PB_H_INCLUDED
#define PB_SHADOW_PB_H_INCLUDED
#include <pb.h>

#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

/* Struct definitions */
typedef struct _Shadow {
    float temp_value;
    float humid_value;
} Shadow;


#ifdef __cplusplus
extern "C" {
#endif

/* Initializer values for message structs */
#define Shadow_init_default                      {0, 0}
#define Shadow_init_zero                         {0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define Shadow_temp_value_tag                    1
#define Shadow_humid_value_tag                   2

/* Struct field encoding specification for nanopb */
#define Shadow_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, FLOAT,    temp_value,        1) \
X(a, STATIC,   SINGULAR, FLOAT,    humid_value,       2)
#define Shadow_CALLBACK NULL
#define Shadow_DEFAULT NULL

extern const pb_msgdesc_t Shadow_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define Shadow_fields &Shadow_msg

/* Maximum encoded size of messages (where known) */
#define Shadow_size                              10

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif
