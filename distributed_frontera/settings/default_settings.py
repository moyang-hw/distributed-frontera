# -*- coding: utf-8 -*-
from frontera.settings.default_settings import *

CONSUMER_BATCH_SIZE = 512
DELAY_ON_EMPTY = 30.0
FRONTIER_GROUP = 'general'

HBASE_THRIFT_HOST = 'localhost'
HBASE_THRIFT_PORT = 9090
HBASE_NAMESPACE = 'crawler'
HBASE_DROP_ALL_TABLES = False
HBASE_METADATA_TABLE = 'metadata'
HBASE_USE_SNAPPY = False
HBASE_USE_COMPACT_PROTOCOL = False
HBASE_BATCH_SIZE = 9216
HBASE_STORE_CONTENT = False
HBASE_STATE_CACHE_SIZE_LIMIT = 3000000
HBASE_QUEUE_TABLE = 'queue'

INCOMING_TOPIC = 'frontier-done'

MESSAGE_BUS = 'distributed_frontera.messagebus.zeromq.MessageBus'
NEW_BATCH_DELAY = 30.0
OUTGOING_TOPIC = 'frontier-todo'
OVERUSED_SLOT_FACTOR = 2.0
SCORING_TOPIC = 'frontier-score'
SCORING_GROUP = 'strategy-workers'
SPIDER_LOG_PARTITIONS = 1
SPIDER_FEED_PARTITIONS = 2

URL_FINGERPRINT_FUNCTION = 'frontera.utils.fingerprint.hostname_local_fingerprint'

ZMQ_HOSTNAME = '127.0.0.1'
ZMQ_BASE_PORT = 5550


