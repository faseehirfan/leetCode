class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(line_words, line_len):
            """Justify a single line except for the last line."""
            spaces = maxWidth - line_len
            slots = len(line_words) - 1

            if slots == 0:
                return line_words[0] + ' ' * spaces

            spaces_per_slot, remainder = divmod(spaces, slots)
            gap = ' ' * spaces_per_slot

            parts = []
            for i, w in enumerate(line_words):
                parts.append(w)
                if i != len(line_words) - 1:
                    parts.append(gap)
                    if remainder:
                        parts.append(' ')
                        remainder -= 1
            return ''.join(parts)

        res = []
        cur_line = []
        cur_len = 0

        for word in words:
            if len(word) + cur_len + len(cur_line) <= maxWidth:
                cur_line.append(word)
                cur_len += len(word)
            else:
                res.append(justify(cur_line, cur_len))
                cur_line = [word]
                cur_len = len(word)

        # Last line: left-justified
        res.append(' '.join(cur_line).ljust(maxWidth))
        return res
