package main

import "fmt"

type User struct {
	Name string
	Email string
	Role string
}

func (u User) Print() {
	fmt.Printf("User: %s, Email: %s\n", u.Name, u.Email)
}

type Admin struct {
	User
	Role string
}

func (a Admin) Print() {
	fmt.Printf("Admin: %s, Email: %s\n", a.Name, a.Email)
}


func main() {
	admin := Admin{
		User: User{
			Name:  "John Doe",
			Email: "john@doe.com",
			Role: "user",
		},
		Role: "admin",
	}

	fmt.Println(admin.Role)
	fmt.Println(admin.User.Role)
}