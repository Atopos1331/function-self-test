def myprint(*args, counter = [-1], **kwargs):
  counter[0] = counter[0] + 1
  print(counter[0])
  print(*args, **kwargs)

myprint("Hello, World!")
myprint("This is a test.")
myprint("Counter should be 2 now.")