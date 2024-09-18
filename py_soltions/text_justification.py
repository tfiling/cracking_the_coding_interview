from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        global_cursor = 0
        lines = []
        while global_cursor < len(words):
            curr_cursor = global_cursor
            line_length = 0
            while curr_cursor < len(words) and line_length < maxWidth:
                line_length += len(words[curr_cursor])
                if line_length < maxWidth:
                    line_length += 1
                curr_cursor += 1
            curr_cursor -= 1 # curr_cursor is inclusive
            if line_length > maxWidth:
                line_length -= (len(words[curr_cursor]) + 1)
                curr_cursor -= 1
            spaces_to_distribute = maxWidth - sum([len(word) for word in words[global_cursor:curr_cursor+1]])
            words_in_line = curr_cursor - global_cursor + 1
            if words_in_line > 1:
                curr_line = ""
                even_spaces = int(spaces_to_distribute / (words_in_line - 1))
                uneven_spaces = spaces_to_distribute % (words_in_line - 1)
                for word, word_idx in zip(words[global_cursor:curr_cursor], range(words_in_line)):
                    curr_line += word
                    curr_line += even_spaces * " "
                    if word_idx < uneven_spaces:
                        curr_line += " "
                curr_line += words[curr_cursor]
            else:
                curr_line = words[global_cursor]
                curr_line += (maxWidth - len(words[global_cursor])) * " "
            lines.append(curr_line)
            global_cursor = curr_cursor + 1
        lines[-1] = left_justify(lines[-1], maxWidth)
        return lines

def left_justify(line, max_width):
    res = ""
    words = list(filter(bool, line.split(" ")))
    for word in words[:-1]:
        res += word
        res += " "
    res += words[-1]
    res += " " * (max_width - len(res))
    return res


if __name__ == '__main__':
    s = Solution()
    max_width = 20
    res = s.fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = max_width)
    print(res)
    for line in res:
        assert len(line) == max_width