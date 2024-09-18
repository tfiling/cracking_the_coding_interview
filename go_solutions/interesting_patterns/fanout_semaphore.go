package interesting_patterns

import (
	"fmt"
	"runtime"
)

func RunFanoutSem() {
	workParts := 2000
	concurrencySem := make(chan struct{}, runtime.NumCPU())
	resCh := make(chan string)
	for i := 0; i < workParts; i++ {
		go func(id int) {
			concurrencySem <- struct{}{}
			{
				fmt.Printf("Doing work %d\n", id)
				resCh <- fmt.Sprintf("Done %d", id)
			}
			<-concurrencySem
		}(i)
	}

	for i := 0; i < workParts; i++ {
		<-resCh
	}
	fmt.Println("Done")
	close(resCh)
}
