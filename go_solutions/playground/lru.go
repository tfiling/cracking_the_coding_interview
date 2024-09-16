package playground

import (
	"container/list"
)

type cachedEntry[K comparable, V any] struct {
	key K
	val V
}

type LRUCache[K comparable, V any] struct {
	// myCache stores the cached cachedEntry instances
	myCache *list.List
	// keyIndexes provides O(1) access to cached elements in myCache
	keyIndexes map[K]*list.Element
	limit      int
}

func (c *LRUCache[K, V]) Put(k K, v V) {
	if e, ok := c.keyIndexes[k]; ok {
		//Update cache with new value and mark usage
		c.myCache.MoveToFront(e)
		e.Value = cachedEntry[K, V]{k, v}
		return
	} else if c.myCache.Len() >= c.limit {
		//Cached is full - evict one value
		evictedElement := c.myCache.Back()
		evictedKey := evictedElement.Value.(cachedEntry[K, V])
		delete(c.keyIndexes, evictedKey.key)
		c.myCache.Remove(evictedElement)
	}
	newCacheEntry := cachedEntry[K, V]{k, v}
	newListElement := c.myCache.PushFront(newCacheEntry)
	c.keyIndexes[k] = newListElement
}

func (c *LRUCache[K, V]) Get(k K) (V, bool) {
	if e, ok := c.keyIndexes[k]; ok {
		//Cache hit
		c.myCache.MoveToFront(e)
		entry := e.Value.(cachedEntry[K, V])
		return entry.val, true
	}
	//Cache miss
	var empty V
	return empty, false
}

func NewLRUCache[K comparable, V any](limit int) *LRUCache[K, V] {
	return &LRUCache[K, V]{
		keyIndexes: make(map[K]*list.Element),
		myCache:    list.New(),
		limit:      limit,
	}
}
