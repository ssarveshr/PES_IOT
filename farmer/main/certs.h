#ifndef _CERTS_H_
#define _CERTS_H_

// Connection settings
#define DEVICE_ID "51b875d7-e35c-4baf-abc5-347da40bb14d"
#define DEVICE_NAME "Arduinoo"
#define MQTT_HOST "broker.golain.io"
#define MQTT_PORT "8083"
#define ROOT_TOPIC "/5441_b363/"

// Device Certificate
const char DEVICE_CERT[] = R"(-----BEGIN CERTIFICATE-----
MIIFFTCCA/2gAwIBAgIQYHkneL91zRgRfmOf2uRIWDANBgkqhkiG9w0BAQsFADBi
MQswCQYDVQQGEwJJTjELMAkGA1UECAwCTUgxDDAKBgNVBAcMA1BOUTEPMA0GA1UE
CgwGR29sYWluMQwwCgYDVQQLDANkZXYxGTAXBgNVBAMMEENFUlRJRklDQVRFIEFV
VEgwHhcNMjQxMDE5MDUxMDM3WhcNMzQxMDE3MDUxMDM3WjCCAQAxDDAKBgNVBAYT
A1VTQTETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNU2FuIEZyYW5jaXNj
bzEtMCsGA1UEChMkMzFlNGFmMTItNTRiNC00YWQ0LWFiMmEtMGM0ZGIyYjQ1NDQx
MVIwUAYDVQQLDElkZDkyODIyNS1hYjY3LTQxNTUtOWE3Ny1iYzJjYTNhNWY1MDA7
N2JmNzZmMjEtZGJkOS00OTg4LThkNjUtMTM0YWQyOTFiMzYzMREwDwYDVQQDEwhB
cmR1aW5vbzEtMCsGA1UEBRMkNTFiODc1ZDctZTM1Yy00YmFmLWFiYzUtMzQ3ZGE0
MGJiMTRkMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAsli+3kjhugbP
MmUuRUZ0rlba/Yk1RPYDJzracZCPjijnbCb0+sXJimUDRSscn6uQmAxv1dN0dlR3
upGQ3YYGg/wXlzOH5Gx9oAJsZsJdjaUKcJydidptNue+YaAYBKzQcCXczOVb4sjj
zV45jcyOTTb1rdlJ62FhmBBxI6kPMQtbX+PASJ6Y7lFeb5k0vwHTDz8fCpJYeawt
3ustKvELlGvjXDGD7cI0oSK+t48xk7al12Xx2eXP/AJSwK06VFrinQGT6rb2HTU3
1z2UJ2RY+EVyJYs6xGmJWVsd53YAxWUiblernTiUIsjGMyixx8p2dKzZiXwbD39h
5Wyv/iwW/uRXWzhUsHJeMO8m22FdVqrbnq/x/uNQc2c/2vlJA7Nae2OrSLFHTx0Q
TV/5UhyibUX7fXQ4+0VxkZzrzBznPscx+0E9uv4OQNxLGkG5OjYJowPd9V0Rwlgb
cURJwfZrjhkQlnFdTZ94Kf5+uAgzxbnm+Faj1cxQxsATIkkv+1jOd5uJ0RSLz3jY
MuNOV0quwalJ+USAqDYA1F6BdBrO5eK1vh12BYV2pvmLyL2rydaWgpAz96EIAVOz
UkfuzVuJxVJwM1SZyacq5GKuLWqxiEucWVhyzjnmvq28GfKoqSCcW0BhU/zcIPTf
+s2PBfp/wXuGEWrv7KTj8iheHVq0JA0CAwEAAaMnMCUwDgYDVR0PAQH/BAQDAgeA
MBMGA1UdJQQMMAoGCCsGAQUFBwMCMA0GCSqGSIb3DQEBCwUAA4IBAQCsDiie5Nbk
V5jXlm5Fihu545Mkp5rb/v1pmNTo71cCyulPW51Dwf1+8G5syI7q33+Q8MwOCaIB
vsJcZG6wfznky622bUvOMv4cKM9w0Q5UIJ9IK/LYtaq9HZcFK4byhgkS719KJ4D+
9Ax/+UbeTG/zNgxTha8e3pEq2oilmE/JpgmLgdpEOisjAtqbyq0kD0Cxq7YWXhGz
ypH9sqlnG4nSPjGbDIAstuitL+T9k14uzUo8rmWcdy/6nok5wTgTKn+EuAGh+8bI
VpEqQ6Y4niuJqRHwXf4/xYFpZJtHTUGv5fZmvimdsV6M8Xm0gaXoVl/Go5AsV/bC
uFFcHQ7d95yZ
-----END CERTIFICATE-----)";

