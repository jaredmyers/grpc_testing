package main

import (
	"context"
	"log"
	"time"

	pb "github.com/jaredmyers/grpc_testing/go_grpc/protos"
	"google.golang.org/grpc"
)

const serverAddr = "localhost:50051"

func main() {
	conn, err := grpc.Dial(serverAddr, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("Connection failed: %v", err)
	}
	defer conn.Close()
	c := pb.NewUsersClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	r, err := c.GetUsers(ctx, &pb.GetUsersRequest{})
	if err != nil {
		log.Fatalf("GetUsers error: %v", err)
	}

	log.Println(r)

	newUser := &pb.User{
		Id:       "3",
		Name:     "Henry",
		Email:    "lkjsdf.co",
		Password: "dfd",
	}
	req := &pb.CreateUserRequest{User: newUser}

	rr, err := c.CreateUser(ctx, req)
	if err != nil {
		log.Fatalf("CreateUser error: %v", err)
	}

	log.Println(rr)

	log.Println("getting users again..")
	r, err = c.GetUsers(ctx, &pb.GetUsersRequest{})
	if err != nil {
		log.Fatalf("GetUsers error: %v", err)
	}

	log.Println(r)
}
