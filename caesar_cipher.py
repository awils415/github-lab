shift = int(input("Shift: "))

message = str(input("Message: "))

encryption = ""

for i in range(len(message)):
  char = message[i]
  char = char.upper()
  if ord(char) >= 65 and ord(char) <= 90:
    encryption += chr((ord(char) + shift - 65) % 26 + 65)
  else:
    continue

n = 5
blocks = []

idx = 0
while idx < len(encryption):
    if idx + n < len(encryption):
        blocks.append(encryption[idx:idx + n])
    else:
        blocks.append(encryption[idx:len(encryption)])
    idx += n
    
out = ""
blocks_printed = 0
for block in blocks:
  out += block + " "
  blocks_printed += 1
  if blocks_printed % 5 == 0:
    out += "\n"
  else:
    continue
    
print(out)

