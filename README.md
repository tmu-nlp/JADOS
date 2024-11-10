# JADOS
JADOS is a Japanese document-level text simplification dataset for the news and encyclopedia domains, as described in "A Document-Level Text Simplification Dataset for Japanese."

## Data structure
Each domain dataset is provided in JSON format.
- Mainichi corpus in News doamin: `data/mainichi_corpus/mainichi_vX.X.X.json`
- Wikipedia corpus in encyclopedia doamin: `data/wikipedia_corpus/wikipedia_vX.X.X.json`

### Mainichi corpus
**Note: To obtain the Mainichi corpus source and target texts, please purchase the 毎日新聞記事データ集 and 毎日小学生新聞記事データ集 corpora from 2013 to 2020 [[link]](https://www.nichigai.co.jp/dcs/index5.html).**

Each entry consists of the following objects.

    ┌──── year
    ├──── source
    │         ├──── id
    │         └──── text
    ├──── target
    │         ├──── id
    │         └──── text
    └──── annotations
              ├──── alignment_ids
              └──── simplification_labels

| Key | Type | Description |
| ---- | ---- |---- |
| year | str | Publication year of Mainichi Japanese Daily Newspaper and Mainichi Elementary School Newspaper articles. |
| source | dict | Mainichi Japanese Daily Newspaper article information extracted from data collection. |
| target | dict | Mainichi Elementary School Newspaper article information extracted from data collection.|
| id | str | Index article number of source/target article.  Extracted from the text annotated with the `＼Ｃ０＼` tag in data collection. |
| text | list[str\|int] | List of starting positions (character count) for each sentence of source/target full article. In the case of a source article, the first element stores the "title". Please replace "title" with the source article heading (the text to which the `＼Ｔ１＼` tag is assigned).<br> The full article was prepared using the following process. <br> ・The full text was derived by concatenating all the text annotated with the `＼Ｔ２＼` tag in the data collection. <br> ・The extracted full text was preprocessed using `script/preprocess.py`.|
| annotations | dict | Data manually annotated by a worker.  |
| alignment_ids | list[str\|int] | List of alignment IDs indicating the corresponding `source text` sentences annotated to each sentence in `target text`. If there is nothing to be aligned, '' is stored. The value minus 1 corresponds to the index of the list. |
| simplification_labels | list[str] | List of simplification operations assigned to each sentence in the source document. |

### Wikipedia corpus
Each entry consists of the following objects.


    ┌──── title
    ├──── class
    ├──── category
    ├──── source_text      
    └──── annotations
              ├──── targrt_text 
              ├──── simplification_labels
              ├──── alignment_ids
              ├──── summarization_ids
              │
              ├──── target_text
              ├──── simplification_labels
              ├──── alignment_ids
              └──── summarization_ids
| Key | Type | Description |
| ---- | ---- |---- |
| title | str | Wikipedia article title. |
| class | str | Class of Wikipedia articles ("featured" or "good"). |
| category | str | (Corpus version ≥ v0.1.3）<br>Categorical classification of Wikipedia articles (in English). <br><br>Types of categorical classification with English-Japanese correspondence:<br><blockquote>general works :総記, philosophy :哲学, history :歴史, social sciences :社会科学, natural sciences :自然科学, technology :技術, industry :産業, arts :芸術, language :言語, literature :文学</blockquote>|
| source_text | list[str] | List of a Wikipedia article split into sentences. The `title` is stored in the first element. |
| annotations | list | Data manually annotated and created by two workers. |
| target_text | list[str] | List of manually created simplified articles split into sentences. |
| simplification_labels | list[str] | List of simplification operations assigned to each sentence in the source document. |
| alignment_ids | list[str\|int] | List of alignment IDs indicating the corresponding `target_text` sentences annotated to each sentence in `source_text`. If there is nothing to be aligned, '' is stored. The value minus 1 corresponds to the index of the list. |
| summarization_ids | list[list[int]] | List indicating which sentences from the `source_text` were retained during the extractive summarization process to create the `target_text`. It contains as many elements as the number of extractive summaries performed. If no summarization was conducted, it is an empty list. |

  
**Note: Due to revisions made upon publication, the statistics in this dataset may differ from those presented in the paper.**


## Release Notes
### Mainichi corpus
| Version | Date | Updates |
| ---- | ---- |---- |
| 0.0.0 | May 2, 2024 | - |

### Wikipedia corpus
| Version | Date | Updates |
| ---- | ---- |---- |
| 0.0.0 | May 2, 2024 | - |
| 0.0.1 | June 17, 2024 | <ul> <li>Corrected the `source_text` of "0.999..." article.</li> <li>Sorted the `summarization_ids`.</li></ul>|
| 0.1.0 | June 18, 2024 | <ul> <li>Added the second paragraph of Wikipedia article to the `source_text` under 150 characters and then simplified it. </li></ul> |
| 0.0.2 <br> 0.1.1 | July 6, 2024 | <ul> <li>Corrected the `title`, `source_text` and `target_text` of some articles.</li></ul>|
| 0.0.3 <br> 0.1.2 | July 16, 2024 | <ul> <li>Corrected the `target_text` and `alignmnet_ids` of some articles.</li></ul>|
| 0.1.3 | November 10, 2024 | `category` was included in the key.<br> (The dataset split details for the experiments in the paper were provided in `experiment_dataset_splits/wikipedia_split_info.json`.)　|

## Citation
If you use of the dataset, please cite:

Yoshinari Nagai, Teruaki Oka, Mamoru Komachi. A Document-Level Text Simplification Dataset for Japanese. The 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), May 2024. [[link]](https://aclanthology.org/2024.lrec-main.41/)
