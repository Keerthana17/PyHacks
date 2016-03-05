inp_txt = input()
cy_txt = ''

i = len(inp_txt) - 1
while i>= 0:
	cy_txt = cy_txt + inp_txt[i]
	i = i-1

print(cy_txt)