package main

import (
	"context"
	"flag"
	"log"
	"net"

	pb "github.com/jaredmyers/grpc_testing/go_grpc/protos"
	"google.golang.org/grpc"
)

type Server struct {
	pb.UnimplementedUsersServer
	userStorage []*pb.User
}

func (s *Server) GetUsers(ctx context.Context, gU *pb.GetUsersRequest) (*pb.GetUsersResponse, error) {

	return &pb.GetUsersResponse{Users: s.userStorage}, nil
}

func (s *Server) CreateUser(ctx context.Context, gU *pb.CreateUserRequest) (*pb.CreateUserResponse, error) {
	log.Println("create user ran")

	/*
		createdUser := &pb.User{
			Id:       "test",
			Name:     "Larry",
			Email:    "email.co",
			Password: "pw2",
		}
	*/
	s.userStorage = append(s.userStorage, gU.User)

	return &pb.CreateUserResponse{User: gU.User}, nil
}

func main() {
	listenAddr := flag.String("listenAddr", ":50051", "server port")
	flag.Parse()

	listen, err := net.Listen("tcp", *listenAddr)
	if err != nil {
		log.Fatal(err)
	}

	s := grpc.NewServer()
	pb.RegisterUsersServer(s, &Server{})
	log.Printf("Listening at %v", listen.Addr())

	if err := s.Serve(listen); err != nil {
		log.Fatalf("Failed: %v", err)
	}

}
