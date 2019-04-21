import re
import matplotlib.pyplot as plt


def make_sbeve(sentence, outtake, drop_spaces=True, lowercase=True):
    try:
        sbeve = Sbeve(sentence, outtake, drop_spaces, lowercase)
        return sbeve
    except Exception:
        return None


class Sbeve:
    
    def __init__(self, sentence, outtake, drop_spaces=False, lowercase=True):
        out = outtake
        if drop_spaces:
            out = out.replace(' ', '')
        if lowercase:
            out = out.lower()

        placeholder = '\\w*'
        rgx_str = placeholder + placeholder.join(list(out))
        regex = re.compile(rgx_str)
        match = re.search(regex, sentence)

        if match is None:
            raise Exception

        self.full = sentence
        self.out = outtake
        self.reddit_part = self.get_reddit_part()
        self.meme = self.get_meme()

    def get_reddit_part(self):
        counter = 0
        ret = ''
        for char in self.full:
            if char == self.out[counter]:
                counter += 1
                continue
            else:
                ret += char
        return ret

    # Get Meme Representation
    def get_meme(self):
        counter = 0
        ret = ''
        streak = False
        for char in self.full:
            if char == self.out[counter]:
                if not streak:
                    ret += '['
                    ret += self.out[counter]
                    streak = True
                elif streak:
                    ret += self.out[counter]
                counter += 1
                continue
            else:
                if streak:
                    ret += ']'
                    streak = False
                ret += char
        if streak:
            ret += ']'
        return ret

    def visualize(self, save='', show=True):
        plt.text(0.5, 0.5, s=self.get_meme())
        plt.xlabel('')
        plt.ylabel('')
        plt.axis('off')
        if save != '':
            plt.savefig(save)
        if show:
            plt.show()

    def __str__(self):
        return self.meme
