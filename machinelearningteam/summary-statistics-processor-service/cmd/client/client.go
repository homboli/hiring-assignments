package main

import (
	"context"
	pb "github.com/homboli/hiring-assignments/machinelearningteam/summary-statistics-processor-service/proto"
	"io/ioutil"
	"log"
	"fmt"
	"google.golang.org/grpc"
)

const (
	host = "127.0.0.1:50053"
)

func main() {
	conn, err := grpc.Dial(host, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	client := pb.NewSummaryStatisticsProcessorClient(conn)
	document, err := ioutil.ReadFile("test.csv")
	if err != nil {
		log.Fatal("Couldn't read input document")
	}
	ctx := context.Background()
	resp, err := client.ProcessStatistics(ctx, &pb.ProcessStatisticsRequest{
		Document: &pb.Document{
			Content: document,
		},
		AggregationColumns: &pb.AggregationColumns{
			AggregationColumns: []string{"BankEntryAmount"},
		},
		ExcludedColumns: &pb.ExcludedColumns{
			ExcludedColumns: []string{"AccountName"},
		},
	})
	fmt.Println(err)
	

	ioutil.WriteFile("out.csv", resp.GetContent(), 0644)
}
