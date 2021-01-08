import collections

input = ["eat", "tea", "tan", "ate", "nat", "bat"]

answer = []
input_dict = {}

# for word in input:
#     input_dict["".join(sorted(word))] = []
#
# for word in input:
#     input_dict["".join(sorted(word))].append(word)
#
# for word, word_arr in input_dict.items():
#     answer.append(word_arr)
#
# for word in input:
#     if "".join(sorted(word)) in input_dict:
#         input_dict["".join(sorted(word))].append(word)
#     else:
#         input_dict["".join(sorted(word))] = []
#         input_dict["".join(sorted(word))].append(word)

#
anagram = collections.defaultdict(list)

for word in input:
    anagram["".join(sorted(word))].append(word)
# sorted(input, key=lambda x: (x[0], x[1]))
