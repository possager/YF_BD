#_*_coding:utf-8_*_
import rsa
import base64





publickey=u'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDxGs4EL\/W5fw0WAfy9bHmxss3ld8D2OiHwRhGC5S1+C+gIRGeMM7fkqWowQbZd3T\/rgE9l0YSCf8GG\/NUA1aTzB+4+NE+PGZU+m0qilN1BIJSwLZzw6anltAtoDQCShFQ0\/OMkbGmBiUkv9mTLAjDMlEJxUDeC6rR\/9Qzz0HWOkwIDAQAB'
# publickey=u'EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443'

# rsapubkey=int(publickey,16)
puibint=int(publickey,18)
print publickey

(pubk,prik)=rsa.newkeys(1024)


a=int(str(publickey).decode('utf-8'))

print a
# print pubk
# print prik



print rsa.PublicKey(n=16,e=a)



rsastr=rsa.encrypt(message='asdqwe123',pub_key='0822781a17f46a976df14b3c00772379')
print rsastr