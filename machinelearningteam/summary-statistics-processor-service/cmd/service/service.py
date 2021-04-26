import grpc
import numpy as np
import pandas as pd

from api_pb2 import ProcessStatisticsReply
from api_pb2_grpc import SummaryStatisticsProcessorServicer, add_SummaryStatisticsProcessorServicer_to_server


def process_summary(csv_data_in, excluded_columns, aggregation_columns):
    df = pd.read_csv(csv_data_in)
	df = df.drop(excluded_columns, axis=1)
	df = df.groupby(aggregation_columns).count()
	return df.to_csv()


class SummaryStatisticsProcessorServer(SummaryStatisticsProcessorServicer):
    def Detect(self, request, context):
		processed_summary = process_summary(request.document)
        response = ProcessStatisticsReply(content = processed_summary)
        return response


if __name__ == '__main__':
    server = grpc.server(ThreadPoolExecutor())
    add_SummaryStatisticsProcessorServicer_to_server(SummaryStatisticsProcessorServer, server)
    port = 50051
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()
