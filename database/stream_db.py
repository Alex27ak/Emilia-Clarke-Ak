import pymongo

from info import DATABASE_URI, DATABASE_NAME

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

myclient = pymongo.MongoClient(DATABASE_URI)
mydb = myclient[DATABASE_NAME]
mycol = mydb["stream_db"]


async def add_stream_details(file_id, chat_id, message_id, file_unique_id):
    data = {"file_id": file_id, "chat_id": chat_id, "message_id": message_id, "file_unique_id": file_unique_id}

    try:
        mycol.insert_one(data)
    except Exception as e:
        logger.exception("Some error occurred!", exc_info=True)


async def get_stream_details(file_id, chat_id):
    return mycol.find_one({"file_id": file_id, "chat_id": chat_id})
