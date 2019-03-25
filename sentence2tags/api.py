from typing import List

from sklearn.externals import joblib

from sentence2tags.parser import Parser
from sentence2tags.utils import Tree, TxtLoader, Token


class Sentence2Tags(object):

    def __init__(self, model: Parser):
        self.model = model

    def predict(self, inputs: List[Tree]) -> List[Tree]:
        predictions = self.model.predict(inputs)
        return predictions
        # data = self.loader.load(params.test)
        # self.saver.save(params.pred_file, predictions)

    def __getitem__(self, item: Tree) -> Tree:
        return self.predict([item])[0]

    def save(self, path):
        joblib.dump(self.model, filename=path, compress=('lzma', 3))

    @staticmethod
    def load_model(path: str) -> 'Sentence2Tags':
        parser: Parser = joblib.load(filename=path)
        return Sentence2Tags(parser)


def sentence_to_conll(sentence: List[str]) -> List[str]:
    return [word_to_conll(word=w, index=i) for i, w in enumerate(sentence)]


def word_to_conll(word: str, index: int = 0,
                  lemma: str = '_', upostag: str = '_', xpostag: str = '_',
                  feats: str = '_', head: str = '_', deprel: str = '_', deps: str = '_', misc: str = '_') -> str:
    return "{index}\t{word}\t{lemma}\t{upostag}\t{xpostag}\t{feats}\t{head}\t{deprel}\t{deps}\t{misc}\n".format(
        word=word, index=index, lemma=lemma, upostag=upostag, xpostag=xpostag,
        feats=feats, head=head, deprel=deprel, deps=deps, misc=misc
    )


def sentence_to_tree(sentence: List[str], index: int = 0) -> Tree:
    conll_sentence = sentence_to_conll(sentence)
    columns = TxtLoader.columns

    tree = Tree(
        tree_id=index,
        tokens=[],
        words=[],
        comments=[],
    )

    fields = dict(zip(columns, ['__ROOT__'] * len(columns)))
    fields['id'] = '0'
    fields['head'] = '0'
    token = Token(fields=fields)
    tree.tokens.append(token)

    for line in conll_sentence:
        ls = line.strip().split('\t')
        token = Token(fields=dict(zip(columns, ls)))

        if '-' in ls[0] or '.' in ls[0]:
            tree.words.append(token)
        else:
            tree.tokens.append(token)
    return tree
