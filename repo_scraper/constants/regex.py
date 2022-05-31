REGEX_URL = '\\\*(?:\'|\")*[a-zA-Z0-9-_]+://[a-zA-Z0-9-_]+:[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+:[a-zA-Z0-9-_]+/[' \
            'a-zA-Z0-9-_]+\\\*(?:\'|\")* '
REGEX_PASSWORD = '(\S*\\\*(?:\'|\")*(?:pass|PASS)\S*\\\*(?:\'|\")*\s*(?:=|<-|:)\s*\\\*(?:\'|\").+\\\*(?:\'|\"))'
REGEX_PWD = '(\S*\\\*(?:\'|\")*(?:p|P)\S*(?:w|W)\S*(?:d|D)\\\*(?:\'|\")*\s*(?:=|<-|:)\s*\\\*(?:\'|\").+\\\*(?:\'|\"))'
REGEX_IP = "\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
REGEX_BASE_64 = '(?:"|\')[A-Za-z0-9\\+\\\=\\/]{50,}(?:"|\')'
REGEX_FILE_NAME = '\s{1}(?:\'|\")*./{1}(.*)(?:\'|\")*'
REGEX_EXTENSION = '.*\.(\S+)$'
REGEX_GIT = '^https:\/\/github\.com\/[a-zA-Z0-9-_.]+\/[a-zA-Z0-9-_.]+\/?'