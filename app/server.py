import logging
import os
import sys
from concurrent import futures

from service import grpc_service

import config
import grpc
import service.grpc_exceptions.grpc_exceptions as gRPC_exceptions
from google.protobuf.json_format import MessageToDict
from service.logs_service.app_logs import config_logs, init_logging

sys.path.append(r"./grpc_file")

from grpc_file.bs_db_connector_msg import db_connector_pb2, db_connector_pb2_grpc
from grpc_file.default_msg import default_pb2


class DbConnectorService:
    def GetBalance(
        self, request: db_connector_pb2.UserId, context: grpc.ServicerContext
    ) -> db_connector_pb2.BalanceInfo:
        """
        Function taking user balance.

        Args:
            request (db_connector_pb2.UserId): A gRPC message containing information.
            context (grpc.ServicerContext): Metadata actual session.

        Returns:
            db_connector_pb2.BalanceInfo: A gRPC message containing response information.
        """
        logging.info("Started method: 'GetBalance'")
        try:
            user_id = request.user_id

            data = grpc_service.getBalance(user_id)

            response = db_connector_pb2.BalanceInfo(
                balance=data["balance"], currency=data["currency"]
            )

            logging.info("Finished method: 'GetBalance'")
            return response

        except Exception as e:
            logging.exception("Method 'GetBalance' ended with some errors:\n{e}")
            gRPC_exceptions.raise_unknown_grpc_exception(e=e, context=context)

    def GetUserInfo(
        self, request: db_connector_pb2.UserId, context: grpc.ServicerContext
    ) -> db_connector_pb2.UserInfo:
        """
        Function taking user info.

        Args:
            request (db_connector_pb2.UserId): A gRPC message containing information.
            context (grpc.ServicerContext): Metadata actual session.

        Returns:
            db_connector_pb2.UserInfo: A gRPC message containing response information.
        """
        logging.info("Started method: 'GetUserInfo'")
        try:
            user_id = request.user_id

            data = grpc_service.getUserInfo(user_id)

            response = db_connector_pb2.UserInfo(
                id=data["id"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                phone_number=data["phone_number"],
                address=data["address"],
                login=data["login"],
            )

            logging.info("Finished method: 'GetUserInfo'")
            return response

        except Exception as e:
            logging.exception("Method 'GetUserInfo' ended with some errors:\n{e}")
            gRPC_exceptions.raise_unknown_grpc_exception(e=e, context=context)


def run_server():
    """
    Function to start a gRPC server for handling incoming requests.

    Raises:
        Exception: An exception is raised if an error occurs during server startup or operation.
    """
    try:
        init_logging()
        config_logs()
        server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=config.WORKERS),
            options=[
                ("grpc.max_send_message_length", config.MAX_MSG_LENGTH),
                ("grpc.max_receive_message_length", config.MAX_MSG_LENGTH),
            ],
        )
        db_connector_pb2_grpc.add_DbConnectorServicer_to_server(
            DbConnectorService(), server
        )
        server.add_insecure_port("[::]:" + str(config.SERVICE_PORT))
        server.start()
        logging.info("MICROSERVICE IS WORKING")
        server.wait_for_termination()

    except Exception as e:
        if config.LOGGING_MODE == "DEBUG":
            raise
        logging.error("SERVER HAS STOPPED WORKING")
        logging.error(e)


if __name__ == "__main__":
    run_server()
