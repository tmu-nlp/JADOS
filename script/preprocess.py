import re

def pre_process(full_text):
 
    for _ in range(int(max(full_text.count('（'), full_text.count('）')))):
        full_text = re.sub(r'（[^\（]+?）', '', full_text)

    full_text = re.sub('。　', '。', full_text)

    full_text = re.sub(r'＝.+?＝', '', full_text)
    full_text = re.sub(r'＝写真[^。]+?(撮影|提供)', '', full_text)
    full_text = re.sub(r'＝写真(|＜.+?＞|.*?(ＡＰ|ロイター|共同|ＵＰＩ))。', '。', full_text)

    full_text = re.sub(r'＝地図', '', full_text)
    full_text = re.sub(r'＝(グラフ|評価|イラスト)(|参照)。', '', full_text)              
    
    full_text = re.sub(r'【.+?】', '', full_text)
    full_text = re.sub(r'[…]+?', '', full_text)
    full_text = re.sub('――', '', full_text)
    full_text = re.sub('◇', '', full_text)
    
    return full_text


if __name__ == '__main__':
    full_text = ''
    pre_process(full_text)