Tentu, kita bisa menggunakan pendekatan sederhana tanpa menggunakan built-in `sort`. Berikut adalah implementasinya:

```python
class PriorityQueueSorted:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def remove(self):
        if not self.is_empty():
            self.queue.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def add(self, data, priority):
        new_item = (data, priority)
        i = 0
        while i < len(self.queue) and priority >= self.queue[i][1]:
            i += 1
        self.queue.insert(i, new_item)

    def print_all(self):
        print([item[0] for item in self.queue])

# TEST CASE
myQueue = PriorityQueueSorted()

myQueue.add('Gian', 2)
myQueue.add('Kezia', 8)

myQueue.print_all()

print("Peek:", myQueue.peek())

myQueue.add('Glen', 5)
myQueue.add('Christo', 9)

myQueue.print_all()

print("Peek:", myQueue.peek())

print("========REMOVE========")

myQueue.remove()
myQueue.print_all()

myQueue.remove()
myQueue.print_all()

myQueue.remove()
myQueue.print_all()

myQueue.add('Saya', 7)
myQueue.print_all()
```

Anda dapat menjalankan kode ini untuk menguji implementasinya. buatKata(str):
    strLength = len(str)
    if strLength % 2 == 0:
       return str[0] + str[1]+str[2],"dan",str[-3]+ str[-2],str[1]
    else :
        midle = int(strLength/2)
        return str[midle - 1 ]+ str[midle]+str[midle+1]
word = input("Masukkan Kata ")
then = buatKata(word)
print("Huruf yang di ambil pada kata ", word,"adalah",then)


Tentu, kita bisa menggunakan pendekatan sederhana tanpa lambda. Berikut adalah implementasinya:

```python
class PriorityQueueSorted:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def remove(self):
        if not self.is_empty():
            self.queue.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def add(self, data, priority):
        new_item = (data, priority)
        inserted = False

        for i in range(len(self.queue)):
            if priority > self.queue[i][1]:
                self.queue.insert(i, new_item)
                inserted = True
                break

        if not inserted:
            self.queue.append(new_item)

    def print_all(self):
        print([item[0] for item in self.queue])

# TEST CASE
myQueue = PriorityQueueSorted()

myQueue.add('Gian', 2)
myQueue.add('Kezia', 8)

myQueue.print_all()

print("Peek:", myQueue.peek())

myQueue.add('Glen', 5)
myQueue.add('Christo', 9)

myQueue.print_all()

print("Peek:", myQueue.peek())

print("========REMOVE========")

myQueue.remove()
myQueue.print_all()

myQueue.remove()
myQueue.print_all()

myQueue.remove()
myQueue.print_all()

myQueue.add('Saya', 7)
myQueue.print_all()


class PriorityQueueSorted:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def len(self):
        if self.data == 0 :
            print('Data Kosong')
        else:
            panjang = len(self.data)
            print(f'Panjang Datanya adalah : {panjang}')

    def peek(self):
        if self.is_empty()==1:
            print('Data Kosong')
        else:
            return self.data[0][0]
        
    def remove(self):
        if not self.is_empty():
            self.data.pop(0)
    
    def add(self, item, priority):
        new_item = (item, priority)
        inserted = False

        for i in range(len(self.data)):
            if priority > self.data[i][1]:
                self.data.insert(i, new_item)
                inserted = True
                break

        if not inserted:
            self.data.append(new_item)
    def print_all(self):
       for i in self.data:
           print(i)
    def mergesort(self):
        if len(self)>1:
            mid = len(self)//2
            left = self[:mid]
            right = self[mid:]
            self.mergesort(left)
            self.mergesort(right)
            i = 0
            j = 0
            k= 0
            while i < len(left) and j < len(right):
                if len[i] >= right[j]:
                    self[k]= left[i]
                    i+=1
                else:
                    self[k]= right[j]
                    j+=1
                k+=1
            while i < len(left):
                self[k]=left[i]
                i+=1
                k+=1
            while j < len(right):
                self[k]= right[j]
                j+=1
                k+=1

myQueue = PriorityQueueSorted()

myQueue.add('Gian', 2)
myQueue.add('Kezia', 8)

myQueue.print_all()
print("Peek:", myQueue.peek())

myQueue.add('Glen', 5)
myQueue.add('Christo', 9)

myQueue.print_all()

print("Peek:", myQueue.peek())

print("========REMOVE========")

myQueue.remove()
myQueue.print_all()

myQueue.remove()
myQueue.print_all()

myQueue.remove()
myQueue.print_all()

myQueue.add('Saya', 7)
myQueue.print_all()


```


