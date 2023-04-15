def line(times, text):
	if text == "":
		text = "*"
	k = text[0]
	for i in range(0, times):
		print(k, end="")
    
def box_of_hashes(height):
    for i in range(0, height):
    	line(10, "#")
    	print("")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
