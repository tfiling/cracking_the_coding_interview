package interesting_patterns

import (
	"fmt"
	"runtime"
)

func Pooling() {
	workParts := 2000
	ch := make(chan string)
	resCh := make(chan string, workParts)
	for i := 0; i < runtime.NumCPU(); i++ {
		go func() {
			for input := range ch {
				fmt.Printf("Doing work %s\n", input)
				resCh <- fmt.Sprintf("Done %s", input)
			}
		}()
	}

	for i := 0; i < workParts; i++ {
		ch <- fmt.Sprintf("Work %d", i)
	}
	for i := 0; i < workParts; i++ {
		<-resCh
	}
	fmt.Println("Done")
	close(ch)
	close(resCh)
}
