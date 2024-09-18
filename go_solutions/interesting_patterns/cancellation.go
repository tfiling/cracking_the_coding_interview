package interesting_patterns

import (
	"context"
	"fmt"
	"math/rand"
	"time"
)

func Cancellation() {
	doneCh := make(chan struct{})
	ctx, cancel := context.WithTimeout(context.Background(), time.Millisecond*150)
	defer cancel()

	go func() {
		//Simulate a long operation e.g. querying an API or a DB
		time.Sleep(time.Millisecond * time.Duration(rand.Intn(300)))
		doneCh <- struct{}{}
	}()

	select {
	case <-doneCh:
		fmt.Println("Done")
	case <-ctx.Done():
		fmt.Println("Timeout")
	}
}
