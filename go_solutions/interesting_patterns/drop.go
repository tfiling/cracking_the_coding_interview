package interesting_patterns

import (
	"fmt"
	"sync"
)

func Drop() {
	//A throttling pattern
	//In cases there are more than capacity pending request - drop any new incoming requests
	const capacity = 100
	ch := make(chan string, capacity)
	workParts := 2000
	var wg sync.WaitGroup
	wg.Add(1)

	go func() {
		for input := range ch {
			fmt.Printf("Doing work %s\n", input)
		}
		wg.Done()
	}()

	for i := 0; i < workParts; i++ {
		select {
		case ch <- fmt.Sprintf("Work %d", i):
			println("Delivered")
		default:
			fmt.Printf("Dropped work #%d\n", i)
		}
	}

	close(ch)
	wg.Wait()
}
