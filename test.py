from generator import generator


gen = generator("[1-255].[1-255].[1-255].[1-255]")

print(gen.get())