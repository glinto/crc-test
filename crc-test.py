def crc16_modbus(buf: bytearray) -> int:
    # Until we implement the CRC16 algorithm properly, our code will break at the assertions 
    return 0

# Our test strings
phrases = [
    'Assorted Breath',
    'Robust Arch',
    'Prickly Scent',
    'Bustling Lumber',
    'Graceful Ticket'
]

# And their checksum, respectively
checksums = [
    17040,
    10013,
    55244,
    5881,
    10582
]

# Check if our CRC algorithm (crc16_modbus) works properly
for i in range(len(phrases)): 
    print(phrases[i], end='... ') 
    checksum = crc16_modbus(bytearray(phrases[i], 'utf-8'))
    assert checksum == checksums[i]
    print('ok!')