// Device Private Key
const char DEVICE_PRIVATE_KEY[] = R"(-----BEGIN PRIVATE KEY-----
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
oHFYx2SBO3wDQcKhEYb47iGCQHSDEA==
-----END PRIVATE KEY-----)";

const char MQTT_BROKER_CERT[] = R"(-----BEGIN CERTIFICATE-----
MIIEoTCCA4mgAwIBAgIBAzANBgkqhkiG9w0BAQsFADBiMQswCQYDVQQGEwJJTjEL
MAkGA1UECAwCTUgxDDAKBgNVBAcMA1BOUTEPMA0GA1UECgwGR29sYWluMQwwCgYD
VQQLDANkZXYxGTAXBgNVBAMMEENFUlRJRklDQVRFIEFVVEgwHhcNMjMxMjA2MTky
NTQ0WhcNMjgwNjEyMTkyNTQ0WjB3MQswCQYDVQQGEwJJTjELMAkGA1UECAwCTUgx
DzANBgNVBAoMBkdvbGFpbjENMAsGA1UECwwEcHJvZDEZMBcGA1UEAwwQYnJva2Vy
LmdvbGFpbi5pbzEgMB4GCSqGSIb3DQEJARYRc3VwcG9ydEBnb2xhaW4uaW8wggIi
MA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQCMKByCbpWDRdHLA+Prfc2ccmzK
q1JbfiCfccH1zmuMYHXundiK+Cmm5qo/3bxfttXY+VNGzUMRUpfu9i3cqmHM7I+f
iGCITtu2guj8KFhepUheR3x8yRSOFjGzP42ru3EsQpGcLrY4HVx/lHb4PcIQuK19
dNjIlS8Mc8tjpdRQUmFKs6rMAV89VSq3RZJyGDnnvFUzc3DCoMM7lOB+Yyqpjrs7
cv2sorOJDwf4BRc1amn+emNtykIYolEg8LcWaMmp/8wb6SzCn8IG9L41rILrtb6Y
GUuS1kygarZf1jfAtgcTJcUHA174qvB66agBICaQ1Unh47TGTDP7BNjMdOUxWvHu
T6X9E0YVoKPw3+rXiSsaVmyWCipEZO+w348obIZvQfd1O7/btlAdx+jjNxfHC64E
foNbWuhT+JP5SHMOgFkGMKIoXKQrLvFtDECzZJ7Jzd2KWmunPY7md7Evh19rPUxw
fWhn73b9LBTc5Ut0VR2nRtCZrQWd2iktHhvVap4E87fHytx0L/+Hu45GJFYoRISW
usyIMKDqPUOQ7wXIf7zrt3w7UT/KbHwauRI189Izzya5EBzycZ0Iz1/4JA+BOACB
esg1ODKD3Aq+F6Tw6p846rv2grcvj2ZTjHlVTM3O9J2DhjCho4JQ/knn7PM2iKR4
TmtBwm1tH1NbrUTvnQIDAQABo00wSzAJBgNVHRMEAjAAMB0GA1UdDgQWBBR60TDH
n81N/S/c5EpASoF4GtjbDTAfBgNVHSMEGDAWgBS1We7i5hgfbNA9AXIgEpJbtzrN
MTANBgkqhkiG9w0BAQsFAAOCAQEALToS1AyEIPz9wnqh2YcxXL6n9h4OhCdPrMY7
Wt7c6vj+g5X49go5BJVemSFcPlb4d92XSHJE6yUR0Epmp1NevKL0oBLUFRn7Y24/
l77E/Feal5hf+XP1o1DtAxZ5vCCuzIaQzFajWfs/pbCbT4FYLgcNqim9f2zPnluP
hip1D1Bwii7bc4AmALBK7DiqZt+pfZek2FbHSuy75oQt78XQs5rSlwDLiGDbWnEt
b0IxjhjrWSkqMUVK8zQyt26uahiKFG+i0yM//4cH1s2DqAGIqLCscGviFyNqoH+E
qcrN71Su2y28GSwoiRKtXRKnO+amJ3+FgR1tA+HA9kmvGaGSXQ==
-----END CERTIFICATE-----)";


