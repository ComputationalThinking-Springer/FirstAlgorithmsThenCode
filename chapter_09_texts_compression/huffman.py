# Program HUFFMAN in Python
# Figure 9.2 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


# loads auxiliary functions
from collections import defaultdict


def frequencies(t):
    f = defaultdict(int)
    for u in range(0, len(t)):
        f[t[u]] += 1

    return f


def huffman(sigma_f):
    """
    The Huffman algorithm for the statistical compression of texts.
    :param sigma_f: sequence of letters with relative frequency
    :return: tree for encoding the letters of the input text
    """
    tree = {u: (sigma_f[u], None, None) for u in sigma_f}
    s = {u: sigma_f[u] for u in sigma_f}

    for i in range(1, len(sigma_f)):
        u = sorted(s, key=s.get)[0]         # select the pair u and v such that f[u] and f[v] are minimum
        v = sorted(s, key=s.get)[1]
        w = '%s%s' % (u, v)                 # create the node w
        s[w] = s[u] + s[v]                  # add the pair <w, f[w]> to s
        del s[u]                            # delete u,v from s
        del s[v]
        tree[w] = (s[w], u, v)              # insert in the tree, the node w as parent of u and v

    return tree


def get_encoding(tree):
    root = sorted(tree, key=tree.get, reverse=True)[0]
    left = tree[root][1]
    right = tree[root][2]
    codex = dict()
    get_encoding_rec(tree, left, '0', codex)
    get_encoding_rec(tree, right, '1', codex)
    return codex


def get_encoding_rec(tree, u, code, codex):
    left = tree[u][1]
    right = tree[u][2]
    if (left is None) and (right is None):
        codex[u] = code
        return
    get_encoding_rec(tree, left, '0' + code, codex)
    get_encoding_rec(tree, right, '1' + code, codex)


def compress_huffman(t, code):
    """
    Compresses the text t by using the tree
    :param t: text to compress
    :param code: Huffman compression code
    :return: tc compressed text
    """

    tc = ''
    for i in range(0, len(t)):
        tc = tc + code[t[i]]

    return tc


def main():

    t = 'LABELLABALLA'
    print "\n Input text: ", t

    sigma_f = frequencies(t)
    # print sigma_f

    tree = huffman(sigma_f)
    # print tree

    code = get_encoding(tree)
    print "\n Huffman code: ", code

    tc = compress_huffman(t, code)
    print "\n Text compressed according to Huffman: ", tc


if __name__ == "__main__":
    main()
