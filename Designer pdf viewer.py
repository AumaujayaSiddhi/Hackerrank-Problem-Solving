# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true
def designerPdfViewer(h, word):
    max_word_height = h[ord(word[0])-97]
    for w in range(len(word)):
        max_word_height = max_word_height if h[ord(word[w])-97] < max_word_height else h[ord(word[w])-97]
    return max_word_height * len(word)