const char DEVICE_PRIVATE_KEY[] = R"(-----BEGIN CERTIFICATE-----
MIIEoTCCA4mgAwIBAgIBAzANBgkqhkiG9w0BAQsFADBiMQswCQYDVQQGEwJJTjEL
MAkGA1UECAwCTUgxDDAKBgNVBAcMA1BOUTEPMA0GA1UECgwGR29sYWluMQwwCgYD
VQQLDANkZXYxGTAXBgNVBAMMEENFUlRJRklDQVRFIEFVVEgwHhcNMjMxMjA2MTky
NTQ0WhcNMjgwNjEyMTkyNTQ0WjB3MQswCQYDVQQGEwJJTjELMAkGA1UECAwCTUgx
DzANBgNVBAoMBkdvbGFpbjENMAsGA1UECwwEcHJvZDEZMBcGA1UEAwwQYnJva2Vy
LmdvbGFpbi5pbzEgMB4GCSqGSIb3DQEJARYRc3VwcG9ydEBnb2xhaW4uaW8wggIi
MA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQCMKByCbpWDRdHLA+Prfc2ccmzK
q1JbfiCfccH1zmuMYHXundiK+Cmm5qo/3bxfttXY+VNGzUMRUpfu9i3cqmHM7I+f
iGCITtu2guj8KFhepUheR3x8yRSOFjGzP42ru3EsQpGcLrY4HVx/lHb4PcIQuK19
dNjIlS8Mc8tjpdRQUmFKs6rMAV89VSq3RZJyGDnnvFUzc3DCoMM7lOB+Yyqpjrs7
cv2sorOJDwf4BRc1amn+emNtykIYolEg8LcWaMmp/8wb6SzCn8IG9L41rILrtb6Y
GUuS1kygarZf1jfAtgcTJcUHA174qvB66agBICaQ1Unh47TGTDP7BNjMdOUxWvHu
T6X9E0YVoKPw3+rXiSsaVmyWCipEZO+w348obIZvQfd1O7/btlAdx+jjNxfHC64E
foNbWuhT+JP5SHMOgFkGMKIoXKQrLvFtDECzZJ7Jzd2KWmunPY7md7Evh19rPUxw
fWhn73b9LBTc5Ut0VR2nRtCZrQWd2iktHhvVap4E87fHytx0L/+Hu45GJFYoRISW
usyIMKDqPUOQ7wXIf7zrt3w7UT/KbHwauRI189Izzya5EBzycZ0Iz1/4JA+BOACB
esg1ODKD3Aq+F6Tw6p846rv2grcvj2ZTjHlVTM3O9J2DhjCho4JQ/knn7PM2iKR4
TmtBwm1tH1NbrUTvnQIDAQABo00wSzAJBgNVHRMEAjAAMB0GA1UdDgQWBBR60TDH
n81N/S/c5EpASoF4GtjbDTAfBgNVHSMEGDAWgBS1We7i5hgfbNA9AXIgEpJbtzrN
MTANBgkqhkiG9w0BAQsFAAOCAQEALToS1AyEIPz9wnqh2YcxXL6n9h4OhCdPrMY7
Wt7c6vj+g5X49go5BJVemSFcPlb4d92XSHJE6yUR0Epmp1NevKL0oBLUFRn7Y24/
l77E/Feal5hf+XP1o1DtAxZ5vCCuzIaQzFajWfs/pbCbT4FYLgcNqim9f2zPnluP
hip1D1Bwii7bc4AmALBK7DiqZt+pfZek2FbHSuy75oQt78XQs5rSlwDLiGDbWnEt
b0IxjhjrWSkqMUVK8zQyt26uahiKFG+i0yM//4cH1s2DqAGIqLCscGviFyNqoH+E
qcrN71Su2y28GSwoiRKtXRKnO+amJ3+FgR1tA+HA9kmvGaGSXQ==
-----END CERTIFICATE-----)";

#endif