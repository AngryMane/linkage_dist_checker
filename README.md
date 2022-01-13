#How to use

```python
$python3 -m pip install -r requirements.txt
$python3 checker.py ここにチェックしたい文章を入力する
total_distance is 18.
"ここ" linked to "入力". distance is 7.
"チェック" linked to "文章". distance is 3.
"たい" linked to "チェック". distance is 2.
"文章" linked to "入力". distance is 2.
"に" linked to "ここ". distance is 1.
"し" linked to "チェック". distance is 1.
"を" linked to "文章". distance is 1.
"する" linked to "入力". distance is 1.
"入力" linked to "root". distance is 0.
```

If you want to check English sentences.

```python3
$python3 checker.py This\ is\ English\ sample. -l en
```

