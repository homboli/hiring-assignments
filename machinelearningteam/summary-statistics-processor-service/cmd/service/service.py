import grpc
import numpy as np
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from io import StringIO
import api_pb2
from api_pb2_grpc import SummaryStatisticsProcessorServicer, add_SummaryStatisticsProcessorServicer_to_server


def process_summary(csv_data_in, columns, aggregate_functions):
    df = pd.read_csv(csv_data_in)
    df = df.drop(excluded_columns, axis=1)
    dfgb = df.groupby(columns).agg(aggregate_functions)
    return str.encode(dfgb.to_csv())

class SummaryStatisticsProcessorServer(SummaryStatisticsProcessorServicer):
    def ProcessStatistics(self, request, context):
        print(StringIO(request.document.content.decode("utf-8")))
        processed_summary = process_summary(StringIO(request.document.content.decode("utf-8")), [v for v in request.excludedColumns.excludedColumns], [v for v in request.aggregateFunctions.aggregateFunctions])
        print(process_summary)
        response = api_pb2.ProcessStatisticsReply(content = processed_summary)
        return response

if __name__ == '__main__':
    server = grpc.server(ThreadPoolExecutor())
    add_SummaryStatisticsProcessorServicer_to_server(SummaryStatisticsProcessorServer(), server)
    port = 50053
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print("jajj")
    server.wait_for_termination()
