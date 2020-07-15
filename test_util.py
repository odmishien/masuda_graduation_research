import unittest
import util

class TestUtil(unittest.TestCase):
    def test_get_num_of_sentences(self):
        text = "こんにちは！今日はいい天気だと思います。そう思いませんか？私は思いませんが...。"
        expected = 4
        got = util.get_num_of_sentences(text)
        self.assertEqual(expected, got)

    def test_get_num_of_comma(self):
        text = "あの、えっと、その、たくさん、読点を、打っています。"
        expected = 5
        got = util.get_num_of_comma(text)
        self.assertEqual(expected, got)

    def test_get_num_of_period(self):
        text = "吾輩は猫である。名前はまだない。どこで生れたか頓と見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。"
        expected = 4
        got = util.get_num_of_period(text)
        self.assertEqual(expected, got)

    def test_get_length_of_text(self):
        text = "これは8文字の文"
        expected = 8
        got = util.get_length_of_text(text)
        self.assertEqual(expected, got)

    def test_get_distance_btw_commas(self):
        text = "あの、えっと、その、たくさん、読点を、打っています。"
        expected = float(26 - 5 - 1) / (5 + 1)
        got = util.get_distance_btw_commas(text)
        self.assertEqual(expected, got)

    def test_get_kanji_content_rate(self):
        text = "漢字ひらがなカタカナ漢字ひらがなカタカナ"
        expected = float(4 / 20)
        got = util.get_kanji_content_rate(text)
        self.assertEqual(expected, got)

    def test_get_sentiment_polarity_score(self):
        text = '遅刻したけど楽しかったし嬉しかった。すごく充実した！'
        expected = (0.3333333333333333 + 1) / 2
        got = util.get_sentiment_polarity_score(text)
        self.assertEqual(expected, got)

    def test_get_raising_discussion_score(self):
        masuda_id = '20200628072917'
        bookmark_count = 1687
        expected = 346 / bookmark_count
        got = util.get_raising_discussion_score(masuda_id, bookmark_count)
        self.assertEqual(expected, got)

if __name__ == "__main__":
    unittest.main()
