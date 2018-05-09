#trial = input()
trial = '1S2D*3T'
trial = '1D2S#10S'
trial = '1D2S0T'
trial = '1S*2T*3S'
trial = '1D#2S*3S'
trial = '1T2D3D#'
trial = '1D2S3T*'
indexInfo = []
threeParts = [] * 3
for idx in range(len(trial)):
    if trial[idx].isnumeric():
        indexInfo.append('N')
    else:
        indexInfo.append('S')

print(indexInfo)
for i in range(1,len(indexInfo)):
    if indexInfo[i-1] == 'S' and indexInfo[i] == 'N':
        threeParts.append(trial[:i])

threeParts[0] = threeParts[0]
threeParts[1] = threeParts[1][len(threeParts[0]):]
threeParts.append(trial[len(threeParts[0]) + len(threeParts[1]):])

print(threeParts)
scores = [0] * 3

# First Score
if 'S' in threeParts[0]:
    num, char = threeParts[0].split('S')
    scores[0] += int(num) ** 1
elif 'D' in threeParts[0]:
    num, char = threeParts[0].split('D')
    scores[0] += int(num) ** 2
else:
    num, char = threeParts[0].split('T')
    scores[0] += int(num) ** 3

if '*' in threeParts[0]:
    scores[0] *= 2
if '#' in threeParts[0]:
    scores[0] *= -1

# Second Score

if 'S' in threeParts[1]:
    num, char = threeParts[1].split('S')
    scores[1] += int(num) ** 1
elif 'D' in threeParts[1]:
    num, char = threeParts[1].split('D')
    scores[1] += int(num) ** 2
else:
    num, char = threeParts[1].split('T')
    scores[1] += int(num) ** 3

if '*' in threeParts[1]:
    scores[0] *= 2
    scores[1] *= 2
if '#' in threeParts[1]:
    scores[1] *= -1

# Third Score
if 'S' in threeParts[2]:
    num, char = threeParts[2].split('S')
    scores[2] += int(num) ** 1
elif 'D' in threeParts[2]:
    num, char = threeParts[2].split('D')
    scores[2] += int(num) ** 2
else:
    num, char = threeParts[2].split('T')
    scores[2] += int(num) ** 3

if '*' in threeParts[2]:
    scores[1] *= 2
    scores[2] *= 2
if '#' in threeParts[2]:
    scores[2] *= -1
print(sum(scores))